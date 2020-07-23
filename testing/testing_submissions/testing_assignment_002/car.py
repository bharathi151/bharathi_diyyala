class Car:
    _horn_sound="Beep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color=None):
        
        
        error(max_speed,"max_speed")
        error(acceleration,"acceleration")
        error(tyre_friction,"tyre_friction")
        self._color,self._max_speed,self._acceleration,self._tyre_friction=color,max_speed,acceleration,tyre_friction
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
            self._current_speed=self._current_speed+self._acceleration 
            
            if self._current_speed>self._max_speed:
                self._current_speed=self._max_speed
        else:print("Start the engine to accelerate")
    def apply_brakes(self):
        
        eligible_speed=self._current_speed>=self._tyre_friction
        
        if eligible_speed:
            self._current_speed-=self._tyre_friction
        else:
            self._current_speed=0
    def sound_horn(self):
        if self._is_engine_started:print(f'{self._horn_sound}')
        else:print("Start the engine to sound_horn")
        
def error(value,string):
    zero=0
    if value<=zero:raise ValueError("Invalid value for "+string)   
