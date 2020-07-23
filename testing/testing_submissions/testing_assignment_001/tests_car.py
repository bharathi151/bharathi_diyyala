from car import Car

import pytest
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",-100,10,3),("red",0,10,3)
])

def test_object_creation_with_invalid_max_speed_raise_value_error(
    color, max_speed, acceleration, tyre_friction, snapshot):
    #arrange
    error="Invalid value for max_speed"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    snapshot.assert_match(str(e.value), "Invalid value for max_speed")
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,-10,3),("red",100,0,3)
])
    
def test_object_creation_with_invalid_acceleration_raise_value_error(
    color, max_speed, acceleration, tyre_friction, snapshot):
    #arrange
    error="Invalid value for acceleration"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    snapshot.assert_match(str(e.value), "Invalid value for acceleration")

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,-3),("red",100,10,0)
])

def test_object_creation_with_invalid_tyre_friction_raise_value_error(
    color, max_speed, acceleration, tyre_friction, snapshot):
    #arrange
    error="Invalid value for tyre_friction"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Car(color=color, max_speed=max_speed,
                   acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    snapshot.assert_match(str(e.value), "Invalid value for tyre_friction")

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",2,1,1)
])
def test_object_creation_with_valid_details_rerurn_car_object(
    color, max_speed, acceleration, tyre_friction, snapshot):
    #arrange 
    
    #act
    car= Car(color=color, max_speed=max_speed,
             acceleration=acceleration, tyre_friction=tyre_friction)
    
    #assert
    assert_created_car_object(car, snapshot)
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",2,1,1),("red",3,1,1)
])
def test_multiple_objects_creation_with_valid_details_return_car_objects(
    color, max_speed, acceleration, tyre_friction, snapshot):
    #arrange 
    
    #act
    car= Car(color=color, max_speed=max_speed,
             acceleration=acceleration, tyre_friction=tyre_friction)
    
    #assert
    assert_created_car_object(car, snapshot)

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",1,1,1)
])
  
def test_start_engine_first_time_returns_is_engine_true(color,max_speed, acceleration, tyre_friction, snapshot):
    #arrange
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #act
    car.start_engine()
    #assert 
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",1,1,1)
])
def test_current_speed_when_start_engine_called_twice_return_is_engine_started_true(color,max_speed, acceleration, tyre_friction, snapshot):
    #arrange
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #act
    car.start_engine()
    car.start_engine()
    #assert 
    snapshot.assert_match(car.is_engine_started, "is_engine_started")

    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",1,1,1)
])
def test_sound_horn_when_car_engine_is_not_started_return_warn(color,max_speed, acceleration, tyre_friction, snapshot,capsys):
    #arrange
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    warn="Start the engine to sound_horn\n"
    #act
    car.sound_horn()
    captured = capsys.readouterr()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(captured.out==warn, "warn for start_engine")

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",1,1,1)
])
def test_sound_horn_when_car_engine_is_started_returns_sound(color,max_speed, acceleration, tyre_friction, snapshot,capsys):
    #arrange
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    horn="Beep Beep\n"
    car.start_engine()
    #act
    
    car.sound_horn()
    captured = capsys.readouterr()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(captured.out, "horn_sound")

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",1,1,1)
])   
def test_accelerate_before_engine_starts_returns_error(color,max_speed, acceleration, tyre_friction, snapshot,capsys):
    #arrange
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    warn="Start the engine to accelerate\n"
    #act
    car.accelerate()
    captured = capsys.readouterr()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(captured.out==warn, "warn for start_engine")
   

def test_stop_engine_when_car_is_not_running_returns_is_engine_started_false(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.stop_engine()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")

def test_stop_engine_when_car_is_running_returns_is_engine_started_false(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=1,acceleration=1,tyre_friction=1)
    car.start_engine()

    #act
    
    
    car.stop_engine()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")


def test_apply_breaks_before_engine_starts_zero_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=1,acceleration=1,tyre_friction=1)
    zero_current_speed=0
    #act
    car.apply_brakes()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    
def test_apply_breaks_after_engine_starts_return_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=0
    car.start_engine()
    #act
    
    car.apply_brakes()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    
def test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=10
    car.start_engine()
    
    #act
    
    car.accelerate()
    
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    
    
def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=11,tyre_friction=3)
    updated_current_speed=20
    car.start_engine()
    car.accelerate()
    
    #act
    
    car.accelerate()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    
    
    

def test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=20
    car.start_engine()
    car.accelerate()
    speed_at_accelerate=car.current_speed
    #act
    
    car.accelerate()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    



def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=0
    car.start_engine()
    
    #act
    
    car.apply_brakes()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")
    
    
    
def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=7
    car.start_engine()
    car.accelerate()

    #act
    
    car.apply_brakes()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")

def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=3)
    zero_current_speed=0
    car.start_engine()
    car.accelerate()
    #act

    car.apply_brakes()
    #assert
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")

def test_color_encaspulation_returns_updated_color(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_color="blue"
    #act
    with pytest.raises(AttributeError) as e:
        car.color=new_color
    #assert
    assert_attribute_error(e, snapshot)

def test_current_speed_encaspulation_returns_updated_current_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_speed=10
    #act
    with pytest.raises(AttributeError) as e:
        car.current_speed=new_speed
    #assert
    assert_attribute_error(e, snapshot)

def test_tyre_friction_encaspulation_returns_updated_tyre_friction(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_tyre_friction=4
    #act
    with pytest.raises(AttributeError) as e:
        car.tyre_friction=new_tyre_friction
    #assert
    assert_attribute_error(e, snapshot)
    
def test_max_speed_encaspulation_returns_updated_max_speed(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    max_speed=30
    #act
    with pytest.raises(AttributeError) as e:
        car.max_speed=max_speed
    #assert
    assert_attribute_error(e, snapshot)
    
def test_acceleraton_encaspulation_returns_updated_acceleration(snapshot):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_acceleration=5
    #act
    with pytest.raises(AttributeError) as e:
        car.acceleration=new_acceleration
    #assert
    assert_attribute_error(e, snapshot)

def assert_attribute_error(e, snapshot):
    snapshot.assert_match(str(e.value), "error_message")

def assert_created_car_object(car, snapshot):
    snapshot.assert_match(isinstance(car,Car), "is_instance")
    snapshot.assert_match(car.max_speed, "max_speed")
    snapshot.assert_match(car.tyre_friction, "tyre_friction")
    snapshot.assert_match(car.acceleration, "acceleration")
    snapshot.assert_match(car.is_engine_started, "is_engine_started")
    snapshot.assert_match(car.current_speed, "current_speed")