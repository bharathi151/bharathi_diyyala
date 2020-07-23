import pytest


def test_color_encaspulation_returns_updated_color(truck):
    #arrange
    new_color = "blue"
    error = "cant't set attribute"
    # act
    with pytest.raises(AttributeError) as error_exception:
        truck.color = new_color
    # assert
    assert str(error_exception.value) == error


def test_current_speed_encaspulation_returns_updated_current_speed(truck):
    #arrange
    new_speed = 10
    error = "cant't set attribute"
    # act
    with pytest.raises(AttributeError) as error_exception:
        truck.current_speed = new_speed
    # assert
    assert str(error_exception.value) == error


def test_tyre_friction_encaspulation_returns_updated_tyre_friction(truck):
    #arrange
    new_tyre_friction = 4
    error = "cant't set attribute"
    # act
    with pytest.raises(AttributeError) as error_exception:
        truck.tyre_friction = new_tyre_friction
    # assert
    assert str(error_exception.value) == error


def test_max_speed_encaspulation_returns_updated_max_speed(truck):
    #arrange
    max_speed = 30
    #act
    truck.max_speed = max_speed
    #assert
    assert truck.max_speed == max_speed


def test_acceleraton_encaspulation_returns_updated_acceleration(truck):
    #arrange
    new_acceleration = 5
    error = "cant't set attribute"
    # act
    with pytest.raises(AttributeError) as error_exception:
        truck.acceleration = new_acceleration
    # assert
    assert str(error_exception.value) == error


def test_max_cargo_weight_encaspulation_returns_updated_max_cargo_weight(truck):
    #arrange
    new_weight = 5
    error = "cant't set attribute"
    # act
    with pytest.raises(AttributeError) as error_exception:
        truck.max_cargo_weight = new_weight
    # assert
    assert str(error_exception.value) == error
