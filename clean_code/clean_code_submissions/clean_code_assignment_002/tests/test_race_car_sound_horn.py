def test_sound_horn_when_car_engine_is_not_started_return_warn(race_car, capsys):
    #arrange
    warn = "Start the engine to sound_horn\n"
    false = False
    #act
    race_car.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert race_car.is_engine_started == false
    assert captured.oout == warn


def test_sound_horn_when_car_engine_is_started_returns_sound(capsys, race_car):
    #arrange
    horn = "Peep Peep\nBeep Beep\n"
    race_car.start_engine()
    true = True
    #act
    race_car.sound_horn()
    captured = capsys.readouterr()
    #assert
    assert race_car.is_engine_started == true
    assert captured.out == horn
