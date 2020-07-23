import math
class Car:
    _horn_sound="Beep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color=None):
        if max_speed<=0:raise ValueError("Invalid value for max_speed")
        if acceleration<=0:raise ValueError("Invalid value for acceleration")
        if tyre_friction<=0:raise ValueError("Invalid value for tyre_friction")
        self._color,self._max_speed,self._acceleration,self._tyre_friction=acceleration=color,max_speed,acceleration,tyre_friction
        self._is_engine_started,self._current_speed=False,0
    @property
    def current_speed(self):return self._current_speed
    @property
    def max_speed(self):return self._max_speed
    @property
    def is_engine_started(self):return self._is_engine_started
    @property
    def acceleration(self):return self._acceleration
    @property
    def tyre_friction(self):return self._tyre_friction
    @property
    def color(self):return self._color
    def start_engine(self):self._is_engine_started=True
    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started=False
    def accelerate(self):
        if self._is_engine_started:
            self._current_speed=self._current_speed+self._acceleration if (self._current_speed+self._acceleration)<=self._max_speed else self._max_speed
        else:print("Start the engine to accelerate")
    def apply_brakes(self):
        if (self._current_speed-self.tyre_friction)>=0:self._current_speed-=self._tyre_friction
        else:self._current_speed=0
    def sound_horn(self):
        if self._is_engine_started:print(f'{self._horn_sound}')
        else:print("Start the engine to sound_horn")
class Truck(Car):
    _horn_sound="Honk Honk"
    def __init__(self,max_speed,acceleration,tyre_friction,max_cargo_weight,color=None):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        if max_cargo_weight<=0:raise ValueError("Invalid value for cargo_weight")
        self._max_cargo_weight,self._cargo_weight=max_cargo_weight,0
    @property
    def max_cargo_weight(self):return self._max_cargo_weight
    def load(self,cargo_weight):
        if cargo_weight<=0:raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:
            if (self._cargo_weight+cargo_weight)<=self._max_cargo_weight:self._cargo_weight+=cargo_weight
            else:print("Cannot load cargo more than max limit:",self._max_cargo_weight)
        else:print("Cannot load cargo during motion")
    def unload(self,cargo_weight):
        if cargo_weight<=0:raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:
            if cargo_weight<=self._max_cargo_weight:
                if (self._cargo_weight-cargo_weight)>=0:self._cargo_weight-=cargo_weight
            else:print("Cannot unload cargo more than max limit:",self._max_cargo_weight)
        else:print("Cannot unload cargo during motion")
class RaceCar(Car):
    _horn_sound="Peep Peep\nBeep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color=None):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
    @property
    def nitro(self):return self._nitro
    def apply_brakes(self):
        if self._current_speed>=(self._max_speed//2):self._nitro+=10
        super().apply_brakes()
    def accelerate(self):
        super().accelerate()
        if self._nitro>0:
            if(self._current_speed+((self._acceleration*30)/100)<=self._max_speed):
                self._current_speed+=round(math.ceil((self._acceleration*30)/100))
            else:self._current_speed=self._max_speed
            self._nitro-=10