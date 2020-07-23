
import pytest
def test_car_creation_with_invalid_max_speed_where_max_speed_less_than_zero():
    #arrange
    from car import Car
    error='Invalid value for max_speed'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=-20,acceleration=3,tyre_friction=10)
    #assert
    assert str(e.value)==error

def test_car_creation_with_invalid_max_speed_where_max_speed_equals_to_zero():
    #arrange
    from car import Car
    error='Invalid value for max_speed'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=0,acceleration=3,tyre_friction=10)
    #assert
    assert str(e.value)==error

def test_car_creation_with_invalid_acceleration_where_acceleration_less_than_zero():
    #arrange
    from car import Car
    error='Invalid value for acceleration'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=20,acceleration=-3,tyre_friction=10)
    #assert
    assert str(e.value)==error

def test_car_creation_with_invalid_acceleration_where_acceleration_equals_to_zero():
    #arrange
    from car import Car
    error='Invalid value for acceleration'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=20,acceleration=0,tyre_friction=10)
    #assert
    assert str(e.value)==error
    


def test_car_creation_with_invalid_tyre_friction_where_tyre_friction_less_than_zero():
    #arrange
    from car import Car
    error='Invalid value for tyre_friction'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=20,acceleration=3,tyre_friction=-10)
    #assert
    assert str(e.value)==error

def test_car_creation_with_invalid_tyre_friction_where_tyre_friction_equals_to_zero():
    #arrange
    from car import Car
    error='Invalid value for tyre_friction'
    #act
    with pytest.raises(Exception) as e: # Asserting the exception
        assert Car(color="red",max_speed=20,acceleration=3,tyre_friction=0)
    #assert
    assert str(e.value)==error

def test__creation_with_valid_details():
    #arrange 
    from car import Car
    #act
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    
    #assert
    assert isinstance(car,Car)
    

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction", [
    ("red",130,10,3),("blue",20,3,10)
])
def test_creation_of_multiple_car_objects_with_valid_details(color,max_speed,acceleration,tyre_friction):
    #arange
    from car import Car
    #act
    car= Car(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction)
    #assert
    assert isinstance(car,Car)
    


def test_start_the_car_engine_when_car_is_not_running_returns_true():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.start_engine()
    
    #assert
    assert car.is_engine_started==True
    
def test_start_the_car_engine_when_car_is_running_returns_true():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.start_engine()
    car.start_engine()
    
    #assert
    assert car.is_engine_started==True


def test_object_creation_without_color():
    #arrange 
    from car import Car
    #act
    car=Car(max_speed=20,acceleration=3,tyre_friction=10)
    
    #assert
    assert isinstance(car,Car)

def test_object_creation_with_color_returns_true():
    #arrange 
    from car import Car
    #act
    car=Car(color="white",max_speed=20,acceleration=3,tyre_friction=10)
    
    #assert
    assert isinstance(car,Car)



def test_stop_the_car_engine_when_car_is_not_running_returns_true():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.stop_engine()
    
    #assert
    assert car.is_engine_started==False
    
def test_stop_the_car_engine_when_car_is_running_returns_true():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    #act
    car.start_engine()
    car.stop_engine()
    
    #assert
    assert car.is_engine_started==False

def test_set_the_car_current_speed_when_car_engine_starts_returns_zero():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    minimum_speed=0
    #act
    car.start_engine()
    
    #assert
    assert car.current_speed==minimum_speed

def test_horn_sound_before_engine_starts_returns_warn(capsys):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    warn="Start the engine to sound_horn\n"
    #act
    car.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert captured.out==warn

def test_horn_sound_after_engine_starts_return_horn(capsys):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    horn="Beep Beep\n"
    #act
    car.start_engine()
    car.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert captured.out==horn
    

def test_accelerate_before_engine_starts_reruns_warn(capsys):
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    warn="Start the engine to accelerate\n"
    #act
    car.accelerate()
    captured = capsys.readouterr()
    #assert
    assert captured.out==warn
    
def test_accelerate_after_engine_starts_increase_current_speed():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    accelerate_speed=3
    
    #act
    car.start_engine()
    car.accelerate()
    
    
    
    #assert
    assert car.current_speed==accelerate_speed

def test_apply_breaks_before_engine_starts():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=10)
    minimum_speed=0
    #act
    car.apply_brakes()
    
    #assert
    assert car.current_speed==minimum_speed
    
def test_apply_breaks_after_engine_starts():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    minimum_speed=0
    #act
    car.start_engine()
    car.apply_brakes()
    
    #assert
    assert car.current_speed==minimum_speed
    
def test_curent_speed_after_acceleration_with_increment():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    speed=car.acceleration
    #act
    car.start_engine()
    car.accelerate()
    
    #assert
    assert car.current_speed==speed
    
def test_curent_speed_more_than_max_speed_after_acceleration():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=11,tyre_friction=3)

    #act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    #assert
    assert car.current_speed==car.max_speed
    


    

def test_accelerate_equal_to_max_limit():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)

    #act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    #assert
    assert car.current_speed==car.max_speed

def test_apply_brakes_when_tyre_friction_more_than_current_speed():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    minimum_speed=0
    #act
    car.start_engine()
    car.apply_brakes()
    #assert
    assert car.current_speed==minimum_speed
    
def test_apply_brakes_when_tyre_friction_less_than_current_speed():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=10,tyre_friction=3)
    speed=7
    #act
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    #assert
    assert car.current_speed==speed
    
def test_apply_brakes_when_tyre_friction_equal_current_speed():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=3,tyre_friction=3)
    speed=0
    #act
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    #assert
    assert car.current_speed==speed   

def test_accelerate_after_apply_brakes():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    speed=5
    #act
    car.start_engine()
    car.apply_brakes()
    car.accelerate()
    
    #assert
    assert car.current_speed==speed  
def test_current_speed_after_stop_engine():
    #arrange
    from car import Car
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    speed=2
    #act
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    car.stop_engine()
    
    #assert
    assert car.current_speed==speed 
def test_encaspulation():
    #arrange
    from car import Car
    #act
    car=Car(color="red",max_speed=20,acceleration=5,tyre_friction=3)
    car._color="black"
    #assert
    assert car.color=="black"
    

#object creation with color
#object creation without color
#set current speed equal to zero when engine started first time

