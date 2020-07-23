from truck import Truck


def test_accelerate_before_engine_starts_returns_error(truck, capsys):
    #arrange
    warn = "Start the engine to accelerate\n"
    zero = 0
    #act
    truck.accelerate()
    captured = capsys.readouterr()
    #assert
    assert captured.out == warn
    assert truck.cargo_weight == zero


def test_acceleration_when_engine_started_curent_speed_less_than_max_speed_returns_updated_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=10,
                  tyre_friction=3,
                  max_cargo_weight=40)
    updated_current_speed = 10
    truck.start_engine()
    true = True
    zero = 0

    #act
    truck.accelerate()

    #assert
    assert truck.is_engine_started == true
    assert truck.current_speed == updated_current_speed
    assert truck.cargo_weight == zero


def test_acceleration_when_current_speed_more_than_max_speed_return_max_speed_as_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=1,
                  tyre_friction=3,
                  max_cargo_weight=50)
    updated_current_speed = 20
    truck.start_engine()
    truck.accelerate()
    true = True
    zero = 0

    #act
    truck.accelerate()
    #assert
    assert truck.is_engine_started == true
    assert truck.current_speed == updated_current_speed
    assert truck.cargo_weight == zero


def test_accelerate_when_current_speed_equal_to_max_limit_returns_updated_current_speed():
    #arrange
    truck = Truck(color="red", max_speed=20,
                  acceleration=10,
                  tyre_friction=3,
                  max_cargo_weight=50)
    updated_current_speed = 20
    truck.start_engine()
    truck.accelerate()
    zero = 0
    true = True
    #act
    truck.accelerate()
    #assert
    assert truck.is_engine_started == true
    assert truck.current_speed == updated_current_speed
    assert truck.cargo_weight == zero
