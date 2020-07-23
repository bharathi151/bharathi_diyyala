from car import Car


def test_accelerate_before_engine_starts_returns_error(car,
                                                       capsys):
    # arrange
    false = False
    warn = "Start the engine to accelerate\n"

    # act
    car.accelerate()
    captured = capsys.readouterr()

    # assert
    assert car.is_engine_started == false
    assert captured.out == warn


def test_acceleration_when_curent_speed_less_than_max_speed_returns_updated_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=10, tyre_friction=3)
    true = True
    updated_current_speed = 10
    car.start_engine()

    # act
    car.accelerate()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=11, tyre_friction=3)
    true = True
    updated_current_speed = 20
    car.start_engine()
    car.accelerate()

    # act
    car.accelerate()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=10, tyre_friction=3)
    true = True
    updated_current_speed = 20
    car.start_engine()
    car.accelerate()

    # act
    car.accelerate()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed
