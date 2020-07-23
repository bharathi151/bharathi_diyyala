from car import Car


def test_apply_breaks_before_engine_starts_zero_current_speed(car):
    # arrange
    false = False
    zero_current_speed = 0

    # act
    car.apply_brakes()

    # assert
    assert car.is_engine_started == false
    assert car.current_speed == zero_current_speed


def test_apply_breaks_after_engine_starts_return_updated_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=10, tyre_friction=3)
    true = True
    updated_current_speed = 0
    car.start_engine()

    # act
    car.apply_brakes()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=10, tyre_friction=3)
    true = True
    updated_current_speed = 0
    car.start_engine()

    # act
    car.apply_brakes()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=10, tyre_friction=3)
    true = True
    updated_current_speed = 7
    car.start_engine()
    car.accelerate()

    # act

    car.apply_brakes()
    # assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed():
    # arrange
    car = Car(color="red", max_speed=20,
              acceleration=3, tyre_friction=3)
    true = True
    zero_current_speed = 0
    car.start_engine()
    car.accelerate()

    # act
    car.apply_brakes()

    # assert
    assert car.is_engine_started == true
    assert car.current_speed == zero_current_speed
