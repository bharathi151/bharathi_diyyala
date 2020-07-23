def test_sound_horn_when_truck_engine_is_not_started_return_warn(truck,
                                                                 capsys):
    # arrange
    warn = "Start the engine to sound_horn\n"
    false = False
    zero = 0
    # act
    truck.sound_horn()
    captured = capsys.readouterr()

    # assert
    assert truck.is_engine_started == false
    assert captured.out == warn
    assert truck.cargo_weight == zero


def test_sound_horn_when_truck_engine_is_started_returns_sound(truck,
                                                               capsys):
    # arrange
    horn = "Honk Honk\n"
    true = True
    zero = 0
    truck.start_engine()
    # act

    truck.sound_horn()
    captured = capsys.readouterr()
    # assert
    assert truck.is_engine_started == true
    assert captured.out == horn
    assert truck.cargo_weight == zero
