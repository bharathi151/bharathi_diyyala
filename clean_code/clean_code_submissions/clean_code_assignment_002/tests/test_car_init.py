import pytest
from car import Car


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("red", -100, 10, 3), ("red", 0, 10, 3)])
def test_object_creation_with_invalid_max_speed_raise_value_error(color,
                                                                  max_speed,
                                                                  acceleration,
                                                                  tyre_friction):
    # arrange
    error = "Invalid value for max_speed"

    # act
    with pytest.raises(ValueError) as error_exception:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration,
                   tyre_friction=tyre_friction)

    # assert
    assert max_speed <= 0
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("red", 100, -10, 3), ("red", 110, 0, 5)])
def test_object_creation_with_invalid_acceleration_raise_value_error(color,
                                                                     max_speed,
                                                                     acceleration,
                                                                     tyre_friction):
    # arrange
    error = "Invalid value for acceleration"

    # act
    with pytest.raises(ValueError) as error_exception:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration,
                   tyre_friction=tyre_friction)

    # assert
    assert acceleration <= 0
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("red", 100, 10, -3), ("red", 100, 10, 0)])
def test_car_object_creation_with_invalid_tyre_friction_raise_value_error(color,
                                                                      max_speed,
                                                                      acceleration,
                                                                      tyre_friction):
    # arrange
    error = "Invalid value for tyre_friction"

    # act
    with pytest.raises(ValueError) as error_exception:
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration,
                   tyre_friction=tyre_friction)

    # assert
    assert tyre_friction <= 0
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("red", 2, 1, 1)])
def test_car_object_creation_with_valid_details_rerurn_car_object(color,
                                                              max_speed,
                                                              acceleration,
                                                              tyre_friction):
    # arrange
    false = False

    # act
    car = Car(color=color, max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction)

    # assert
    assert car.max_speed == max_speed
    assert car.tyre_friction == tyre_friction
    assert car.acceleration == acceleration
    assert car.is_engine_started == false
    assert car.current_speed == 0
    assert car.max_speed > car.acceleration


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("red", 2, 1, 1), ("red", 3, 1, 1)])
def test_multiple_car_objects_creation_with_valid_details_return_car_objects(color,
                                                                         max_speed,
                                                                         acceleration,
                                                                         tyre_friction):
    # arrange
    false = False

    # act
    car = Car(color=color, max_speed=max_speed,
              acceleration=acceleration,
              tyre_friction=tyre_friction)

    # assert
    assert car.max_speed == max_speed
    assert car.tyre_friction == tyre_friction
    assert car.acceleration == acceleration
    assert car.is_engine_started == false
    assert car.current_speed == 0
    assert car.max_speed > car.acceleration
