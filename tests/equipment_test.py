import pytest
import numpy as np # Added for np.log10
import pandas as pd # Added for DataFrame operations
from unittest.mock import patch, MagicMock, ANY

from apts import equipment # This is apts.equipment module
from apts.equipment import Equipment # Import Equipment class directly
from apts.constants import EquipmentTableLabels, GraphConstants, NodeLabels
from apts.constants.graphconstants import OpticalType, get_plot_style, get_plot_colors # Added get_plot_colors
from apts.config import get_dark_mode
from apts.opticalequipment import Barlow, Binoculars, Telescope, Camera, Eyepiece # Added Telescope, Camera, Eyepiece
from apts.utils import ureg, ConnectionType # Added ureg, ConnectionType
from . import setup_equipment


def test_zoom():
  e = setup_equipment()
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 = 30
  assert row[EquipmentTableLabels.ZOOM] == 30
  # Only possiable fov should be 2.333 ± 0.001
  assert row[EquipmentTableLabels.FOV] == pytest.approx(2.333, 0.001)
  # Range 12.880 ± 0.001
  assert row[EquipmentTableLabels.RANGE] == pytest.approx(13.580, 0.001)


def test_barlow():
  e = setup_equipment()
  e.register(Barlow(2))
  row = e.data().iloc[0]
  # Only possiable zoom should be 750/25 * 2 = 60
  assert row[EquipmentTableLabels.ZOOM] == 60
  # Using 3 elements
  assert row[EquipmentTableLabels.ELEMENTS] == 3


def test_barlow_stacking():
  e = setup_equipment()
  e.register(Barlow(2)) # Changed to use Barlow directly
  e.register(Barlow(3)) # Changed to use Barlow directly
  # Get row with biggest zoom
  row = e.data().sort_values(by=EquipmentTableLabels.ZOOM, ascending=False).iloc[0]
  # With two stacked barlows max zoom should be 180 (30 * 3 * 2)
  assert row[EquipmentTableLabels.ZOOM] == 180
  # Using 4 elements
  assert row[EquipmentTableLabels.ELEMENTS] == 4


def test_multi_barlow():
  e = setup_equipment()
  e.register(Barlow(2)) # Changed to use Barlow directly
  e.register(Barlow(3)) # Changed to use Barlow directly
  # With two barlows and single eyepiece number of possiable connection is 4 (with barlow stacking)
  assert len(e.data()[EquipmentTableLabels.ZOOM]) == 4


def test_camera_path_with_setup_equipment(): # Renamed
  e = setup_equipment()
  # The telescope from setup_equipment() is Telescope(150, 750, t2_output=True, vendor="unknown telescope")
  # Let's find this telescope instance from the equipment graph for later assertion
  # NodeLabels is already imported at the top
  setup_tele = None
  for v in e.connection_garph.vs:
      node_equipment_attr = v.attributes().get(NodeLabels.EQUIPMENT) # Use NodeLabels for graph attributes
      if isinstance(node_equipment_attr, Telescope) and \
         node_equipment_attr.focal_length.magnitude == 750 and \
         node_equipment_attr.aperture.magnitude == 150:
          setup_tele = node_equipment_attr
          break
  assert setup_tele is not None, "Could not find the telescope from setup_equipment"

  cam_vendor = "OriginalTestCam"
  cam = Camera(30, 40, 100, 200, vendor=cam_vendor) # Changed to use Camera directly
  e.register(cam)

  # Retrieve OpticalPath objects
  all_image_ops = e._get_paths(GraphConstants.IMAGE_ID)
  target_op = None
  for op in all_image_ops:
      # Identify the path with the setup_tele and the new cam
      if (isinstance(op.telescope, Telescope) and # Changed to use Telescope directly
          op.telescope.focal_length.magnitude == 750 and # Check properties of setup_tele
          isinstance(op.output, Camera) and # Changed to use Camera directly
          op.output.vendor == cam_vendor and
          not op.barlows and # Ensure no barlows
          op.length() == 2):
          target_op = op
          break

  assert target_op is not None, "Specific Telescope -> Camera path not found"

  # Verify components
  assert target_op.telescope == setup_tele
  assert target_op.output == cam
  assert not target_op.barlows

  # Verify Calculations
  # Zoom: telescope.focal_length / camera._zoom_divider()
  # The existing test asserted zoom == 15. Let's verify this with the formula.
  # Camera._zoom_divider() = sqrt(sensor_width^2 + sensor_height^2)
  # For Camera(30, 40, ...), sensor_width=30, sensor_height=40.
  # _zoom_divider = sqrt(30^2 + 40^2) = sqrt(900 + 1600) = sqrt(2500) = 50.
  # Telescope focal length = 750mm.
  # Expected zoom = 750 / 50 = 15.
  expected_zoom = setup_tele.focal_length.magnitude / cam._zoom_divider().magnitude
  assert target_op.zoom().magnitude == pytest.approx(expected_zoom)
  assert target_op.zoom().magnitude == pytest.approx(15) # Confirm original assertion value

  # FOV: (camera.sensor_height.magnitude * 3438 / (telescope.focal_length.magnitude * 1.0)) / 60
  expected_fov = (cam.sensor_height.magnitude * 3438 /
                  (setup_tele.focal_length.magnitude * 1.0)) / 60 # No barlow (mag=1.0)
  assert target_op.fov().magnitude == pytest.approx(expected_fov)

  # Verify the original DataFrame check for completeness, though target_op checks are more robust
  data_df = e.data()
  image_paths_df = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

  # Find the row corresponding to target_op for DataFrame value check
  found_in_df = False
  for _, row in image_paths_df.iterrows():
      if (cam_vendor in row[EquipmentTableLabels.LABEL] and
          setup_tele.vendor in row[EquipmentTableLabels.LABEL] and # "unknown telescope"
          row[EquipmentTableLabels.ELEMENTS] == 2):
          assert row[EquipmentTableLabels.ZOOM] == pytest.approx(15)
          found_in_df = True
          break
  assert found_in_df, "Path not found or zoom incorrect in DataFrame for the specific Camera path"


def test_telescope(): # Corrected typo from telecsope to telescope
  t = Telescope(150, 750) # Changed to use Telescope directly
  assert t.dawes_limit().magnitude == pytest.approx(0.773, 0.001)

# --- Binocular Tests ---

def test_binoculars_instantiation():
    bino = Binoculars(
        magnification=10,
        objective_diameter=50,
        vendor="TestBino",
        apparent_fov_deg=65,
        focal_length=1 # Nominal
    )
    assert bino.magnification == 10
    assert bino.objective_diameter.magnitude == 50
    assert bino.objective_diameter.units == ureg.mm
    assert bino.vendor == "TestBino"
    assert bino.apparent_fov_deg.magnitude == 65
    assert bino.apparent_fov_deg.units == ureg.deg
    assert str(bino) == "TestBino 10x50"
    assert bino.fov().magnitude == pytest.approx(6.5) # 65/10
    assert bino.fov().units == ureg.deg
    assert bino.exit_pupil().magnitude == pytest.approx(5) # 50/10
    assert bino.exit_pupil().units == ureg.mm
    assert bino.dawes_limit().magnitude == pytest.approx(11.6 / 5.0) # 11.6 / 5.0 cm = 2.32
    assert bino.rayleigh_limit().magnitude == pytest.approx(13.8 / 5.0) # 13.8 / 5.0 cm = 2.76
    # limiting_magnitude: 7.7 + 5 * log10(objective_diameter_cm) = 7.7 + 5 * log10(5.0)
    assert bino.limiting_magnitude() == pytest.approx(7.7 + 5 * np.log10(5.0), abs=1e-3)
    assert bino.brightness() == pytest.approx((5.0/7.0)**2 * 100) # (exit_pupil_mm / 7)^2 * 100
    assert bino.output_type() == "Visual"
    assert bino.max_useful_zoom() == 10

def test_binoculars_registration_and_graph():
    eq = Equipment() # Fresh equipment instance, uses Equipment class
    bino = Binoculars(magnification=10, objective_diameter=50, vendor="TestBino", apparent_fov_deg=65)
    eq.register(bino)

    # Check graph connections
    # 1. Binoculars node exists
    bino_node_id_in_graph = None
    for v in eq.connection_garph.vs:
        if v[NodeLabels.EQUIPMENT] == bino: # Use NodeLabels directly
            bino_node_id_in_graph = v[NodeLabels.NAME] # Use NodeLabels directly
            break
    assert bino_node_id_in_graph is not None, "Binoculars node not found in graph"

    # 2. Connected from SPACE
    space_node = eq.connection_garph.vs.find(name=GraphConstants.SPACE_ID)
    bino_vertex_index = eq.connection_garph.vs.find(name=bino_node_id_in_graph).index
    assert eq.connection_garph.get_eid(space_node.index, bino_vertex_index, directed=True, error=False) >= 0, \
        "Binoculars not connected from SPACE"

    # 3. Connected to EYE
    eye_node = eq.connection_garph.vs.find(name=GraphConstants.EYE_ID)
    assert eq.connection_garph.get_eid(bino_vertex_index, eye_node.index, directed=True, error=False) >= 0, \
        "Binoculars not connected to EYE"

    # 4. Ensure no input/output connection points were created for binoculars
    bino_internal_id = bino.id() # The ID of the equipment itself
    for v_node in eq.connection_garph.vs:
        node_name = v_node[NodeLabels.NAME] # Use NodeLabels directly
        if node_name.startswith(bino_internal_id + "_") and \
           (node_name.endswith("_IN") or node_name.endswith("_OUT")):
            pytest.fail(f"Binoculars created an unexpected connection node: {node_name}")


def test_binoculars_in_equipment_data():
    eq = Equipment() # Use Equipment class
    bino = Binoculars(
        magnification=8,
        objective_diameter=42,
        vendor="TestBino8x42",
        apparent_fov_deg=60
    )
    eq.register(bino)

    data_df = eq.data()

    assert len(data_df) == 1, f"Expected 1 optical path for binoculars, got {len(data_df)}"

    bino_row = data_df.iloc[0]

    assert bino_row[EquipmentTableLabels.LABEL] == "TestBino8x42 8x42"
    assert bino_row[EquipmentTableLabels.TYPE] == "Visual"
    assert bino_row[EquipmentTableLabels.ZOOM] == pytest.approx(8)
    assert bino_row[EquipmentTableLabels.USEFUL_ZOOM] == True
    assert bino_row[EquipmentTableLabels.FOV] == pytest.approx(60 / 8) # 7.5

    expected_exit_pupil = 42.0 / 8.0  # 5.25
    assert bino_row[EquipmentTableLabels.EXIT_PUPIL] == pytest.approx(expected_exit_pupil)

    expected_dawes = round(11.6 / 4.2, 3) # Dawes: 11.6 / 4.2cm, rounded to 3 decimal places
    assert bino_row[EquipmentTableLabels.DAWES_LIMIT] == pytest.approx(expected_dawes)

    expected_range = 7.7 + 5 * np.log10(4.2) # Range: 7.7 + 5 * log10(4.2cm)
    assert bino_row[EquipmentTableLabels.RANGE] == pytest.approx(expected_range)

    expected_brightness = (expected_exit_pupil / 7.0)**2 * 100 # Brightness: (5.25mm / 7mm)^2 * 100
    assert bino_row[EquipmentTableLabels.BRIGHTNESS] == pytest.approx(expected_brightness)

    assert bino_row[EquipmentTableLabels.ELEMENTS] == 1

def test_binoculars_do_not_connect_with_telescope_equipment():
    eq = setup_equipment()

    bino = Binoculars(magnification=10, objective_diameter=50, vendor="TestBino", apparent_fov_deg=65)
    eq.register(bino)

    data_df = eq.data()

    found_bino_only_path = False
    found_tele_eyepiece_path = False

    # These checks assume setup_equipment() creates a telescope "SkyWatcher" and an eyepiece "Plossl"
    # and that these result in one or more paths.
    # If setup_equipment() changes, these string checks might need adjustment.
    for index, row in data_df.iterrows():
        label = row[EquipmentTableLabels.LABEL]
        elements = row[EquipmentTableLabels.ELEMENTS]

        if "TestBino" in label:
            assert elements == 1, f"Binocular path '{label}' should have 1 element, got {elements}"
            assert "unknown telescope 150/750" not in label, "Binocular path should not include Telescope parts"
            assert "unknown ocular f=25" not in label, "Binocular path should not include Eyepiece parts"
            found_bino_only_path = True
        elif "unknown telescope 150/750" in label and "unknown ocular f=25" in label:
            # Assuming a telescope path will have more than 1 element (telescope + eyepiece/camera)
            assert elements > 1, f"Telescope path '{label}' should have more than 1 element, got {elements}"
            assert "TestBino" not in label, "Telescope path should not include Binocular parts"
            found_tele_eyepiece_path = True

    assert found_bino_only_path, "Did not find a dedicated optical path for binoculars"
    assert found_tele_eyepiece_path, "Did not find the original telescope path from setup_equipment"

    bino_paths_count = sum(["TestBino" in label for label in data_df[EquipmentTableLabels.LABEL]])
    assert bino_paths_count == 1, "Expected exactly one path containing the TestBino"


# --- T2 Adapter Tests ---

def test_telescope_to_camera_direct_t2():
    """Test Telescope directly connected to Camera via T2."""
    eq = Equipment() # Use Equipment class
    # OpticalType and GraphConstants are imported at the top
    # from apts.opticalequipment import Telescope, Camera # Already imported

    # Telescope with T2 output
    # Parameters: aperture, focal_length, vendor="unknown telescope", t2_output=False
    tele = Telescope(150, 750, t2_output=True, vendor="TestScopeT2")
    # Camera defaults to T2 connection
    # Parameters: chip_w, chip_h, pixel_w, pixel_h, vendor="unknown camera"
    cam = Camera(22.2, 14.8, 4.3, 4.3, vendor="TestCamT2")

    eq.register(tele)
    eq.register(cam)

    data_df = eq.data()

    # Filter for paths that result in an "Image" type output
    image_paths = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

    assert not image_paths.empty, "No image paths found for Telescope direct to Camera (T2)"

    # Assuming one primary path for this simple setup
    # If multiple, this might need adjustment or looping through paths
    path_info = image_paths.iloc[0]

    assert path_info[EquipmentTableLabels.ELEMENTS] == 2, \
        f"Expected 2 elements, got {path_info[EquipmentTableLabels.ELEMENTS]}"

    # Verify label contains both component names (vendors)
    assert tele.vendor in path_info[EquipmentTableLabels.LABEL]
    assert cam.vendor in path_info[EquipmentTableLabels.LABEL]
    # Optional: Check zoom/FOV if a simple formula exists for direct T2 projection
    # For prime focus, zoom is often considered focal_length_tele / diagonal_sensor_size_mm
    # This might require more detailed calculation based on how OpticalPath calculates it.

    # --- Detailed OpticalPath verification ---
    all_image_ops = eq._get_paths(GraphConstants.IMAGE_ID)
    target_op = None
    for op in all_image_ops:
        if (tele.vendor in op.label() and
            cam.vendor in op.label() and
            op.length() == 2):
            target_op = op
            break

    assert target_op is not None, "Could not find the specific Telescope->Camera OpticalPath"

    # Verify components
    assert target_op.telescope == tele
    assert target_op.output == cam
    assert not target_op.barlows # No barlows in this path

    # Verify calculations
    # op.zoom() internally calls: OpticsUtils.compute_camera_zoom(self.telescope, self.output, self.barlow_magnification())
    # OpticsUtils.compute_camera_zoom: return telescope.focal_length / camera._zoom_divider() * barlow_magnification

    # Use target_op.output (which is the camera instance 'cam') for camera-specific attributes
    expected_zoom = tele.focal_length.magnitude / target_op.output._zoom_divider().magnitude
    assert target_op.zoom().magnitude == pytest.approx(expected_zoom)

    # op.fov() calls camera.field_of_view(self.telescope, self.zoom(), self.barlow_magnification())
    # The zoom argument to camera.field_of_view is not used in its formula.
    expected_fov = (target_op.output.sensor_height.magnitude * 3438 /
                    (tele.focal_length.magnitude * 1.0)) / 60 # Barlow mag is 1.0 for this path
    assert target_op.fov().magnitude == pytest.approx(expected_fov)


def test_telescope_barlow_t2_camera():
    """Test Telescope to Barlow (T2 output) to Camera."""
    eq = Equipment() # Use Equipment class
    # OpticalType, GraphConstants, ConnectionType are imported at the top
    # from apts.opticalequipment import Telescope, Barlow, Camera # Already imported

    # Telescope with standard 1.25" output
    tele = Telescope(150, 750, vendor="MainScope")
    # Barlow with 1.25" input, but T2 output
    barlow_t2 = Barlow(magnification=2.0,
                       connection_type=ConnectionType.F_1_25,
                       t2_output=True,
                       vendor="BarlowT2Out")
    # Camera defaults to T2 connection
    cam = Camera(12.48, 9.98, 2.4, 2.4, vendor="MicroCam")

    eq.register(tele)
    eq.register(barlow_t2)
    eq.register(cam)

    data_df = eq.data()
    image_paths = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

    assert not image_paths.empty, "No image paths found for Telescope -> Barlow (T2) -> Camera"

    path_info = image_paths.iloc[0]

    assert path_info[EquipmentTableLabels.ELEMENTS] == 3, \
        f"Expected 3 elements, got {path_info[EquipmentTableLabels.ELEMENTS]}"

    assert tele.vendor in path_info[EquipmentTableLabels.LABEL]
    assert barlow_t2.vendor in path_info[EquipmentTableLabels.LABEL]
    assert cam.vendor in path_info[EquipmentTableLabels.LABEL]
    # Optional: Check zoom/FOV. Zoom should reflect Barlow's magnification.
    # e.g., if direct camera zoom was X, with 2x Barlow it should be 2X.

    # --- Detailed OpticalPath verification ---
    all_image_ops = eq._get_paths(GraphConstants.IMAGE_ID)
    target_op = None
    for op in all_image_ops:
        if (tele.vendor in op.label() and
            barlow_t2.vendor in op.label() and
            cam.vendor in op.label() and
            op.length() == 3):
            target_op = op
            break

    assert target_op is not None, "Could not find the specific Telescope->Barlow->Camera OpticalPath"

    # Verify components
    assert target_op.telescope == tele
    assert target_op.output == cam
    assert len(target_op.barlows) == 1
    assert target_op.barlows[0] == barlow_t2
    assert target_op.effective_barlow() == pytest.approx(barlow_t2.magnification)

    # Verify calculations
    expected_zoom = (tele.focal_length.magnitude / target_op.output._zoom_divider().magnitude) * barlow_t2.magnification
    assert target_op.zoom().magnitude == pytest.approx(expected_zoom)

    expected_fov = (target_op.output.sensor_height.magnitude * 3438 /
                    (tele.focal_length.magnitude * barlow_t2.magnification)) / 60
    assert target_op.fov().magnitude == pytest.approx(expected_fov)


def test_telescope_std_barlow_t2_camera_variation():
    """Confirms Telescope (standard) -> Barlow (standard_in, T2_out) -> Camera connection."""
    eq = Equipment() # Use Equipment class
    # OpticalType, GraphConstants, ConnectionType are imported at the top
    # from apts.opticalequipment import Telescope, Barlow, Camera # Already imported

    tele = Telescope(100, 500, vendor="ScopeStdOut") # Default F_1_25 output
    barlow = Barlow(magnification=1.5,
                    connection_type=ConnectionType.F_1_25, # Standard input
                    t2_output=True,
                    vendor="BarlowT2Var")
    cam = Camera(10, 10, 5, 5, vendor="CamT2Var") # T2 input

    eq.register(tele)
    eq.register(barlow)
    eq.register(cam)

    data_df = eq.data()
    image_paths = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

    assert not image_paths.empty, "No image paths found for Telescope (std) -> Barlow (T2 out) -> Camera"

    # Find the specific path
    correct_path_found = False
    for _, row in image_paths.iterrows():
        if (tele.vendor in row[EquipmentTableLabels.LABEL] and
            barlow.vendor in row[EquipmentTableLabels.LABEL] and
            cam.vendor in row[EquipmentTableLabels.LABEL] and
            row[EquipmentTableLabels.ELEMENTS] == 3):
            correct_path_found = True
            break
    assert correct_path_found, "Specific Telescope (std) -> Barlow (T2 out) -> Camera path not found or element count incorrect"

    # --- Detailed OpticalPath verification ---
    all_image_ops = eq._get_paths(GraphConstants.IMAGE_ID)
    target_op = None
    for op_path in all_image_ops: # Renamed op to op_path to avoid conflict with outer scope if any
        # Check label and number of elements to identify the correct path
        if (tele.vendor in op_path.label() and
            barlow.vendor in op_path.label() and
            cam.vendor in op_path.label() and
            op_path.length() == 3):
            target_op = op_path
            break

    assert target_op is not None, "Could not find the specific Telescope->Barlow->Camera OpticalPath for detailed check"

    # Verify components
    assert target_op.telescope == tele
    assert target_op.output == cam
    assert len(target_op.barlows) == 1
    assert target_op.barlows[0] == barlow
    assert target_op.effective_barlow() == pytest.approx(barlow.magnification)

    # Verify calculations
    expected_zoom = (tele.focal_length.magnitude / target_op.output._zoom_divider().magnitude) * barlow.magnification
    assert target_op.zoom().magnitude == pytest.approx(expected_zoom)

    expected_fov = (target_op.output.sensor_height.magnitude * 3438 /
                    (tele.focal_length.magnitude * barlow.magnification)) / 60
    assert target_op.fov().magnitude == pytest.approx(expected_fov)


def test_connection_specificity_tele_no_t2_output_to_t2_camera():
    """Test Telescope (no T2 out) does not connect to Camera (only T2 in)."""
    eq = Equipment() # Use Equipment class
    # OpticalType, GraphConstants, ConnectionType are imported at the top
    # from apts.opticalequipment import Telescope, Camera # Already imported

    # Telescope with F_1_25 output, t2_output=False by default
    tele_no_t2 = Telescope(80, 400, vendor="TeleNoT2", connection_type=ConnectionType.F_1_25)
    # Camera with only T2 input (default)
    cam_t2_only = Camera(10, 10, 5, 5, vendor="CamOnlyT2")

    eq.register(tele_no_t2)
    eq.register(cam_t2_only)

    data_df = eq.data()
    image_paths = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

    # We expect NO paths that are just these two items.
    # If any image path exists, it must not be a direct connection of these two.
    direct_connection_found = False
    for _, row in image_paths.iterrows():
        if (tele_no_t2.vendor in row[EquipmentTableLabels.LABEL] and
            cam_t2_only.vendor in row[EquipmentTableLabels.LABEL] and
            row[EquipmentTableLabels.ELEMENTS] == 2):
            direct_connection_found = True
            break
    assert not direct_connection_found, \
        f"Unexpected direct path found between Telescope (no T2 out) and Camera (T2 in): {row[EquipmentTableLabels.LABEL] if direct_connection_found else ''}"


def test_connection_specificity_barlow_no_t2_output_to_t2_camera():
    """Test Barlow (no T2 out) does not connect to Camera (only T2 in) in a sequence."""
    eq = Equipment() # Use Equipment class
    # OpticalType, GraphConstants, ConnectionType are imported at the top
    # from apts.opticalequipment import Telescope, Barlow, Camera # Already imported

    tele = Telescope(100, 500, vendor="SeqScope") # Standard F_1_25 output
    # Barlow with F_1_25 input, but t2_output explicitly False
    barlow_no_t2 = Barlow(magnification=2.0,
                          connection_type=ConnectionType.F_1_25,
                          t2_output=False,
                          vendor="BarlowNoT2")
    cam_t2_only = Camera(10, 10, 5, 5, vendor="SeqCamT2") # T2 input

    eq.register(tele)
    eq.register(barlow_no_t2)
    eq.register(cam_t2_only)

    data_df = eq.data()
    image_paths = data_df[data_df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]

    problematic_path_found = False
    for _, row in image_paths.iterrows():
        is_problem_path = (
            tele.vendor in row[EquipmentTableLabels.LABEL] and
            barlow_no_t2.vendor in row[EquipmentTableLabels.LABEL] and
            cam_t2_only.vendor in row[EquipmentTableLabels.LABEL] and
            row[EquipmentTableLabels.ELEMENTS] == 3 # Path with all three
        )
        if is_problem_path:
            # This path should not form if Barlow cannot output to T2 for the camera
            problematic_path_found = True
            break

    assert not problematic_path_found, \
        f"Path formed with Barlow (no T2 out) to Camera (T2 in): {row[EquipmentTableLabels.LABEL] if problematic_path_found else ''}"


# --- Brightness Tests ---

def test_camera_path_brightness_is_nan():
    """Test that brightness for a camera path is NaN."""
    eq = Equipment() # Use Equipment class
    # Telescope with T2 output
    scope_t2 = Telescope(aperture=80, focal_length=400, vendor="TestScopeT2", t2_output=True)
    # Camera with T2 input (default)
    cam = Camera(sensor_width=22.2, sensor_height=14.8, width=5184, height=3456, vendor="TestCamT2")

    eq.register(scope_t2)
    eq.register(cam)

    df = eq.data()
    assert not df.empty, "Equipment data frame is empty"

    camera_rows = df[df[EquipmentTableLabels.TYPE] == GraphConstants.IMAGE_ID]
    assert not camera_rows.empty, "No camera output paths found in DataFrame."

    # Check if all brightness values in camera_rows are NaN
    assert camera_rows[EquipmentTableLabels.BRIGHTNESS].isnull().all(), \
        f"Brightness for camera paths should be NaN. Got: {camera_rows[EquipmentTableLabels.BRIGHTNESS].values}"

def test_eyepiece_path_brightness_is_numeric():
    """Test that brightness for an eyepiece path is numeric and non-negative."""
    eq = Equipment() # Use Equipment class
    # Telescope with default F_1_25 output
    scope = Telescope(aperture=80, focal_length=400, vendor="TestScopeVisual")
    # Eyepiece with F_1_25 input
    ep = Eyepiece(focal_length=10, vendor="TestEPVisual", field_of_view=50, connection_type=ConnectionType.F_1_25)

    eq.register(scope)
    eq.register(ep)

    df = eq.data()
    assert not df.empty, "Equipment data frame is empty"

    eyepiece_rows = df[df[EquipmentTableLabels.TYPE] == GraphConstants.EYE_ID]
    assert not eyepiece_rows.empty, "No eyepiece output paths found in DataFrame."

    # Check that all brightness values are not NaN (i.e., they are numbers)
    assert eyepiece_rows[EquipmentTableLabels.BRIGHTNESS].notnull().all(), \
        f"Brightness for eyepiece paths should be a number. Got: {eyepiece_rows[EquipmentTableLabels.BRIGHTNESS].values}"

    # Check that all brightness values are non-negative
    assert (eyepiece_rows[EquipmentTableLabels.BRIGHTNESS] >= 0).all(), \
        f"Brightness for eyepiece paths should be non-negative. Got: {eyepiece_rows[EquipmentTableLabels.BRIGHTNESS].values}"

# --- Plotting Tests ---

def _create_custom_equipment_for_plotting():
    eq = Equipment() # Starts with SPACE, EYE, IMAGE nodes (OpticalType.GENERIC)

    # Telescope registers its main node as OpticalType.OPTICAL
    # and connection points as OpticalType.INPUT / OpticalType.OUTPUT
    tele = Telescope(focal_length=750, aperture=150, vendor="TestPlotTele")
    eq.register(tele)

    # Eyepiece registers its main node as OpticalType.OPTICAL
    # and connection points as OpticalType.INPUT / OpticalType.OUTPUT
    ep = Eyepiece(focal_length=25, field_of_view=50, vendor="TestPlotEP")
    eq.register(ep)

    return eq

@patch('apts.equipment.get_dark_mode')
@patch('apts.equipment.ig.plot') # Mock the ig.plot call itself
def test_plot_connection_graph_override_dark(mock_ig_plot, mock_get_global_dark_mode):
    mock_get_global_dark_mode.return_value = False # Global is light
    eq = _create_custom_equipment_for_plotting()

    expected_style = GraphConstants.DARK_MODE_STYLE
    expected_colors_map = GraphConstants.DARK_COLORS
    # Default color for vertices if their type is not in expected_colors_map
    # This should match the default used in equipment.py's plot_connection_graph
    default_vertex_color_if_unmapped = '#FF00FF' # Magenta

    eq.plot_connection_graph(dark_mode_override=True) # Override to dark

    mock_ig_plot.assert_called_once()
    args, kwargs = mock_ig_plot.call_args

    assert kwargs.get('background') == expected_style['BACKGROUND_COLOR']
    assert kwargs.get('edge_color') == expected_style['AXIS_COLOR']

    plotted_graph = args[0] # The first positional argument to ig.plot is the graph
    all_vertex_types = plotted_graph.vs[NodeLabels.TYPE]
    all_actual_colors = plotted_graph.vs['color']
    all_actual_label_colors = plotted_graph.vs['label_color']

    assert len(all_vertex_types) == len(all_actual_colors), "Mismatch in vertex type and color list lengths"
    assert len(all_vertex_types) == len(all_actual_label_colors), "Mismatch in vertex type and label color list lengths"

    for i, v_type in enumerate(all_vertex_types):
        expected_v_color = expected_colors_map.get(v_type, default_vertex_color_if_unmapped)
        assert all_actual_colors[i] == expected_v_color, f"Vertex {i} (type {v_type}) color mismatch. Expected {expected_v_color}, got {all_actual_colors[i]}"
        assert all_actual_label_colors[i] == expected_style['TEXT_COLOR'], f"Vertex {i} (type {v_type}) label color mismatch. Expected {expected_style['TEXT_COLOR']}, got {all_actual_label_colors[i]}"
        assert plotted_graph.vs[i]['size'] == 20, f"Vertex {i} size mismatch"
        assert plotted_graph.vs[i]['label_dist'] == 1.5, f"Vertex {i} label_dist mismatch"

@patch('apts.equipment.get_dark_mode')
@patch('apts.equipment.ig.plot')
def test_plot_connection_graph_override_light(mock_ig_plot, mock_get_global_dark_mode):
    mock_get_global_dark_mode.return_value = True # Global is dark
    eq = _create_custom_equipment_for_plotting()

    expected_style = GraphConstants.LIGHT_MODE_STYLE
    expected_colors_map = GraphConstants.COLORS # Standard colors for light mode
    default_vertex_color_if_unmapped = '#FF00FF'

    eq.plot_connection_graph(dark_mode_override=False) # Override to light

    mock_ig_plot.assert_called_once()
    args, kwargs = mock_ig_plot.call_args

    assert kwargs.get('background') == expected_style['BACKGROUND_COLOR']
    assert kwargs.get('edge_color') == expected_style['AXIS_COLOR']

    plotted_graph = args[0]
    all_vertex_types = plotted_graph.vs[NodeLabels.TYPE]
    all_actual_colors = plotted_graph.vs['color']
    all_actual_label_colors = plotted_graph.vs['label_color']

    for i, v_type in enumerate(all_vertex_types):
        expected_v_color = expected_colors_map.get(v_type, default_vertex_color_if_unmapped)
        assert all_actual_colors[i] == expected_v_color, f"Vertex {i} (type {v_type}) color mismatch. Expected {expected_v_color}, got {all_actual_colors[i]}"
        assert all_actual_label_colors[i] == expected_style['TEXT_COLOR'], f"Vertex {i} (type {v_type}) label color mismatch. Expected {expected_style['TEXT_COLOR']}, got {all_actual_label_colors[i]}"
        assert plotted_graph.vs[i]['size'] == 20
        assert plotted_graph.vs[i]['label_dist'] == 1.5

@patch('apts.equipment.get_dark_mode')
@patch('apts.equipment.ig.plot')
def test_plot_connection_graph_global_dark(mock_ig_plot, mock_get_global_dark_mode):
    mock_get_global_dark_mode.return_value = True # Global is dark
    eq = _create_custom_equipment_for_plotting()

    expected_style = GraphConstants.DARK_MODE_STYLE
    expected_colors_map = GraphConstants.DARK_COLORS
    default_vertex_color_if_unmapped = '#FF00FF'

    eq.plot_connection_graph(dark_mode_override=None) # No override, use global

    mock_ig_plot.assert_called_once()
    args, kwargs = mock_ig_plot.call_args

    assert kwargs.get('background') == expected_style['BACKGROUND_COLOR']
    assert kwargs.get('edge_color') == expected_style['AXIS_COLOR']

    plotted_graph = args[0]
    all_vertex_types = plotted_graph.vs[NodeLabels.TYPE]
    all_actual_colors = plotted_graph.vs['color']
    all_actual_label_colors = plotted_graph.vs['label_color']

    for i, v_type in enumerate(all_vertex_types):
        expected_v_color = expected_colors_map.get(v_type, default_vertex_color_if_unmapped)
        assert all_actual_colors[i] == expected_v_color, f"Vertex {i} (type {v_type}) color mismatch. Expected {expected_v_color}, got {all_actual_colors[i]}"
        assert all_actual_label_colors[i] == expected_style['TEXT_COLOR'], f"Vertex {i} (type {v_type}) label color mismatch. Expected {expected_style['TEXT_COLOR']}, got {all_actual_label_colors[i]}"
        assert plotted_graph.vs[i]['size'] == 20
        assert plotted_graph.vs[i]['label_dist'] == 1.5

@patch('apts.equipment.get_dark_mode')
@patch('apts.equipment.ig.plot')
def test_plot_connection_graph_global_light(mock_ig_plot, mock_get_global_dark_mode):
    mock_get_global_dark_mode.return_value = False # Global is light
    eq = _create_custom_equipment_for_plotting()

    expected_style = GraphConstants.LIGHT_MODE_STYLE
    expected_colors_map = GraphConstants.COLORS
    default_vertex_color_if_unmapped = '#FF00FF'

    eq.plot_connection_graph(dark_mode_override=None) # No override, use global

    mock_ig_plot.assert_called_once()
    args, kwargs = mock_ig_plot.call_args

    assert kwargs.get('background') == expected_style['BACKGROUND_COLOR']
    assert kwargs.get('edge_color') == expected_style['AXIS_COLOR']

    plotted_graph = args[0]
    all_vertex_types = plotted_graph.vs[NodeLabels.TYPE]
    all_actual_colors = plotted_graph.vs['color']
    all_actual_label_colors = plotted_graph.vs['label_color']

    for i, v_type in enumerate(all_vertex_types):
        expected_v_color = expected_colors_map.get(v_type, default_vertex_color_if_unmapped)
        assert all_actual_colors[i] == expected_v_color, f"Vertex {i} (type {v_type}) color mismatch. Expected {expected_v_color}, got {all_actual_colors[i]}"
        assert all_actual_label_colors[i] == expected_style['TEXT_COLOR'], f"Vertex {i} (type {v_type}) label color mismatch. Expected {expected_style['TEXT_COLOR']}, got {all_actual_label_colors[i]}"
        assert plotted_graph.vs[i]['size'] == 20
        assert plotted_graph.vs[i]['label_dist'] == 1.5

# --- SVG Plotting Tests ---

@unittest.skip("Skipping test because cairo is not available in the CI environment")
@patch('apts.equipment.ca.ImageSurface') # Mock cairo.ImageSurface
@patch.object(Equipment, 'plot_connection_graph') # Mock the internal call
def test_plot_connection_graph_svg_override_dark(mock_plot_connection_graph, mock_cairo_surface):
    eq = Equipment()
    mock_plot_instance = MagicMock()
    mock_plot_instance._repr_svg_.return_value = ("<svg_output_string>",)
    mock_plot_connection_graph.return_value = mock_plot_instance

    eq.plot_connection_graph_svg(dark_mode_override=True)

    mock_cairo_surface.assert_called_once_with(ANY, 800, 600)
    mock_plot_connection_graph.assert_called_once()
    called_kwargs = mock_plot_connection_graph.call_args.kwargs
    assert called_kwargs.get('dark_mode_override') is True
    assert 'target' in called_kwargs
    assert called_kwargs['target'] == mock_cairo_surface.return_value

@unittest.skip("Skipping test because cairo is not available in the CI environment")
@patch('apts.equipment.ca.ImageSurface')
@patch.object(Equipment, 'plot_connection_graph')
def test_plot_connection_graph_svg_override_light(mock_plot_connection_graph, mock_cairo_surface):
    eq = Equipment()
    mock_plot_instance = MagicMock()
    mock_plot_instance._repr_svg_.return_value = ("<svg_output_string>",)
    mock_plot_connection_graph.return_value = mock_plot_instance

    eq.plot_connection_graph_svg(dark_mode_override=False)

    mock_cairo_surface.assert_called_once_with(ANY, 800, 600)
    mock_plot_connection_graph.assert_called_once()
    called_kwargs = mock_plot_connection_graph.call_args.kwargs
    assert called_kwargs.get('dark_mode_override') is False
    assert 'target' in called_kwargs
    assert called_kwargs['target'] == mock_cairo_surface.return_value

@unittest.skip("Skipping test because cairo is not available in the CI environment")
@patch('apts.equipment.ca.ImageSurface')
@patch.object(Equipment, 'plot_connection_graph')
def test_plot_connection_graph_svg_override_none(mock_plot_connection_graph, mock_cairo_surface):
    eq = Equipment()
    mock_plot_instance = MagicMock()
    mock_plot_instance._repr_svg_.return_value = ("<svg_output_string>",)
    mock_plot_connection_graph.return_value = mock_plot_instance

    eq.plot_connection_graph_svg(dark_mode_override=None)

    mock_cairo_surface.assert_called_once_with(ANY, 800, 600)
    mock_plot_connection_graph.assert_called_once()
    called_kwargs = mock_plot_connection_graph.call_args.kwargs
    assert called_kwargs.get('dark_mode_override') is None
    assert 'target' in called_kwargs
    assert called_kwargs['target'] == mock_cairo_surface.return_value

@unittest.skip("Skipping test because cairo is not available in the CI environment")
@patch('apts.equipment.ca.ImageSurface')
@patch.object(Equipment, 'plot_connection_graph')
def test_plot_connection_graph_svg_no_override(mock_plot_connection_graph, mock_cairo_surface):
    eq = Equipment()
    mock_plot_instance = MagicMock()
    mock_plot_instance._repr_svg_.return_value = ("<svg_output_string>",)
    mock_plot_connection_graph.return_value = mock_plot_instance

    eq.plot_connection_graph_svg() # Call without dark_mode_override

    mock_cairo_surface.assert_called_once_with(ANY, 800, 600)
    mock_plot_connection_graph.assert_called_once()
    called_kwargs = mock_plot_connection_graph.call_args.kwargs
    assert called_kwargs.get('dark_mode_override') is None
    assert 'target' in called_kwargs
    assert called_kwargs['target'] == mock_cairo_surface.return_value
