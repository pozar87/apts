from typing import Any, cast
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
    total_mass = cast(Any, path.total_mass()).to("gram").magnitude
    assert total_mass == 3000 + 500 + 500

def test_filter_wheel_paths():
    e = Equipment()
    # Use T2 consistently for connections
    t = Telescope(80, 480, vendor="Refractor", outputs=[(ConnectionType.T2, Gender.MALE)])

    fw = FilterWheel("EFW", in_connection=(ConnectionType.T2, Gender.FEMALE), out_connection=(ConnectionType.T2, Gender.MALE))
    f1 = Filter("Red", connection_type=ConnectionType.T2)
    f2 = Filter("Green", connection_type=ConnectionType.T2)
    fw.add_filter(f1)
    fw.add_filter(f2)

    c = Camera(10, 10, 1000, 1000, vendor="Cam", inputs=[(ConnectionType.T2, Gender.FEMALE)])

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
    assert any("Red" in label for label in labels)
    assert any("Green" in label for label in labels)

def test_oag_paths():
    e = Equipment()
    t = Telescope(80, 480, vendor="Refractor", outputs=[(ConnectionType.T2, Gender.MALE)])

    oag = OAG("ZWO OAG", in_connection=(ConnectionType.T2, Gender.FEMALE), out_connection=(ConnectionType.T2, Gender.MALE), guide_connection=(ConnectionType.T2, Gender.MALE))

    main_cam = Camera(10, 10, 1000, 1000, vendor="Main Cam", inputs=[(ConnectionType.T2, Gender.FEMALE)])
    guide_cam = Camera(5, 5, 500, 500, vendor="Guide Cam", inputs=[(ConnectionType.T2, Gender.FEMALE)])

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
    assert any("Main Cam" in label for label in labels)
    assert any("Guide Cam" in label for label in labels)

def test_flip_mirror_paths():
    e = Equipment()
    # Use unique connection types to enforce the path: t -> fm -> (cam OR eye)
    # Telescope to FlipMirror input: M48
    t = Telescope(80, 480, vendor="Refractor", outputs=[(ConnectionType.M48, Gender.MALE)])

    # FlipMirror: IN=M48, OUT1=T2, OUT2=1.25
    fm = FlipMirror("Baader FlipMirror", in_connection=(ConnectionType.M48, Gender.FEMALE), out_connection=(ConnectionType.T2, Gender.MALE), diagonal_connection=(ConnectionType.F_1_25, Gender.FEMALE))

    # Camera: T2
    cam = Camera(10, 10, 1000, 1000, vendor="Cam", inputs=[(ConnectionType.T2, Gender.FEMALE)])

    # Eyepiece: 1.25
    from apts.opticalequipment.eyepiece import Eyepiece
    eye = Eyepiece(20, vendor="Plossl", field_of_view=50, inputs=[(ConnectionType.F_1_25, Gender.MALE)])

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
    assert cast(Any, path.total_mass()).to("gram").magnitude == 1600

def test_supporting_equipment_in_path():
    e = Equipment()
    t = Telescope(80, 480, vendor="Refractor", outputs=[(ConnectionType.M48, Gender.MALE)])

    # Use unique connection M68 between Rotator and Focuser to force the order
    rot = Rotator("Falcon", in_connection=(ConnectionType.M48, Gender.FEMALE), out_connection=(ConnectionType.M68, Gender.MALE))
    foc = Focuser("ESATTO", in_connection=(ConnectionType.M68, Gender.FEMALE), out_connection=(ConnectionType.M42, Gender.MALE))

    cam = Camera(10, 10, 1000, 1000, vendor="Cam", inputs=[(ConnectionType.M42, Gender.FEMALE)])

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
    t = Telescope(80, 480, outputs=[(ConnectionType.M54, Gender.MALE)])

    # Use chain of unique connections: M54 -> M56 -> M63 -> M48 -> M42
    at = AntiTilt("TiltPlate", in_connection=(ConnectionType.M54, Gender.FEMALE), out_connection=(ConnectionType.M56, Gender.MALE))
    sp = Spacer("10mm Spacer", in_connection=(ConnectionType.M56, Gender.FEMALE), out_connection=(ConnectionType.M63, Gender.MALE), optical_length=10)
    ad = Adapter("M54 to M42", in_connection=(ConnectionType.M63, Gender.FEMALE), out_connection=(ConnectionType.M42, Gender.MALE))

    cam = Camera(10, 10, 1000, 1000, inputs=[(ConnectionType.M42, Gender.FEMALE)])

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

def test_gender_exclusivity():
    """
    Verify that components with matching genders (e.g., two Male M42 ports)
    do not connect, while opposing genders do.
    """
    # Test Case 1: Matching genders block connection
    # Telescope(M54 Male) -> Adapter(M54 Female IN, M42 Female OUT) -> Camera(M42 Female IN)
    # The last connection (F to F) should fail.
    # Direct Telescope to Camera should fail due to size mismatch (M54 vs M42).
    t = Telescope(80, 480, outputs=[(ConnectionType.M54, Gender.MALE)])
    ad = Adapter("M54F-M42F Coupler", in_connection=(ConnectionType.M54, Gender.FEMALE), out_connection=(ConnectionType.M42, Gender.FEMALE))
    c = Camera(10, 10, 1000, 1000, inputs=[(ConnectionType.M42, Gender.FEMALE)])

    e1 = Equipment()
    e1.register(t)
    e1.register(ad)
    e1.register(c)

    paths1 = e1._get_paths("Image")
    assert len(paths1) == 0

    # Test Case 2: Adding a gender changer resolves the blockage
    # Telescope(M) -> Adapter(F, F) -> GenderChanger(M, M) -> Camera(F)
    gc = Adapter("M42M-M42M Gender Changer", in_connection=(ConnectionType.M42, Gender.MALE), out_connection=(ConnectionType.M42, Gender.MALE))
    e1.register(gc)

    paths2 = e1._get_paths("Image")
    assert len(paths2) == 1
    label = paths2[0].label()
    assert "M54F-M42F Coupler" in label
    assert "M42M-M42M Gender Changer" in label

    # Test Case 3: Push-fit connections (1.25") allow connecting if one or both genders are missing
    # (Existing legacy behavior)
    e3 = Equipment()
    t3 = Telescope(80, 480, outputs=[(ConnectionType.F_1_25, None)])
    c3 = Camera(10, 10, 1000, 1000, inputs=[(ConnectionType.F_1_25, None)])
    e3.register(t3)
    e3.register(c3)
    assert len(e3._get_paths("Image")) == 1
