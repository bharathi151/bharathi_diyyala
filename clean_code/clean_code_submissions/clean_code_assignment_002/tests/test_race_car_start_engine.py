def test_start_engine_first_time_returns_is_engine_true(race_car):
    #arrange
    true = True
    #act
    race_car.start_engine()
    #assert
    assert race_car.is_engine_started == true


def test_current_speed_when_start_engine_called_twice_return_is_engine_started_true(race_car):
    #arrange
    true = True
    #act
    race_car.start_engine()
    race_car.start_engine()
    #assert
    assert race_car.is_engine_started == true
