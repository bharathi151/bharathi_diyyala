def test_load_when_truck_obj_is_in_motion_raises_warn(capsys, truck_obj):
    #arrange
    load_weight = 30
    zero = 0
    truck_obj.load(load_weight)
    truck_obj.start_engine()
    truck_obj.accelerate()
    extra_load_weight = 20
    warn = "Cannot load cargo during motion\n"
    #act
    truck_obj.load(extra_load_weight)
    captured = capsys.readouterr()
    #assert
    assert truck_obj.current_speed > zero
    assert captured.out == warn
    assert truck_obj.cargo_weight <= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == extra_load_weight


def test_load_when_load_is_more_than_max_limit_raises_warn(capsys, truck_obj):
    #arrange
    truck_obj.start_engine()
    warn = "Cannot load cargo more than max limit: 50\n"
    load = 70
    zero = 0
    #act
    truck_obj.load(load)
    captured = capsys.readouterr()
    #assert
    assert truck_obj.current_speed == zero
    assert captured.out == warn
    assert load >= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == zero


def test_load_when_truck_obj_is_not_motion_returns_loaded_weight(truck_obj):
    #arrange
    truck_obj.start_engine()
    load_weight = 50
    zero = 0
    #act
    truck_obj.load(load_weight)
    #assert
    assert truck_obj.current_speed == zero
    assert truck_obj.cargo_weight <= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == load_weight
