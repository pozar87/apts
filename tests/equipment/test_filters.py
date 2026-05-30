import pytest

from apts.constants import EquipmentTableLabels, GraphConstants, OpticalType
from apts.equipment import Equipment
from apts.opticalequipment import Camera, Filter, FilterWheel, Telescope
from apts.utils import ConnectionType, Gender


def test_filter_registration_and_transmission():
    e = Equipment()
    t = Telescope(150, 750, vendor="TestTele", outputs=[(ConnectionType.T2, Gender.MALE)])
    c = Camera(
        22.2, 14.8, 4, 4, vendor="TestCam", quantum_efficiency=0.5, read_noise=3.0
    )

    # Filter now defaults to FEMALE IN, MALE OUT
    f = Filter(
        "H-alpha",
        transmission=0.9,
        connection_type=ConnectionType.T2,
        vendor="TestFilter",
    )

    e.register(t)
    e.register(f)
    e.register(c)

    image_paths = e._get_paths(GraphConstants.IMAGE_ID)
    path_with_filter = None
    for op in image_paths:
        if any(
            isinstance(filt, Filter) and filt.name == "H-alpha" for filt in op.filters
        ):
            path_with_filter = op
            break

    assert path_with_filter is not None
    assert path_with_filter.filters[0].transmission == 0.9

    # Create another path without filter
    e2 = Equipment()
    e2.register(t)
    e2.register(c)
    path_without_filter = e2._get_paths(GraphConstants.IMAGE_ID)[0]

    flux_with = path_with_filter.object_flux(10.0)
    flux_without = path_without_filter.object_flux(10.0)

    assert flux_with is not None
    assert flux_without is not None
    assert flux_with == pytest.approx(flux_without * 0.9)


def test_filter_wheel_paths():
    e = Equipment()
    t = Telescope(150, 750, vendor="TestTele", outputs=[(ConnectionType.T2, Gender.MALE)])
    # FilterWheel IN (FEMALE), OUT (MALE) for T2
    fw = FilterWheel(
        vendor="TestWheel",
        in_connection=(ConnectionType.T2, Gender.FEMALE), out_connection=(ConnectionType.T2, Gender.MALE),
    )

    f1 = Filter(
        "Red", transmission=0.8, connection_type=ConnectionType.T2, vendor="TestFilter"
    )
    f2 = Filter(
        "Blue", transmission=0.7, connection_type=ConnectionType.T2, vendor="TestFilter"
    )

    fw.add_filter(f1)
    fw.add_filter(f2)

    c = Camera(22.2, 14.8, 4, 4, vendor="TestCam")

    e.register(t)
    e.register(fw)
    e.register(c)

    data = e.data()
    image_paths = data[data[EquipmentTableLabels.TYPE] == OpticalType.IMAGE.name]
    labels = image_paths[EquipmentTableLabels.LABEL].tolist()
    labels = [lb for lb in labels if "TestTele" in lb]

    assert any("Red" in lb for lb in labels)
    assert any("Blue" in lb for lb in labels)
    assert any(
        "Red" not in lb and "Blue" not in lb and "TestWheel" in lb for lb in labels
    )
    assert len(labels) >= 3


def test_filter_component_list_and_mass():
    e = Equipment()
    t = Telescope(150, 750, mass=5000, vendor="TestTele", outputs=[(ConnectionType.T2, Gender.MALE)])
    f = Filter(
        "H-alpha", mass=50, connection_type=ConnectionType.T2, vendor="TestFilter"
    )
    c = Camera(22.2, 14.8, 4, 4, mass=500, vendor="TestCam")

    e.register(t)
    e.register(f)
    e.register(c)

    op = next(p for p in e._get_paths(GraphConstants.IMAGE_ID) if len(p.filters) == 1)

    components = op.component_list()
    assert t in components
    assert f in components
    assert c in components

    assert op.total_mass().magnitude == 5550


def test_filter_wheel_mass():
    e = Equipment()
    t = Telescope(150, 750, mass=5000, vendor="TestTele", outputs=[(ConnectionType.T2, Gender.MALE)])
    fw = FilterWheel(
        vendor="TestWheel",
        mass=300,
        in_connection=(ConnectionType.T2, Gender.FEMALE), out_connection=(ConnectionType.T2, Gender.MALE),
    )

    f1 = Filter("Red", mass=20, connection_type=ConnectionType.T2, vendor="TestFilter")
    fw.add_filter(f1)

    c = Camera(22.2, 14.8, 4, 4, mass=500, vendor="TestCam")

    e.register(t)
    e.register(fw)
    e.register(c)

    image_paths = e._get_paths(GraphConstants.IMAGE_ID)
    path_bypass = next(
        op
        for op in image_paths
        if len(op.filters) == 0
        and any(isinstance(comp, FilterWheel) for comp in op.component_list())
    )

    assert path_bypass.total_mass().magnitude == 5820
