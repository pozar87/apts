import networkx as nx

from ...config import get_dark_mode as get_dark_mode
from .base import BaseEquipmentPlottingMixIn as BaseEquipmentPlottingMixIn
from .graph import GraphEquipmentPlottingMixIn as GraphEquipmentPlottingMixIn
from .simple import SimpleEquipmentPlottingMixIn as SimpleEquipmentPlottingMixIn


class EquipmentPlottingMixIn(SimpleEquipmentPlottingMixIn, GraphEquipmentPlottingMixIn):
    """
    Modularized plotting mixin for astronomical equipment.
    Inherits from Simple (zoom, fov) and Graph (connection graph) specialized mixins.
    """

    pass
