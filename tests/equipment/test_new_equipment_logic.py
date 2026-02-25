import pytest
from apts.equipment import Equipment
from apts.opticalequipment.telescope import Telescope
from apts.opticalequipment.camera import Camera
from apts.opticalequipment.filter import Filter
from apts.opticalequipment.filter_wheel import FilterWheel
from apts.opticalequipment.oag import OAG
from apts.opticalequipment.focuser import Focuser
from apts.opticalequipment.rotator import Rotator
from apts.opticalequipment.adapter import Adapter, Spacer
from apts.opticalequipment.anti_tilt import AntiTilt
from apts.opticalequipment.flip_mirror import FlipMirror
from apts.utils import ConnectionType, Gender
from apts.optics import OpticalPath

def test_attached_equipment_mass():
    t = Telescope(80, 480, vendor="Refractor", mass=3000)
    f = Focuser("EAF", mass=500)
    t.attach(f)

    # Generic camera for mass testing
    c = Camera(10, 10, 1000, 1000, vendor="Cam", mass=500)

    path = OpticalPath.from_path([t, c])

    # Total mass should include t, f, and c
    total_mass = path.total_mass().to("gram").magnitude
    assert total_mass == 3000 + 500 + 500

def test_filter_wheel_paths():
    e = Equipment()
    # Use T2 consistently for connections
    t = Telescope(80, 480, vendor="Refractor", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)

    fw = FilterWheel("EFW", in_connection_type=ConnectionType.T2, out_connection_type=ConnectionType.T2, in_gender=Gender.FEMALE, out_gender=Gender.MALE)
    f1 = Filter("Red", connection_type=ConnectionType.T2)
    f2 = Filter("Green", connection_type=ConnectionType.T2)
    fw.add_filter(f1)
    fw.add_filter(f2)

    c = Camera(10, 10, 1000, 1000, vendor="Cam", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)

    e.register(t)
    e.register(fw)
    e.register(c)

    # Find paths to image
    paths = e._get_paths("Image")

    # Filter wheel paths now include parallel filter paths.
    # Actually, fw_Node also connects to fw_M42_out directly.
    # So we might have 3 paths: Red, Green, and None?
    # Let's see.
    assert len(paths) >= 2

    labels = [p.label() for p in paths]
    assert any("Red" in l for l in labels)
    assert any("Green" in l for l in labels)

def test_oag_paths():
    e = Equipment()
    t = Telescope(80, 480, vendor="Refractor", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)

    oag = OAG("ZWO OAG", in_connection_type=ConnectionType.T2, out_connection_type=ConnectionType.T2, in_gender=Gender.FEMALE, out_gender=Gender.MALE, guide_connection_type=ConnectionType.T2, guide_gender=Gender.MALE)

    main_cam = Camera(10, 10, 1000, 1000, vendor="Main Cam", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)
    guide_cam = Camera(5, 5, 500, 500, vendor="Guide Cam", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)

    e.register(t)
    e.register(oag)
    e.register(main_cam)
    e.register(guide_cam)

    # Paths to image
    paths = e._get_paths("Image")

    # We expect 4 paths, because each camera can connect to either output of the OAG
    # since both outputs and both inputs use T2 connection.
    assert len(paths) == 4

    labels = [p.label() for p in paths]
    assert any("Main Cam" in l for l in labels)
    assert any("Guide Cam" in l for l in labels)

def test_flip_mirror_paths():
    e = Equipment()
    # Use unique connection types to enforce the path: t -> fm -> (cam OR eye)
    # Telescope to FlipMirror input: M48
    t = Telescope(80, 480, vendor="Refractor", connection_type=ConnectionType.M48, connection_gender=Gender.MALE)

    # FlipMirror: IN=M48, OUT1=T2, OUT2=1.25
    fm = FlipMirror("Baader FlipMirror",
                    in_connection_type=ConnectionType.M48, in_gender=Gender.FEMALE,
                    out_connection_type=ConnectionType.T2, out_gender=Gender.MALE,
                    diagonal_connection_type=ConnectionType.F_1_25, diagonal_gender=Gender.FEMALE)

    # Camera: T2
    cam = Camera(10, 10, 1000, 1000, vendor="Cam", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)

    # Eyepiece: 1.25
    from apts.opticalequipment.eyepiece import Eyepiece
    eye = Eyepiece(20, vendor="Plossl", field_of_view=50, connection_type=ConnectionType.F_1_25, connection_gender=Gender.MALE)

    e.register(t)
    e.register(fm)
    e.register(cam)
    e.register(eye)

    # Path to Image
    image_paths = e._get_paths("Image")
    print(f"Image paths: {[p.label() for p in image_paths]}")
    assert len(image_paths) == 1
    assert "Cam" in image_paths[0].label()

    # Path to Eye
    visual_paths = e._get_paths("Visual")
    # One path is through flip mirror, the other is Naked Eye (registered by default in Equipment)
    assert len(visual_paths) == 2
    assert any("Plossl" in p.label() for p in visual_paths)
    assert any("Naked Eye" in p.label() for p in visual_paths)

def test_optical_path_expand_all_types():
    t = Telescope(80, 480)
    rot = Rotator("Rotator")
    foc = Focuser("Focuser")
    adapt = Adapter("Adapter")
    spc = Spacer("Spacer")
    at = AntiTilt("AntiTilt")
    c = Camera(10, 10, 1000, 1000)

    path = [t, rot, foc, adapt, spc, at, c]
    from apts.optics import OpticsUtils
    (telescope, barlows, diagonals, filters, others, output) = OpticsUtils.expand(path)

    assert telescope == t
    assert output == c
    assert rot in others
    assert foc in others
    assert adapt in others
    assert spc in others
    assert at in others
    assert len(others) == 5

def test_nested_attachments():
    t = Telescope(80, 480, mass=1000)
    f = Focuser("Focuser", mass=200)
    r = Rotator("Rotator", mass=100)

    t.attach(f)
    f.attach(r)

    c = Camera(10, 10, 1000, 1000, mass=300)

    path = OpticalPath.from_path([t, c])
    # total mass should be 1000 + 200 + 100 + 300 = 1600
    assert path.total_mass().to("gram").magnitude == 1600

def test_supporting_equipment_in_path():
    e = Equipment()
    t = Telescope(80, 480, vendor="Refractor", connection_type=ConnectionType.M48, connection_gender=Gender.MALE)

    # Use unique connection M68 between Rotator and Focuser to force the order
    rot = Rotator("Falcon", in_connection_type=ConnectionType.M48, in_gender=Gender.FEMALE, out_connection_type=ConnectionType.M68, out_gender=Gender.MALE)
    foc = Focuser("ESATTO", in_connection_type=ConnectionType.M68, in_gender=Gender.FEMALE, out_connection_type=ConnectionType.M42, out_gender=Gender.MALE)

    cam = Camera(10, 10, 1000, 1000, vendor="Cam", connection_type=ConnectionType.M42, connection_gender=Gender.FEMALE)

    e.register(t)
    e.register(rot)
    e.register(foc)
    e.register(cam)

    paths = e._get_paths("Image")
    assert len(paths) == 1
    label = paths[0].label()
    assert "Falcon" in label
    assert "ESATTO" in label
    assert "Cam" in label

def test_spacer_adapter_anti_tilt():
    e = Equipment()
    t = Telescope(80, 480, connection_type=ConnectionType.M54, connection_gender=Gender.MALE)

    # Use chain of unique connections: M54 -> M56 -> M63 -> M48 -> M42
    at = AntiTilt("TiltPlate", in_connection_type=ConnectionType.M54, in_gender=Gender.FEMALE, out_connection_type=ConnectionType.M56, out_gender=Gender.MALE)
    sp = Spacer("10mm Spacer", in_connection_type=ConnectionType.M56, in_gender=Gender.FEMALE, out_connection_type=ConnectionType.M63, out_gender=Gender.MALE, optical_length=10)
    ad = Adapter("M54 to M42", in_connection_type=ConnectionType.M63, in_gender=Gender.FEMALE, out_connection_type=ConnectionType.M42, out_gender=Gender.MALE)

    cam = Camera(10, 10, 1000, 1000, connection_type=ConnectionType.M42, connection_gender=Gender.FEMALE)

    e.register(t)
    e.register(at)
    e.register(sp)
    e.register(ad)
    e.register(cam)

    paths = e._get_paths("Image")
    assert len(paths) == 1
    path = paths[0]
    assert "TiltPlate" in path.label()
    assert "10mm Spacer" in path.label()
    assert "M54 to M42" in path.label()
