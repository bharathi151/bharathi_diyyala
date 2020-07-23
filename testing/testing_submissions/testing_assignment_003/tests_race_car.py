from car import Car
from race_car import RaceCar
import pytest
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",-100,10,3),("red",0,10,3)
])

def test_object_creation_with_invalid_max_speed_raise_value_error(color,max_speed,acceleration,tyre_friction):
    #arrange
    error="Invalid value for max_speed"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    assert max_speed<=0
    assert str(e.value)==error
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,-10,3),("red",100,0,3)
])
    
def test_object_creation_with_invalid_acceleration_raise_value_error(color,max_speed,acceleration,tyre_friction):
    #arrange
    error="Invalid value for acceleration"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    assert acceleration<=0
    assert str(e.value)==error
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,-3),("red",100,10,0)
])

def test_object_creation_with_invalid_tyre_friction_raise_value_error(color,max_speed,acceleration,tyre_friction):
    #arrange
    error="Invalid value for tyre_friction"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    assert tyre_friction<=0
    assert str(e.value)==error  
    
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])

    
def test_object_creation_with_valid_details_rerurn_car_object(color,max_speed,acceleration,tyre_friction):
    #arrange 
    
    #act
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    #assert
    assert isinstance(car,Car)
    assert car.max_speed==max_speed
    assert car.tyre_friction==tyre_friction
    assert car.acceleration==acceleration
    assert car.is_engine_started==False
    assert car.current_speed==0
    assert car.max_speed>car.acceleration
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3),("red",130,15,5)
])

    
def test_multiple_objects_creation_with_valid_details_return_car_objects(color,max_speed,acceleration,tyre_friction):
    #arrange 
    
    #act
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    #assert
    assert isinstance(car,Car)
    assert car.max_speed==max_speed
    assert car.tyre_friction==tyre_friction
    assert car.acceleration==acceleration
    assert car.is_engine_started==False
    assert car.current_speed==0
    assert car.max_speed>car.acceleration
 
 
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])
  
def test_start_engine_first_time_returns_is_engine_true(color,max_speed,acceleration,tyre_friction):
    #arrange
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #act
    car.start_engine()
    #assert 
    assert car.is_engine_started==True
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])
def test_current_speed_when_start_engine_called_twice_return_is_engine_started_true(color,max_speed,acceleration,tyre_friction):
    #arrange
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #act
    car.start_engine()
    car.start_engine()
    #assert 
    assert car.is_engine_started==True

    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])
def test_sound_horn_when_car_engine_is_not_started_return_warn(color,max_speed,acceleration,tyre_friction,capsys):
    #arrange
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    warn="Start the engine to sound_horn\n"
    #act
    car.sound_horn()
    captured = capsys.readouterr()
    
    #assert
    assert car.is_engine_started==False
    assert captured.out==warn
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])
def test_sound_horn_when_car_engine_is_started_returns_sound(color,max_speed,acceleration,tyre_friction,capsys):
    #arrange
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    horn="Beep Beep\n"
    car.start_engine()
    #act
    
    car.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert car.is_engine_started==True
    assert captured.out==horn
    
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",100,10,3)
])   
def test_accelerate_before_engine_starts_returns_error(color,max_speed,acceleration,tyre_friction,capsys):
    #arrange
    car= RaceCar(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    
    warn="Start the engine to accelerate\n"
    #act
    car.accelerate()
    captured = capsys.readouterr()
    #assert
    assert captured.out==warn
   

def test_stop_engine_when_car_is_not_running_returns_is_engine_started_false():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.stop_engine()
    
    #assert
    assert car.is_engine_started==False

    
    
    
def test_stop_engine_when_car_is_running_returns_is_engine_started_false():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    car.start_engine()

    #act
    
    
    car.stop_engine()
    
    #assert
    assert car.is_engine_started==False
   
    



def test_apply_breaks_before_engine_starts_zero_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    zero_current_speed=0
    #act
    car.apply_brakes()
    
    #assert
    assert car.is_engine_started==False
    assert car.current_speed==zero_current_speed
    
def test_apply_breaks_after_engine_starts_return_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=0
    car.start_engine()
    #act
    
    car.apply_brakes()
    
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    
def test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=10
    car.start_engine()
    
    #act
    
    car.accelerate()
    
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    
    
def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=11,tyre_friction=3)
    updated_current_speed=20
    car.start_engine()
    car.accelerate()
    
    #act
    
    car.accelerate()
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    
    
    

def test_accelerate_equal_to_max_limit_current_speed_returns_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=20
    car.start_engine()
    car.accelerate()
    speed_at_accelerate=car.current_speed
    #act
    
    car.accelerate()
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    



def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=0
    car.start_engine()
    
    #act
    
    car.apply_brakes()
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    
    
    
def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    updated_current_speed=7
    car.start_engine()
    car.accelerate()

    #act
    
    car.apply_brakes()
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==updated_current_speed
    
    
    
def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=3,tyre_friction=3)
    zero_current_speed=0
    car.start_engine()
    car.accelerate()
    #act

    car.apply_brakes()
    #assert
    assert car.is_engine_started==True
    assert car.current_speed==zero_current_speed  
    
    


    

    
def test_color_encaspulation_returns_updated_color():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_color="blue"
    #act
    car._color=new_color
    #assert
    assert car.color==new_color
    
def test_current_speed_encaspulation_returns_updated_current_speed():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_speed=10
    #act
    car._color=new_speed
    #assert
    assert car.color==new_speed
    

def test_tyre_friction_encaspulation_returns_updated_tyre_friction():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_tyre_friction=4
    #act
    car._tyre_friction=new_tyre_friction
    #assert
    assert car.tyre_friction==new_tyre_friction
    
def test_max_speed_encaspulation_returns_updated_max_speed():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    max_speed=30
    #act
    car._max_speed=max_speed
    #assert
    assert car.max_speed==max_speed
    
def test_acceleraton_encaspulation_returns_updated_acceleration():
    #arrange
    from car import Car
    car=RaceCar(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    new_acceleration=5
    #act
    car._acceleration=new_acceleration
    #assert
    assert car.acceleration==new_acceleration
    

