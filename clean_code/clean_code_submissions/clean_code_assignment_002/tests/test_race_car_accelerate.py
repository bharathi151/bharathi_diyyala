from race_car import RaceCar


def test_accelerate_before_engine_starts_returns_error(race_car, capsys):
    #arrange
    warn = "Start the engine to accelerate\n"
    false = False
    #act
    race_car.accelerate()
    captured = capsys.readouterr()
    #assert
    assert race_car.is_engine_started == false
    assert captured.out == warn


def test_acceleration_when_curent_speed_less_than_max_speed_returns_updated_current_speed(race_car_obj):
    #arrange
    updated_current_speed = 10
    true = True
    zero = 0
    race_car_obj.start_engine()
    #act
    race_car_obj.accelerate()
    #assert
    assert race_car_obj.is_engine_started == true
    assert race_car_obj.current_speed == updated_current_speed
    assert race_car_obj.nitro == zero

    
def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed():
    #arrange
    car = RaceCar(color="red", max_speed=20, acceleration=11, tyre_friction=3)
    true = True
    updated_current_speed = 20
    car.start_engine()
    car.accelerate()
    zero = 0
    #act
    car.accelerate()
    #assert
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed
    assert car.nitro == zero


def test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed(race_car_obj):
    #arrange
    updated_current_speed = 20
    race_car_obj.start_engine()
    race_car_obj.accelerate()
    true = True
    zero = 0
    #act
    race_car_obj.accelerate()
    #assert
    assert race_car_obj.is_engine_started == true
    assert race_car_obj.current_speed == updated_current_speed
    assert race_car_obj.nitro == zero


def test_acclelerate_when_nitro_present_returns_extra_acceleration_less_than_max_speed():
    #arrange
    car = RaceCar(color="red", max_speed=15, acceleration=3, tyre_friction=2)
    updated_current_speed = 11
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.apply_brakes()
    nitro = car.nitro
    nitro_value_at_half_speed = 10
    true = True
    zero = 0
    #act
    car.accelerate()
    #assert
    assert nitro >= nitro_value_at_half_speed
    assert car.nitro == zero
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_acclelerate_when_nitro_present_returns_extra_acceleration_more_than_max_speed():
    #arrange
    car = RaceCar(color="red", max_speed=15, acceleration=7, tyre_friction=2)
    updated_current_speed = 15
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.apply_brakes()
    nitro = car.nitro
    true = True
    nitro_value_at_half_speed = 10
    zero = 0
    #act
    car.accelerate()
    #assert
    assert nitro >= nitro_value_at_half_speed
    assert car.nitro == zero
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed
