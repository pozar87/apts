import pytest
import numpy as np # Added for np.log10

from apts import equipment
from apts.constants import EquipmentTableLabels, GraphConstants # Added GraphConstants
from apts.opticalequipment import Barlow, Binoculars # Added Binoculars
from apts.utils import ureg # Added ureg
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
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # Get row with biggest zoom
  row = e.data().sort_values(by=EquipmentTableLabels.ZOOM, ascending=False).iloc[0]
  # With two stacked barlows max zoom should be 180 (30 * 3 * 2)
  assert row[EquipmentTableLabels.ZOOM] == 180
  # Using 4 elements
  assert row[EquipmentTableLabels.ELEMENTS] == 4


def test_multi_barlow():
  e = setup_equipment()
  e.register(equipment.Barlow(2))
  e.register(equipment.Barlow(3))
  # With two barlows and single eyepiece number of possiable connection is 4 (with barlow stacking)
  assert len(e.data()[EquipmentTableLabels.ZOOM]) == 4


def test_camera():
  e = setup_equipment()
  e.register(equipment.Camera(30, 40, 100, 200))
  # Zoom of camera (sqrt(30^2 + 40^2) = 50)
  data = e.data()
  assert data[data.Type == "Image"].iloc[0][EquipmentTableLabels.ZOOM] == 15

def test_telecsope():
  t = equipment.Telescope(150, 750)
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
    eq = equipment.Equipment() # Fresh equipment instance
    bino = Binoculars(magnification=10, objective_diameter=50, vendor="TestBino", apparent_fov_deg=65)
    eq.register(bino)

    # Check graph connections
    # 1. Binoculars node exists
    bino_node_id_in_graph = None
    for v in eq.connection_garph.vs:
        if v[equipment.NodeLabels.EQUIPMENT] == bino: # equipment.NodeLabels should work
            bino_node_id_in_graph = v[equipment.NodeLabels.NAME]
            break
    assert bino_node_id_in_graph is not None, "Binoculars node not found in graph"

    # 2. Connected from SPACE
    space_node = eq.connection_garph.vs.find(name=GraphConstants.SPACE_ID)
    bino_vertex_index = eq.connection_garph.vs.find(name=bino_node_id_in_graph).index
    assert eq.connection_garph.are_adjacent(space_node.index, bino_vertex_index), \
        "Binoculars not connected from SPACE"

    # 3. Connected to EYE
    eye_node = eq.connection_garph.vs.find(name=GraphConstants.EYE_ID)
    assert eq.connection_garph.are_adjacent(bino_vertex_index, eye_node.index), \
        "Binoculars not connected to EYE"

    # 4. Ensure no input/output connection points were created for binoculars
    bino_internal_id = bino.id() # The ID of the equipment itself
    for v_node in eq.connection_garph.vs:
        node_name = v_node[equipment.NodeLabels.NAME]
        if node_name.startswith(bino_internal_id + "_") and \
           (node_name.endswith("_IN") or node_name.endswith("_OUT")):
            pytest.fail(f"Binoculars created an unexpected connection node: {node_name}")


def test_binoculars_in_equipment_data():
    eq = equipment.Equipment()
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
