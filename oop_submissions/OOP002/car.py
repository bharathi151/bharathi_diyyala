import math
class Car:
    _horn="Beep Beep"
    def __init__(self,max_speed, acceleration, tyre_friction,color=None):
        if max_speed<0:
            raise ValueError("Invalid value for max_speed")
        if acceleration<0:
            raise ValueError("Invalid value for acceleration")
        if tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
        
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._is_engine_started=False
        self._current_speed=0
        self._max_speed=max_speed
    def start_engine(self):
        if self._is_engine_started==False:
            self._is_engine_started=True
    def accelerate(self):
        if self._is_engine_started==False:
            print("Start the engine to accelerate")
        elif (self._current_speed+self._acceleration)<=self._max_speed:
            self._current_speed+=self._acceleration
        elif (self._current_speed+self._acceleration)>self._max_speed:
            self._current_speed=self._max_speed
    @property
    def color(self):
        return self._color
    @property
    def current_speed(self):
        return self._current_speed
    @property
    def acceleration(self):
        return self._acceleration
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def tyre_friction(self):
        return self._tyre_friction
    def stop_engine(self):
        if self._is_engine_started==True:
            self._is_engine_started=False
    def sound_horn(self):
        if self._is_engine_started==True:
            print(f'{self._horn}')
        else:
            print("Start the engine to sound_horn")
    def apply_brakes(self):
        if (self._current_speed-self._tyre_friction)>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    

class Truck(Car):
    _horn="Honk Honk"
    def __init__(self, max_speed, acceleration, tyre_friction, max_cargo_weight,color=None):
        super().__init__( max_speed, acceleration, tyre_friction,color=None)
        if max_cargo_weight<0:
            raise ValueError("Invalid value for max_cargo_weight")

        self._max_cargo_weight=max_cargo_weight
        self._load=0
    def load(self,load):
        if self._current_speed!=0:
            print("Cannot load cargo during motion")
        elif self._current_speed==0:
            if load>=0:
                if (self._load+load)<self._max_cargo_weight:
                    self._load+=load
                else:
                    print(f"Cannot load cargo more than max limit: {self._max_cargo_weight}")
            else:
                raise ValueError("Invalid value for cargo_weight")

    def unload(self,load):
        if self._current_speed!=0:
            print("Cannot unload cargo during motion")
        elif self._current_speed==0:
            if load>=0:
                if (self._load-load)>=load:
                    self._load-=load
                else:
                    self._load=0
            else:
                raise ValueError("Invalid value for cargo_weight")
                
class RaceCar(Car):
    _horn="Peep Peep\nBeep Beep"
    def __init__(self, max_speed, acceleration, tyre_friction,color=None):
        super().__init__( max_speed, acceleration, tyre_friction,color=None)
        self._nitro=0
    def apply_brakes(self):
        #super().apply_brakes()
        if (self._current_speed)>=(self._max_speed//2):
            self._current_speed-=self._tyre_friction
            self._nitro+=10
        elif (self._current_speed-self._tyre_friction)>=self._tyre_friction:
            self._current_speed-=self._tyre_friction
    def accelerate(self):
        if self._is_engine_started==False:
            print("Start the engine to accelerate")
        elif self._nitro>0:
            if (self._current_speed+(self._acceleration+math.ceil((self._acceleration*30)/100)))<=self._max_speed:
                self._current_speed+=(self._acceleration+math.ceil((self._acceleration*30)/100))
            elif self._current_speed+(self._acceleration+math.ceil((self._acceleration*30)/100))>self._max_speed:  
                self._current_speed=self._max_speed
            self._nitro-=10
        elif (self._current_speed+self._acceleration)<=self._max_speed:
            self._current_speed+=self._acceleration
        elif (self._current_speed+self._acceleration)>self._max_speed:
            self._current_speed=self._max_speed
    @property
    def nitro(self):
        return self._nitro
        
