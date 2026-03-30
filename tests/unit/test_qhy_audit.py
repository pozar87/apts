import pytest
from apts.opticalequipment.camera.vendors.qhy import QhyCamera

def test_qhy268c_specs():
    camera = QhyCamera.from_database(QhyCamera._DATABASE['QHY_QHY_268C'])
    assert camera.width == 6252
    assert camera.height == 4176
    assert camera.optical_length.magnitude == 17.5
    assert camera.mass.magnitude == 780
    assert camera.quantum_efficiency == 92

def test_qhy268m_specs():
    camera = QhyCamera.from_database(QhyCamera._DATABASE['QHY_QHY_268M'])
    assert camera.width == 6252
    assert camera.height == 4176
    assert camera.optical_length.magnitude == 17.5
    assert camera.mass.magnitude == 780
    assert camera.quantum_efficiency == 92

def test_qhy600m_specs():
    camera = QhyCamera.from_database(QhyCamera._DATABASE['QHY_QHY_600M'])
    assert camera.width == 9576
    assert camera.height == 6388
    assert camera.mass.magnitude == 900
    assert camera.quantum_efficiency == 91

def test_qhy600c_specs():
    camera = QhyCamera.from_database(QhyCamera._DATABASE['QHY_QHY_600C'])
    assert camera.width == 9576
    assert camera.height == 6388
    assert camera.mass.magnitude == 900
    assert camera.quantum_efficiency == 91
