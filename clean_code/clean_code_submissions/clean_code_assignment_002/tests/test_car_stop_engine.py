def test_stop_engine_when_car_is_not_running_returns_is_engine_started_false(car):
    # arrange
    false = False
    # act
    car.stop_engine()

    # assert
    assert car.is_engine_started == false


def test_stop_engine_when_car_is_running_returns_is_engine_started_false(car):
    # arrange
    false = False
    car.start_engine()

    # act
    car.stop_engine()

    # assert
    assert car.is_engine_started == false
