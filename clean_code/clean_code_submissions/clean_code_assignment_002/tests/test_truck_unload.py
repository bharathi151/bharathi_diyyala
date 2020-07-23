def test_unload_when_truck_is_in_motion_raises_warn(capsys, truck_obj):
    #arrange
    load_weight = 50
    unload_weight = 20
    truck_obj.load(load_weight)
    truck_obj.start_engine()
    truck_obj.accelerate()
    warn = "Cannot unload cargo during motion\n"
    zero = 0
    #act
    truck_obj.unload(unload_weight)
    captured = capsys.readouterr()
    #assert
    assert truck_obj.current_speed > zero
    assert captured.out == warn
    assert truck_obj.cargo_weight <= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == load_weight


def test_unload_when_load_is_more_than_max_limit_raises_warn(truck_obj, capsys):
    #arrange
    truck_obj.start_engine()
    load_weight = 50
    warn = "Cannot unload cargo more than max limit: 50\n"
    truck_obj.load(load_weight)
    unload_weight = 70
    #act
    truck_obj.unload(unload_weight)
    captured = capsys.readouterr()
    #assert
    assert captured.out == warn
    assert load_weight >= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == load_weight


def test_unload_total_load_when_truck_is_not_motion_returns_remaining_load_weight(truck_obj):
    #arrange
    truck_obj.start_engine()
    load_weight = 50
    truck_obj.load(50)
    unload_weight = 50
    zero = 0
    #act
    truck_obj.unload(unload_weight)
    #assert
    assert truck_obj.current_speed == zero
    assert truck_obj.cargo_weight <= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == zero
    assert load_weight <= truck_obj.max_cargo_weight


def test_unload_when_truck_is_not_motion_returns_remaining_load_weight(truck_obj):
    #arrange
    truck_obj.start_engine()
    load_weight = 50
    truck_obj.load(load_weight)
    unload_weight = 40
    remaing_weight = 10
    zero = 0
    #act
    truck_obj.unload(unload_weight)
    #assert
    assert truck_obj.current_speed == zero
    assert truck_obj.cargo_weight <= truck_obj.max_cargo_weight
    assert truck_obj.cargo_weight == remaing_weight
    assert load_weight <= truck_obj.max_cargo_weight
