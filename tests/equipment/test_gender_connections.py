from apts.equipment import Equipment
from apts.opticalequipment import Telescope, Camera, Eyepiece
from apts.utils import ConnectionType, Gender
from apts.constants import EquipmentTableLabels

def test_gender_matching_success():
    """Test that different genders connect correctly."""
    e = Equipment()

    # MALE output to FEMALE input
    tele_male = Telescope(150, 750, vendor="TeleMale", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)
    cam_female = Camera(10, 10, 100, 100, vendor="CamFemale", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)

    e.register(tele_male)
    e.register(cam_female)

    data = e.data()
    labels = data[EquipmentTableLabels.LABEL].tolist()
    assert any("TeleMale" in l and "CamFemale" in l for l in labels)

    # FEMALE output to MALE input
    e2 = Equipment()
    tele_female = Telescope(150, 750, vendor="TeleFemale", connection_type=ConnectionType.F_1_25, connection_gender=Gender.FEMALE)
    ep_male = Eyepiece(25, vendor="EPMale", connection_type=ConnectionType.F_1_25, connection_gender=Gender.MALE)

    e2.register(tele_female)
    e2.register(ep_male)

    data2 = e2.data()
    labels2 = data2[EquipmentTableLabels.LABEL].tolist()
    assert any("TeleFemale" in l and "EPMale" in l for l in labels2)

def test_gender_matching_blocked_same_gender():
    """Test that same genders do not connect."""
    e = Equipment()

    # MALE to MALE
    tele_male = Telescope(150, 750, vendor="TeleMale", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)
    cam_male = Camera(10, 10, 100, 100, vendor="CamMale", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)

    e.register(tele_male)
    e.register(cam_male)

    data = e.data()
    labels = data[EquipmentTableLabels.LABEL].tolist()
    assert not any("TeleMale" in l and "CamMale" in l for l in labels)

    # FEMALE to FEMALE
    e2 = Equipment()
    tele_female = Telescope(150, 750, vendor="TeleFemale", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)
    cam_female = Camera(10, 10, 100, 100, vendor="CamFemale", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)

    e2.register(tele_female)
    e2.register(cam_female)

    data2 = e2.data()
    labels2 = data2[EquipmentTableLabels.LABEL].tolist()
    assert not any("TeleFemale" in l and "CamFemale" in l for l in labels2)

def test_gender_matching_blocked_missing_gender():
    """Test that connections are blocked if any gender is missing."""
    # None to MALE
    e1 = Equipment()
    tele_none = Telescope(150, 750, vendor="TeleNone", connection_type=ConnectionType.T2, connection_gender=None)
    cam_male = Camera(10, 10, 100, 100, vendor="CamMale", connection_type=ConnectionType.T2, connection_gender=Gender.MALE)
    e1.register(tele_none)
    e1.register(cam_male)
    assert not any("TeleNone" in l and "CamMale" in l for l in e1.data()[EquipmentTableLabels.LABEL])

    # FEMALE to None
    e2 = Equipment()
    tele_female = Telescope(150, 750, vendor="TeleFemale", connection_type=ConnectionType.T2, connection_gender=Gender.FEMALE)
    cam_none = Camera(10, 10, 100, 100, vendor="CamNone", connection_type=ConnectionType.T2, connection_gender=None)
    e2.register(tele_female)
    e2.register(cam_none)
    assert not any("TeleFemale" in l and "CamNone" in l for l in e2.data()[EquipmentTableLabels.LABEL])

    # None to None
    e3 = Equipment()
    tele_none2 = Telescope(150, 750, vendor="TeleNone", connection_type=ConnectionType.T2, connection_gender=None)
    cam_none2 = Camera(10, 10, 100, 100, vendor="CamNone", connection_type=ConnectionType.T2, connection_gender=None)
    e3.register(tele_none2)
    e3.register(cam_none2)
    assert not any("TeleNone" in l and "CamNone" in l for l in e3.data()[EquipmentTableLabels.LABEL])

def test_explicit_t2_gender_on_telescope():
    """Test that Telescope T2 output now has a gender and connects to camera."""
    e = Equipment()
    # By default, t2_output=True should now register a MALE T2 output
    tele = Telescope(150, 750, vendor="TeleT2", t2_output=True)
    # Camera T2 input is FEMALE by default
    cam = Camera(10, 10, 100, 100, vendor="CamT2")

    e.register(tele)
    e.register(cam)

    data = e.data()
    labels = data[EquipmentTableLabels.LABEL].tolist()
    # It should connect!
    assert any("TeleT2" in l and "CamT2" in l for l in labels)
