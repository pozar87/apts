# Django Integration Guidelines for `apts` Equipment

This document provides architectural and implementation guidelines for an agent building a Django application to persist and manage `apts` optical equipment.

## 1. Core Model Architecture

To avoid data loss and maintain the flexibility of the `apts` system, use a **Polymorphic** or **Single Table Inheritance** pattern, complemented by a dedicated **Port** model.

### 1.1 Base `Equipment` Model
Stores shared technical properties found in the `OpticalEquipment` base class.
- `brand` (CharField)
- `name` (CharField)
- `mass_g` (FloatField): Mass in grams.
- `optical_length_mm` (FloatField): Optical length in mm.
- `equipment_type` (CharField): Mapped to `OpticalType` enum.

### 1.2 Specific Properties
Depending on the volume of equipment types, use one of:
- **Polymorphic Models**: (e.g., `django-polymorphic`) `Telescope`, `Camera`, `Eyepiece` as subclasses.
- **JSONField**: A single `metadata` field to store type-specific properties (e.g., `aperture`, `read_noise`) if high schema flexibility is needed.

### 1.3 `ConnectionPort` Model (Crucial)
Hardware can now have multiple ports. Do **not** store connection types as single fields on the equipment model.
- `equipment` (ForeignKey to Equipment)
- `direction` (CharField): 'IN' or 'OUT'.
- `connection_type` (CharField): Mapped to `ConnectionType` enum (e.g., 'T2', 'M48').
- `gender` (CharField): 'M', 'F', or null.
- `label` (CharField, optional): e.g., "Guide Port", "Main Output".

## 2. Data Migration Strategy

The migration must ingest all existing hardware from the `apts` Python database without data loss.

### 2.1 Ingestion Flow
1.  Iterate through all subclasses of `apts.opticalequipment.OpticalEquipment`.
2.  Retrieve the `_DATABASE` dictionary from each class.
3.  For each entry:
    - Call `cls.normalize_database_entry(entry)` to handle guessed properties (like aperture from name).
    - Map generic fields to the `Equipment` model.
    - Map specific fields (e.g., `aperture_mm`, `sensor_width_mm`) to the specific model or JSON metadata.

### 2.2 Legacy Field Mapping (Port Logic)
Legacy database entries use `tside_*` and `cside_*` keys. These must be converted into structured `ConnectionPort` records:
- **`tside_thread`**: Create an **INPUT** port. Use `tside_gender` if present, otherwise use `get_default_gender(type, is_input=True)`.
- **`cside_thread`**: Create an **OUTPUT** port. Use `cside_gender` if present, otherwise use `get_default_gender(type, is_input=False)`.
- **`t2_output: True`**: Create an additional **OUTPUT** port of type `T2` and gender `MALE`.
- **`outputs: [...]`**: Iterate and create an **OUTPUT** port for each entry in the list.

## 3. Unit Management

The `apts` library uses `pint` for unit safety.
- **Database**: Store raw magnitudes in standard units (mm, grams, degrees, e-).
- **Application Layer**: Implement a `.to_apts()` method on your Django models that returns a fully instantiated `apts` object (e.g., `Telescope(...)`) with proper `pint` quantities.

## 4. Validation & Integrity

1.  **Unique Identity**: Use the hardware `brand` and `name` (or the `_DATABASE` key) to prevent duplicate imports.
2.  **Port Requirements**:
    - `Telescope` must have at least one Output.
    - `Camera`/`Eyepiece` must have at least one Input.
    - `Intermediate` equipment must have at least one of each.
3.  **Gender Defaults**: If the database record has a null gender, always use `apts.utils.get_default_gender()` during the migration to ensure future compatibility.

## 5. Implementation Example (`to_apts`)

```python
def to_apts(self):
    # 1. Gather ports
    inputs = [(p.connection_type, p.gender) for p in self.ports.filter(direction='IN')]
    outputs = [(p.connection_type, p.gender) for p in self.ports.filter(direction='OUT')]

    # 2. Instantiate based on type
    if self.type == 'TELESCOPE':
        return Telescope(
            aperture=self.metadata['aperture'],
            focal_length=self.metadata['focal_length'],
            vendor=f"{self.brand} {self.name}",
            mass=self.mass_g,
            optical_length=self.optical_length_mm,
            inputs=inputs,
            outputs=outputs
        )
```
