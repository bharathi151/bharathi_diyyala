
from car import Car
from truck import Truck

import pytest
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",-100,10,3,50),("red",0,10,3,50)
])

def test_object_creation_with_invalid_max_speed_raise_value_error(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    error="Invalid value for max_speed"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #assert
    assert max_speed<=0
    assert str(e.value)==error
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,-10,3,50),("red",100,0,3,50)
])
    
def test_object_creation_with_invalid_acceleration_raise_value_error(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    error="Invalid value for acceleration"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #assert
    assert acceleration<=0
    assert str(e.value)==error
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,-3,50),("red",100,10,0,50)
])

def test_object_creation_with_invalid_tyre_friction_raise_value_error(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    error="Invalid value for tyre_friction"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #assert
    assert tyre_friction<=0
    assert str(e.value)==error 
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,3,-5),("red",100,10,3,0)
])
    
def test_object_creation_with_invalid_cargo_weight_raise_value_error(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    error="Invalid value for cargo_weight"
    #act
    with pytest.raises(ValueError) as e: # Asserting the exception
        assert Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #assert
    assert max_cargo_weight<=0
    assert str(e.value)==error  
    
    
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",2,1,1,1)
])

    
def test_object_creation_with_valid_details_rerurn_truck_object(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange 
    
    #act
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    #assert
    assert isinstance(truck,Truck)
    assert truck.max_speed==max_speed
    assert truck.tyre_friction==tyre_friction
    assert truck.acceleration==acceleration
    assert truck.is_engine_started==False
    assert truck.current_speed==0
    assert truck.max_cargo_weight==max_cargo_weight
    assert truck.max_speed>truck.acceleration
    assert truck.max_speed>truck.current_speed
    assert truck.cargo_weight==0
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",2,1,1,1),("red",2,1,1,1)
])

    
def test_multiple_objects_creation_with_valid_details_return_truck_objects(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange 
    
    #act
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    #assert
    assert isinstance(truck,Truck)
    assert truck.max_speed==max_speed
    assert truck.tyre_friction==tyre_friction
    assert truck.acceleration==acceleration
    assert truck.is_engine_started==False
    assert truck.current_speed==0
    assert truck.max_cargo_weight==max_cargo_weight
    assert truck.max_speed>truck.acceleration
    assert truck.max_speed>truck.current_speed
    assert truck.cargo_weight==0

@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",2,1,1,1)
])
  
def test_start_engine_first_time_returns_is_engine_true(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #act
    truck.start_engine()
    #assert 
    assert truck.is_engine_started==True
    assert truck.cargo_weight==0
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,3,50)
])
def test_current_speed_when_start_engine_called_twice_return_is_engine_started_true(color,max_speed,acceleration,tyre_friction,max_cargo_weight):
    #arrange
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    #act
    truck.start_engine()
    truck.start_engine()
    #assert 
    assert truck.is_engine_started==True
    assert truck.cargo_weight==0
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,3,50)
])
def test_sound_horn_when_truck_engine_is_not_started_return_warn(color,max_speed,acceleration,tyre_friction,max_cargo_weight,capsys):
    #arrange
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    warn="Start the engine to sound_horn\n"
    #act
    truck.sound_horn()
    captured = capsys.readouterr()
    
    #assert
    assert truck.is_engine_started==False
    assert captured.out==warn
    assert truck.cargo_weight==0
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,3,50)
])
def test_sound_horn_when_truck_engine_is_started_returns_sound(color,max_speed,acceleration,tyre_friction,max_cargo_weight,capsys):
    #arrange
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    horn="Honk Honk\n"
    truck.start_engine()
    #act
    
    truck.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert truck.is_engine_started==True
    assert captured.out==horn
    assert truck.cargo_weight==0
    
@pytest.mark.parametrize("color,max_speed, acceleration, tyre_friction,max_cargo_weight", [
    ("red",100,10,3,50)
])   
def test_accelerate_before_engine_starts_returns_error(color,max_speed,acceleration,tyre_friction,max_cargo_weight,capsys):
    #arrange
    truck= Truck(color=color, max_speed=max_speed, acceleration=acceleration, tyre_friction=tyre_friction,max_cargo_weight=max_cargo_weight)
    
    warn="Start the engine to accelerate\n"
    #act
    truck.accelerate()
    captured = capsys.readouterr()
    #assert
    assert captured.out==warn
    assert truck.cargo_weight==0

def test_stop_engine_when_truck_is_not_running_returns_is_engine_started_false():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=3,tyre_friction=10,max_cargo_weight=50)
    #act
    truck.stop_engine()
    
    #assert
    assert truck.is_engine_started==False
    assert truck.cargo_weight==0
    
    
def test_stop_engine_when_truck_is_running_returns_is_engine_started_false():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=3,tyre_friction=10,max_cargo_weight=50)
    truck.start_engine()
    
    #act
    
    
    truck.stop_engine()
    
    #assert
    assert truck.is_engine_started==False
    assert truck.cargo_weight==0
   
    



def test_apply_breaks_before_engine_starts_zero_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=3,tyre_friction=10,max_cargo_weight=50)
    zero_current_speed=0
    #act
    truck.apply_brakes()
    
    #assert
    assert truck.is_engine_started==False
    assert truck.current_speed==zero_current_speed
    assert truck.cargo_weight==0

    
def test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=10,tyre_friction=3,max_cargo_weight=50)
    updated_current_speed=10
    truck.start_engine()
    
    #act
    
    truck.accelerate()
    
    #assert
    assert truck.is_engine_started==True
    assert truck.current_speed==updated_current_speed
    assert truck.cargo_weight==0
    
    
def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=11,tyre_friction=3,max_cargo_weight=50)
    updated_current_speed=20
    truck.start_engine()
    truck.accelerate()
    
    #act
    
    truck.accelerate()
    #assert
    assert truck.is_engine_started==True
    assert truck.current_speed==updated_current_speed
    assert truck.cargo_weight==0
    
    
    

def test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=10,tyre_friction=3,max_cargo_weight=50)
    updated_current_speed=20
    truck.start_engine()
    truck.accelerate()
    speed_at_accelerate=truck.current_speed
    #act
    
    truck.accelerate()
    #assert
    assert truck.is_engine_started==True
    assert truck.current_speed==updated_current_speed
    assert truck.cargo_weight==0



def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=10,tyre_friction=3,max_cargo_weight=50)
    updated_current_speed=0
    truck.start_engine()
    
    #act
    
    truck.apply_brakes()
    #assert
    assert truck.is_engine_started==True
    assert truck.current_speed==updated_current_speed
    assert truck.cargo_weight==0
    
    
def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=10,tyre_friction=3,max_cargo_weight=50)
    updated_current_speed=7
    truck.start_engine()
    truck.accelerate()

    #act
    
    truck.apply_brakes()
    #assert
    assert truck.is_engine_started==True
    assert truck.current_speed==updated_current_speed
    assert truck.cargo_weight==0    
    
    
def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=3,tyre_friction=3,max_cargo_weight=50)
    zero_current_speed=0
    truck.start_engine()
    truck.accelerate()
    #act

    truck.apply_brakes()
    #assert
    
    assert truck.current_speed==zero_current_speed  
    assert truck.cargo_weight==0    
    
def test_load_when_truck_is_in_motion_raises_warn(capsys):
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.load(30)
    truck.start_engine()
    truck.accelerate()
    warn="Cannot load cargo during motion\n"
    #act
    
    truck.load(20)
    captured = capsys.readouterr()
    #assert
    
    assert truck.current_speed>0
    assert captured.out==warn
    assert truck.cargo_weight<=truck.max_cargo_weight
    assert truck.cargo_weight==30
    
def test_load_when_load_is_more_than_max_limit_raises_warn(capsys):
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.start_engine()
    warn="Cannot load cargo more than max limit: 50\n"
    load=70
    #act
    
    truck.load(load)
    captured = capsys.readouterr()
    #assert
    assert truck.current_speed==0
    assert captured.out==warn
    assert load>=truck.max_cargo_weight
    assert truck.cargo_weight==0

def test_load_when_truck_is_not_motion_returns_loaded_weight(capsys):
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.start_engine()
    
    
    #act
    
    truck.load(50)
    
    #assert
    
    assert truck.current_speed==0
    assert truck.cargo_weight<=truck.max_cargo_weight
    assert truck.cargo_weight==50
  
  
  
def test_unload_when_truck_is_in_motion_raises_warn(capsys):
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.load(50)
    truck.start_engine()
    truck.accelerate()
    warn="Cannot unload cargo during motion\n"
    #act
    
    truck.unload(20)
    captured = capsys.readouterr()
    #assert
    
    assert truck.current_speed>0
    assert captured.out==warn
    assert truck.cargo_weight<=truck.max_cargo_weight
    assert truck.cargo_weight==50
    
def test_unload_when_load_is_more_than_max_limit_raises_warn(capsys):
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.start_engine()
    warn="Cannot unload cargo more than max limit: 50\n"
    truck.load(50)
    load=70
    #act
    
    truck.unload(load)
    captured = capsys.readouterr()
    #assert


    assert captured.out==warn
    assert load>=truck.max_cargo_weight
    
    assert truck.cargo_weight==50

def test_unload_total_load_when_truck_is_not_motion_returns_remaining_load_weight():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.start_engine()
    truck.load(50)
    load=50
    #act
    
    truck.unload(load)
    
    #assert
    
    assert truck.current_speed==0
    assert truck.cargo_weight<=truck.max_cargo_weight
    assert truck.cargo_weight==0
    assert load<=truck.max_cargo_weight
def test_unload_when_truck_is_not_motion_returns_remaining_load_weight():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=4,tyre_friction=3,max_cargo_weight=50)
    truck.start_engine()
    truck.load(50)
    load=40
    #act
    
    truck.unload(load)
    
    #assert
    
    assert truck.current_speed==0
    assert truck.cargo_weight<=truck.max_cargo_weight
    assert truck.cargo_weight==10
    assert load<=truck.max_cargo_weight
  
def test_color_encaspulation_returns_updated_color():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    new_color="blue"
    #act
    truck._color=new_color
    #assert
    assert truck.color==new_color
    
def test_current_speed_encaspulation_returns_updated_current_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    new_speed=10
    #act
    truck._color=new_speed
    #assert
    assert truck.color==new_speed
    

def test_tyre_friction_encaspulation_returns_updated_tyre_friction():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    new_tyre_friction=4
    #act
    truck._tyre_friction=new_tyre_friction
    #assert
    assert truck.tyre_friction==new_tyre_friction
    
def test_max_speed_encaspulation_returns_updated_max_speed():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    max_speed=30
    #act
    truck._max_speed=max_speed
    #assert
    assert truck.max_speed==max_speed
    
def test_acceleraton_encaspulation_returns_updated_acceleration():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    new_acceleration=5
    #act
    truck._acceleration=new_acceleration
    #assert
    assert truck.acceleration==new_acceleration
    
def test_max_cargo_weight_encaspulation_returns_updated_max_cargo_weight():
    #arrange
    from car import Car
    from truck import Truck
    truck=Truck(color="red",max_speed=20,acceleration=5,tyre_friction=3,max_cargo_weight=50)
    new_weight=5
    #act
    truck._max_cargo_weight=new_weight
    #assert
    assert truck.max_cargo_weight==new_weight

