import pytest


def test_color_encaspulation_raise_attribute_error(car):
    # arrange
    new_color = "blue"
    error = "cant't set attribute"

    # act
    with pytest.raises(AttributeError) as error_exception:
        car.color = new_color

    # assert
    assert str(error_exception.value) == error


def test_current_speed_encaspulation_raise_attribute_error(car):
    # arrange
    new_speed = 10
    error = "cant't set attribute"

    # act
    with pytest.raises(AttributeError) as error_exception:
        car.current_speed = new_speed

    # assert
    assert str(error_exception.value) == error


def test_tyre_friction_encaspulation_raise_attribute_error(car):
    # arrange
    new_tyre_friction = 4
    error = "cant't set attribute"

    # act
    with pytest.raises(AttributeError) as error_exception:
        car.tyre_friction = new_tyre_friction

    # assert
    assert str(error_exception.value) == error


def test_max_speed_encaspulation_raise_attribute_error(car):
    # arrange
    new_max_speed = 30
    error = "cant't set attribute"

    # act
    with pytest.raises(AttributeError) as error_exception:
        car.max_speed = new_max_speed

    # assert
    assert str(error_exception.value) == error


def test_acceleraton_encaspulation_raise_attribute_error(car):
    # arrange
    new_acceleration = 5
    error = "cant't set attribute"

    # act
    with pytest.raises(AttributeError) as error_exception:
        car.acceleration = new_acceleration

    # assert
    assert str(error_exception.value) == error
