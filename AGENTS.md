# Weather Feature Updates for Agents

This document describes the new weather analysis and plotting features added to the `apts` library.

## Custom Conditions Support

You can now pass an optional `Conditions` object to several methods in the `Observation` class to perform weather analysis or generate plots against custom thresholds.

### Supported Methods in `Observation`:
- `get_weather_analysis(conditions=None, language=None)`
- `is_weather_good(conditions=None)`
- `get_hourly_weather_analysis(conditions=None, language=None)`
- `plot_weather(conditions=None, dark_mode_override=None, language=None, **args)`
- All new individual plot methods (see below).

### Caching Behavior:
When `conditions=None` (the default), `get_weather_analysis` caches its results in `self._weather_analysis`. If custom `conditions` are provided, the analysis is performed on-the-fly and the results are **not** cached, ensuring that the default state of the `Observation` object remains consistent.

## Individual Weather Plots

The library now supports plotting individual weather parameters. These plots automatically include:
- Background shading for night periods.
- Background shading for moon-up periods.
- Highlighting (using `axhspan`) for "good" condition ranges based on the provided or default `Conditions`.

### New `Observation` methods:
- `plot_clouds(conditions=None, ...)`
- `plot_clouds_summary(...)`
- `plot_precipitation(conditions=None, ...)`
- `plot_precipitation_type_summary(...)`
- `plot_temperature(conditions=None, ...)`
- `plot_wind(conditions=None, ...)`
- `plot_pressure_and_ozone(...)`
- `plot_visibility(conditions=None, ...)`
- `plot_moon_illumination(conditions=None, ...)`
- `plot_fog(conditions=None, ...)`
- `plot_aurora(conditions=None, ...)`

### New `Plotter` methods (accessible via `obs.plot`):
- `clouds(conditions=None, ...)`
- `clouds_summary(...)`
- `precipitation(conditions=None, ...)`
- `precipitation_type_summary(...)`
- `temperature(conditions=None, ...)`
- `wind(conditions=None, ...)`
- `pressure_and_ozone(...)`
- `visibility(conditions=None, ...)`
- `moon_illumination(conditions=None, ...)`
- `fog(conditions=None, ...)`
- `aurora(conditions=None, ...)`

## Usage Example

```python
from apts.observations import Observation
from apts.conditions import Conditions

# Define custom conditions
my_conditions = Conditions(max_clouds=50, max_wind=20)

# Check if weather is good against custom conditions
is_good = obs.is_weather_good(conditions=my_conditions)

# Generate a clouds plot with custom threshold highlighted
obs.plot_clouds(conditions=my_conditions)
```
