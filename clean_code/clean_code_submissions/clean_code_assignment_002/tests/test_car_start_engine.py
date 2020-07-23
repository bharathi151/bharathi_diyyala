def test_start_engine_returns_is_engine_true(car):
    # arrange
    true = True

    # act
    car.start_engine()

    # assert
    assert car.is_engine_started == true


def test_start_engine_when_start_engine_called_twice_return_is_engine_started_true(car):
    # arrange
    true = True

    # act
    car.start_engine()
    car.start_engine()

    # assert
    assert car.is_engine_started == true
