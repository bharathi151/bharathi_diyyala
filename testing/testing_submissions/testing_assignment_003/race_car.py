from car import Car
import math
class RaceCar(Car):
    _horn_sound="Peep Peep\nBeep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color=None):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
    @property
    def nitro(self):return self._nitro
    def apply_brakes(self):
        half_speed=self._max_speed//2
        if self._current_speed>half_speed:
            self._nitro+=10
        super().apply_brakes()
    def accelerate(self):
        super().accelerate()
        if self._is_engine_started:
            if self._nitro:                     
                self._current_speed+=round(math.ceil(self._acceleration*0.3))
                if self._current_speed>self._max_speed:
                    self._current_speed=self._max_speed
                self._nitro-=10
        