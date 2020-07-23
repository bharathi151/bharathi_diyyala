def test_stop_engine_when_car_is_not_running_returns_is_engine_started_false(race_car):
    #arrange
    false = False
    #act
    race_car.stop_engine()
    #assert
    assert race_car.is_engine_started == false


def test_stop_engine_when_car_is_running_returns_is_engine_started_false(race_car):
    #arrange
    false = False
    race_car.start_engine()
    #act
    race_car.stop_engine()
    #assert
    assert race_car.is_engine_started == false
