from truck import Truck

def test_apply_breaks_before_engine_starts_zero_current_speed(truck):
    #arrange
    zero = 0
    false = False
    #act
    truck.apply_brakes()

    #assert
    assert truck.is_engine_started == false
    assert truck.current_speed == zero
    assert truck.cargo_weight == zero


def test_apply_brakes_when_tyre_friction_more_than_current_speed_return_updated_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=10,
                  tyre_friction=3,
                  max_cargo_weight=50)
    updated_current_speed = 0
    zero = 0
    true = True
    truck.start_engine()

    #act
    truck.apply_brakes()
    #assert
    assert truck.is_engine_started == true
    assert truck.current_speed == updated_current_speed
    assert truck.cargo_weight == zero


def test_apply_brakes_when_tyre_friction_less_than_current_speed_return_updated_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=10,
                  tyre_friction=3,
                  max_cargo_weight=50)
    updated_current_speed = 7
    truck.start_engine()
    truck.accelerate()
    zero = 0
    true = True

    #act
    truck.apply_brakes()
    #assert
    assert truck.is_engine_started == true
    assert truck.current_speed == updated_current_speed
    assert truck.cargo_weight == zero


def test_apply_brakes_when_tyre_friction_equal_current_speed_returns_zero_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=3,
                  tyre_friction=3,
                  max_cargo_weight=50)
    zero = 0
    truck.start_engine()
    truck.accelerate()
    #act
    truck.apply_brakes()
    #assert

    assert truck.current_speed == zero
    assert truck.cargo_weight == zero
