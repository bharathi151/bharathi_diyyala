from car import Car

class Truck(Car):
    _horn_sound = "Honk Honk"
    def __init__(self, max_speed, acceleration, tyre_friction, max_cargo_weight, color=None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        value_error(max_cargo_weight, "cargo_weight")
        self._max_cargo_weight, self._cargo_weight = max_cargo_weight, 0
    @property
    def max_cargo_weight(self): return self._max_cargo_weight
    @property
    def cargo_weight(self): return self._cargo_weight
    def load(self, cargo_weight):
        value_error(cargo_weight, "cargo_weight")
        if self._current_speed == 0:
            self._cargo_weight += cargo_weight
            if self._cargo_weight > self._max_cargo_weight:
                self._cargo_weight -= cargo_weight
                print("Cannot load cargo more than max limit:", self._max_cargo_weight)
        else: print("Cannot load cargo during motion")
    def unload(self, cargo_weight):
        value_error(cargo_weight, "cargo_weight")
        if self._current_speed == 0:
            self._cargo_weight -= cargo_weight
            if self._cargo_weight < 0: 
                self._cargo_weight += cargo_weight
            else:
                print("Cannot unload cargo more than max limit:", self._max_cargo_weight)
        else:
            print("Cannot unload cargo during motion")
def value_error(value, string):
    if value <= 0:
        raise ValueError("Invalid value for " + string)   