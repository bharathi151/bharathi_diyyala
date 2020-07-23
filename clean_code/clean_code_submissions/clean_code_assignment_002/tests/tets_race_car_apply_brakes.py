from race_car import RaceCar


def test_apply_breaks_before_engine_starts_zero_current_speed(race_car):
    #arrange
    false = False
    zero = 0
    #act
    race_car.apply_brakes()
    #assert
    assert race_car.is_engine_started == false
    assert race_car.current_speed == zero
    assert race_car.nitro == zero


def test_apply_breaks_after_engine_starts_return_updated_current_speed():
    #arrange
    race_car = RaceCar(color="red", max_speed=20,
                       acceleration=2,
                       tyre_friction=3)
    updated_current_speed = 0
    zero = 0
    true = True
    race_car.start_engine()
    race_car.accelerate()
    #act
    race_car.apply_brakes()
    #assert
    assert race_car.is_engine_started == true
    assert race_car.current_speed == updated_current_speed
    assert race_car.nitro == zero


def test_apply_brakes_when_current_speed_more_than_or_equl_to_half_max_speed_returns_updated_nitro():
    #arrange
    car = RaceCar(color="red", max_speed=2,
                  acceleration=2,
                  tyre_friction=3)
    updated_current_speed = 0
    car.start_engine()
    car.accelerate()
    incresed_nitro = 10
    true = True
    #act
    car.apply_brakes()
    #assert
    assert car.nitro == incresed_nitro
    assert car.is_engine_started == true
    assert car.current_speed == updated_current_speed


def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed(race_car_obj):
    #arrange
    updated_current_speed = 0
    zero = 0
    true = True
    race_car_obj.start_engine()
    #act
    race_car_obj.apply_brakes()
    #assert
    assert race_car_obj.is_engine_started == true
    assert race_car_obj.current_speed == updated_current_speed
    assert race_car_obj.nitro == zero


def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed(race_car_obj):
    #arrange
    updated_current_speed = 7
    race_car_obj.start_engine()
    race_car_obj.accelerate()
    true = True
    zero = 0
    #act
    race_car_obj.apply_brakes()
    #assert
    assert race_car_obj.is_engine_started == true
    assert race_car_obj.current_speed == updated_current_speed
    assert race_car_obj.nitro == zero


def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed(race_car_obj):
    #arrange
    zero = 0
    true = True
    race_car_obj.start_engine()
    race_car_obj.accelerate()
    #act
    race_car_obj.apply_brakes()
    #assert
    assert race_car_obj.is_engine_started == true
    assert race_car_obj.current_speed == zero
