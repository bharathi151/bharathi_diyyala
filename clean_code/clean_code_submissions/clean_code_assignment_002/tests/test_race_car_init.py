import pytest
from race_car import RaceCar


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("blue", -100, 20, 5), ("black", 0, 20, 5)])
def test_race_car_object_creation_with_invalid_max_speed_raise_value_error(color,
                                                                           max_speed,
                                                                           acceleration,
                                                                           tyre_friction):
    #arrange
    error = "Invalid value for max_speed"
    zero = 0
    #act
    with pytest.raises(ValueError) as error_exception:
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    #assert
    assert max_speed <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("blue", 120, -10, 5), ("black", 120, 0, 5)])
def test_race_car_object_creation_with_invalid_acceleration_raise_value_error(color,
                                                                              max_speed,
                                                                              acceleration,
                                                                              tyre_friction):
    #arrange
    error = "Invalid value for acceleration"
    zero = 0
    #act
    with pytest.raises(ValueError) as error_exception: # Asserting the exception
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    #assert
    assert acceleration <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("blue", 110, 20, -5), ("black", 120, 20, 0)])
def test_race_car_object_creation_with_invalid_tyre_friction_raise_value_error(color,
                                                                               max_speed,
                                                                               acceleration,
                                                                               tyre_friction):
    #arrange
    error = "Invalid value for tyre_friction"
    zero = 0
    #act
    with pytest.raises(ValueError) as error_exception: # Asserting the exception
        assert RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    #assert
    assert tyre_friction <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("blue", 2, 1, 1)])
def test_race_car_object_creation_with_valid_details_rerurn_race_car_object(color,
                                                                            max_speed,
                                                                            acceleration,
                                                                            tyre_friction):
    #arrange
    zero = 0
    false = False
    #act
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)

    #assert
    assert race_car.max_speed == max_speed
    assert race_car.tyre_friction == tyre_friction
    assert race_car.acceleration == acceleration
    assert race_car.is_engine_started == false
    assert race_car.current_speed == zero
    assert race_car.nitro == zero
    assert race_car.max_speed > race_car.acceleration


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [("black", 2, 1, 1), ("blue", 1, 1, 1)])
def test_multiple_race_car_objects_creation_with_valid_details_return_race_car_objects(color,
                                                                                       max_speed,
                                                                                       acceleration,
                                                                                       tyre_friction):
    #arrange
    zero = 0
    false = False
    #act
    race_car = RaceCar(color=color, max_speed=max_speed,
                       acceleration=acceleration,
                       tyre_friction=tyre_friction)
    #assert
    assert race_car.max_speed == max_speed
    assert race_car.tyre_friction == tyre_friction
    assert race_car.acceleration == acceleration
    assert race_car.is_engine_started == false
    assert race_car.current_speed == zero
    assert race_car.nitro == zero
