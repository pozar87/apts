import pytest
from apts.opticalequipment.diagonal import Diagonal
from apts.equipment import Equipment
from apts.utils import ConnectionType

def test_diagonal_init():
    d = Diagonal(vendor="TeleVue", connection_type=ConnectionType.F_2, is_erecting=True)
    assert d.vendor == "TeleVue"
    assert d.connection_type == ConnectionType.F_2
    assert d.is_erecting
    assert not d.t2_output

def test_diagonal_register():
    eq = Equipment()
    d = Diagonal(vendor="TeleVue", connection_type=ConnectionType.F_2)
    d.register(eq)
    assert d.id() in eq.connection_garph.nodes()

def test_diagonal_register_t2():
    eq = Equipment()
    d = Diagonal(vendor="TeleVue", connection_type=ConnectionType.F_2, t2_output=True)
    d.register(eq)
    assert d.id() in eq.connection_garph.nodes()

def test_diagonal_str():
    d = Diagonal(vendor="TeleVue")
    assert str(d) == "TeleVue"
