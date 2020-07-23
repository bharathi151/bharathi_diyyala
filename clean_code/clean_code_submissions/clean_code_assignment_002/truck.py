from car import Car
class Truck(Car):
    _horn_sound = "Honk Honk"

    def __init__(self, max_speed, acceleration,
                 tyre_friction, max_cargo_weight, color=None):
        super().__init__(max_speed, acceleration, tyre_friction, color)
        is_value_raises_value_error(max_cargo_weight, "cargo_weight")
        self._max_cargo_weight, self._cargo_weight = max_cargo_weight, 0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    @property
    def cargo_weight(self):
        return self._cargo_weight

    def load(self, cargo_weight):
        is_value_raises_value_error(cargo_weight, "cargo_weight")
        if self._current_speed == 0:
            self._cargo_weight += cargo_weight
            self.is_cargo_weight_sufficient_to_load(cargo_weight)
        else: print("Cannot load cargo during motion")

    def unload(self, cargo_weight):
        is_value_raises_value_error(cargo_weight, "cargo_weight")
        if self._current_speed == 0:
            self._cargo_weight -= cargo_weight
            self.is_cargo_weight_sufficient_to_unload(cargo_weight)
        else:
            print("Cannot unload cargo during motion")

    def is_cargo_weight_sufficient_to_load(self, cargo_weight):
        if self._cargo_weight > self._max_cargo_weight:
            self._cargo_weight -= cargo_weight
            print_error_message_for_load(self._max_cargo_weight)

    def is_cargo_weight_sufficient_to_unload(self, cargo_weight):
        if self._cargo_weight < 0:
            self._cargo_weight += cargo_weight
            print_error_message_for_unload(self._max_cargo_weight)

def is_value_raises_value_error(value, name_of_the_value):
    if value <= 0:
        raise ValueError("Invalid value for " + name_of_the_value)

def print_error_message_for_load(max_weight):
    print("Cannot load cargo more than max limit:", max_weight)

def print_error_message_for_unload(max_weight):
    print("Cannot unload cargo more than max limit:", max_weight)
