def test_stop_engine_when_truck_is_not_running_returns_is_engine_started_false(truck):
    #arrange
    #act
    truck.stop_engine()
    zero = 0
    false = False

    #assert
    assert truck.is_engine_started == false
    assert truck.cargo_weight == zero


def test_stop_engine_when_truck_is_running_returns_is_engine_started_false(truck):
    #arrange
    truck.start_engine()
    false = False
    zero = 0

    #act
    truck.stop_engine()

    #assert
    assert truck.is_engine_started == false
    assert truck.cargo_weight == zero
