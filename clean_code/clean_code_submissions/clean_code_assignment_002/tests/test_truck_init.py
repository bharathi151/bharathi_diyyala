import pytest
from truck import Truck


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [("red", -100, 10, 3, 50), ("red", 0, 10, 3, 50)])
def test_object_creation_with_invalid_max_speed_raise_value_error(color,
                                                                  max_speed,
                                                                  acceleration,
                                                                  tyre_friction,
                                                                  max_cargo_weight):
    # arrange
    error = "Invalid value for max_speed"
    zero = 0
    # act
    with pytest.raises(ValueError) as error_exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # assert
    assert max_speed <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [("red", 100, -10, 3, 50), ("red", 100, 0, 3, 50)])
def test_object_creation_with_invalid_acceleration_raise_value_error(color,
                                                                     max_speed,
                                                                     acceleration,
                                                                     tyre_friction,
                                                                     max_cargo_weight):
    # arrange
    error = "Invalid value for acceleration"
    zero = 0
    # act
    with pytest.raises(ValueError) as error_exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # assert
    assert acceleration <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [("red", 100, 10, -3, 50), ("red", 100, 10, 0, 50)])
def test_object_creation_with_invalid_tyre_friction_raise_value_error(color,
                                                                      max_speed,
                                                                      acceleration,
                                                                      tyre_friction,
                                                                      max_cargo_weight):
    # arrange
    error = "Invalid value for tyre_friction"
    zero = 0
    # act
    with pytest.raises(ValueError) as error_exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # assert
    assert tyre_friction <= zero
    assert str(error_exception.value) == error


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [("red", 100, 10, 3, -5), ("red", 100, 10, 3, 0)])
def test_object_creation_with_invalid_cargo_weight_raise_value_error(color,
                                                                     max_speed,
                                                                     acceleration,
                                                                     tyre_friction,
                                                                     max_cargo_weight):
    # arrange
    error = "Invalid value for cargo_weight"
    zero = 0
    # act
    with pytest.raises(ValueError) as error_exception:
        assert Truck(color=color, max_speed=max_speed,
                     acceleration=acceleration,
                     tyre_friction=tyre_friction,
                     max_cargo_weight=max_cargo_weight)
    # assert
    assert max_cargo_weight <= zero
    assert str(error_exception.value) == error


def test_object_creation_with_valid_details_rerurn_truck_object(truck):
    # arrange
    max_speed = 2
    tyre_friction = 1
    acceleration = 1
    max_cargo_weight = 1
    false = False
    zero = 0
    # act

    # assert
    assert truck.max_speed == max_speed
    assert truck.tyre_friction == tyre_friction
    assert truck.acceleration == acceleration
    assert truck.is_engine_started == false
    assert truck.current_speed == zero
    assert truck.max_cargo_weight == max_cargo_weight
    assert truck.max_speed > truck.acceleration
    assert truck.max_speed > truck.current_speed
    assert truck.cargo_weight == zero


@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [("red", 2, 1, 1, 1), ("red", 3, 1, 1, 1)])
def test_multiple_objects_creation_with_valid_details_return_truck_objects(color,
                                                                           max_speed,
                                                                           acceleration,
                                                                           tyre_friction,
                                                                           max_cargo_weight):
    # arrange
    zero = 0
    false = False

    # act
    truck = Truck(color=color, max_speed=max_speed,
                  acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)

    # assert
    assert truck.max_speed == max_speed
    assert truck.tyre_friction == tyre_friction
    assert truck.acceleration == acceleration
    assert truck.is_engine_started == false
    assert truck.current_speed == zero
    assert truck.max_cargo_weight == max_cargo_weight
    assert truck.max_speed > truck.acceleration
    assert truck.max_speed > truck.current_speed
    assert truck.cargo_weight == zero
