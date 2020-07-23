class Car:
    _horn_sound = "Beep Beep"

    def __init__(self, max_speed, acceleration, tyre_friction, color=None):
        is_valid_value(max_speed, "max_speed")
        is_valid_value(acceleration, "acceleration")
        is_valid_value(tyre_friction, "tyre_friction")
        self._color, self._max_speed = color, max_speed
        self._acceleration, self._tyre_friction = acceleration, tyre_friction
        self._is_engine_started = False
        self._current_speed = 0

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def is_engine_started(self):
        return self._is_engine_started

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def tyre_friction(self):
        return self._tyre_friction

    @property
    def color(self):
        return self._color

    def start_engine(self):
        self._is_engine_started = True

    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started = False

    def accelerate(self):
        if self._is_engine_started:
            self._current_speed = self._current_speed + self._acceleration
        else: print("Start the engine to accelerate")
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0

    def sound_horn(self):
        if self._is_engine_started:
            print(f'{self._horn_sound}')
        else:
            print("Start the engine to sound_horn")

def is_valid_value(value, name_of_the_value):
    if value <= 0:
        raise ValueError("Invalid value for " + name_of_the_value)
