import pytest
@pytest.fixture
def car():
    from car import Car 
    car_obj = Car(color="Red", max_speed=1, acceleration=1, tyre_friction=1)
    return car_obj


@pytest.fixture
def truck():
    from truck import Truck
    truck_obj = Truck(color="red",
                              max_speed=2,
                              acceleration=1,
                              tyre_friction=1,
                              max_cargo_weight=1)
    return truck_obj
    
    
@pytest.fixture
def truck_obj():
    from truck import Truck
    truck_obj = Truck(color="red",
                              max_speed=20,
                              acceleration=4,
                              tyre_friction=3,
                              max_cargo_weight=50)
    return truck_obj


@pytest.fixture
def race_car():
    from race_car import RaceCar
    race_car_obj = RaceCar(color="red",
                              max_speed=2,
                              acceleration=1,
                              tyre_friction=1)
    return truck_obj

@pytest.fixture
def race_car_obj():
    from race_car import RaceCar
    race_car_obj = RaceCar(color="red",
                              max_speed=20,
                              acceleration=10,
                              tyre_friction=3)
    return truck_obj