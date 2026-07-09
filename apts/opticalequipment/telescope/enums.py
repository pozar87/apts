from enum import Enum


class TelescopeType(Enum):
    REFRACTOR = "refractor"
    NEWTONIAN_REFLECTOR = "newtonian_reflector"
    SCHMIDT_CASSEGRAIN = "schmidt_cassegrain"
    MAKSUTOV_CASSEGRAIN = "maksutov_cassegrain"
    CATADIOPTRIC = "catadioptric"


class TubeMaterial(Enum):
    ALUMINUM = 2.31e-05
    CARBON_FIBER = 5e-07
    STEEL = 1.2e-05
    BRASS = 1.9e-05
    GLASS_FIBER = 8e-06
