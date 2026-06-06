from scripts.audit_equipment_ports import audit
def test_equipment_database_port_standards():
    assert not audit()
