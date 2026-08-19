class ObjectTableLabels:
    # Altitude
    ALTITUDE = "Altitude"
    # Transit time
    TRANSIT = "Transit"
    # Right ascension
    RA = "RA"
    # Declination
    DEC = "Dec"
    # Name
    NAME = "Name"
    # Obeject
    OBJECT = "Object"
    # Magnitude
    MAGNITUDE = "Magnitude"
    # Distance
    DISTANCE = "Distance"
    # Phase
    PHASE = "Phase"
    # Apparent size
    SIZE = "Size"
    # Elongation
    ELONGATION = "Elongation"
    # Rising
    RISING = "Rising"
    # Setting
    SETTING = "Setting"

    SIMBAD = "SIMBAD"
    ALADIN = "ALADIN"
    ASTROBIN = "Astrobin"

    MESSIER = "Messier"
    NGC = "NGC"
    IC = "IC"
    TYPE = "Type"
    DSO_TYPE = "DSO Type"
    SIZE_MAJOR = "Size Major"
    SIZE_MINOR = "Size Minor"

    CURRENT_ALT = "current_alt"
    CURRENT_AZ = "current_az"


TECHNICAL_COLUMNS = [
    "skyfield_object",
    "ra_hours",
    "dec_degrees",
    "Magnitude_float",
    "sin_dec",
    "cos_dec_cos_ra",
    "cos_dec_sin_ra",
    "NGC_norm",
    "IC_norm",
    "Name_norm",
    "TechnicalName",
    "current_alt",
    "current_az",
]
