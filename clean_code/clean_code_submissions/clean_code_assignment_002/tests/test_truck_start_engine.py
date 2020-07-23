def test_start_engine_first_time_returns_is_engine_true(truck):
    # arrange
    zero = 0
    true = True
    # act
    truck.start_engine()
    # assert
    assert truck.is_engine_started == true
    assert truck.cargo_weight == zero


def test_current_speed_when_start_engine_called_twice_return_is_engine_started_true(truck):
    # arrange
    zero = 0
    true = True
    # act
    truck.start_engine()
    truck.start_engine()
    # assert
    assert truck.is_engine_started == true
    assert truck.cargo_weight == zero
