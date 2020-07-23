def test_sound_horn_when_car_engine_is_not_started_return_warn(car,
                                                               capsys):
    # arrange
    false = False
    warn = "Start the engine to sound_horn\n"

    # act
    car.sound_horn()
    captured = capsys.readouterr()

    # assert
    assert car.is_engine_started == false
    assert captured.out == warn


def test_sound_horn_when_car_engine_is_started_returns_sound(car,
                                                             capsys):
    # arrange
    horn = "Beep Beep\n"
    true = True
    car.start_engine()

    # act
    car.sound_horn()
    captured = capsys.readouterr()

    # assert
    assert car.is_engine_started == true
    assert captured.out == horn
