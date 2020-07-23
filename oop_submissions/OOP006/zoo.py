class Zoo:
    _breath,_sound,_list="","",[]
    def __init__(self):
        Zoo._list.append(self)
        self._deers,self._gold_fish,self._count=0,0,0
        self._reserved_food_in_kgs,self._age_grow,self._grow_food,self._age_in_months,self._required_food_in_kgs,self._breed=0,0,0,0,0,""
    def add_food_to_reserve(self,food):self._reserved_food_in_kgs+=food
    def add_animal(self,animal):
        self._count+=1
        if isinstance(animal,Deer):self._deers+=1
        if isinstance(animal,GoldFish):self._gold_fish+=1
    def feed(self,animal):
        if self._reserved_food_in_kgs-animal._required_food_in_kgs>=0:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
    def make_instance(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self._age_in_months,self._breed,self._required_food_in_kgs=age_in_months,breed,required_food_in_kgs
    @classmethod
    def breathe(cls):print(f'{cls._breath}')
    @classmethod
    def make_sound(cls):print(f'{cls._sound}')
    def grow(self):self._age_in_months,self._required_food_in_kgs=self.age_in_months+self._age_grow,self._required_food_in_kgs+self._grow_food
    def count_animals(self):return self._count
    @classmethod
    def count_animals_in_all_zoos(cls):
        _total=0
        for i in Zoo._list:_total+=i._count
        return(_total)
    @staticmethod
    def count_animals_in_given_zoos(list=None):
        _total=0
        for i in list:_total+=i._count
        return _total
    def hunt(self,other):
        if isinstance(self,Lion) or isinstance(self,Snake):
            if other._deers>=1:other._deers,other._count=other._deers-1,other._count-1
            else:print("No deers to hunt")
        elif isinstance(self,Shark):
            if other._gold_fish>=1:other._deers,other._count=other._deers-1,other._count-1
            else:print("No GoldFish to hunt")
    @property 
    def reserved_food_in_kgs(self):return self._reserved_food_in_kgs
    @property 
    def required_food_in_kgs(self):return self._required_food_in_kgs
    @property 
    def age_in_months(self):return self._age_in_months
    @property
    def breed(self):return self._breed
class Deer(Zoo):
    _breath,_sound,_age_grow,_grow_food="Breathe in air","Buck Buck",1,2
    def __init__(self,age_in_months, breed, required_food_in_kgs):self.make_instance(age_in_months, breed, required_food_in_kgs)
class Lion(Zoo):
    _breath,_sound,_age_grow,_grow_food="Breathe in air","Roar Roar",1,4
    def __init__(self,age_in_months, breed, required_food_in_kgs):self.make_instance(age_in_months, breed, required_food_in_kgs)
class Shark(Zoo):
    _breath,_sound,_age_grow,_grow_food="Breathe oxygen from water","Shark Sound",1,8
    def __init__(self,age_in_months, breed, required_food_in_kgs):self.make_instance(age_in_months, breed, required_food_in_kgs)
class GoldFish(Zoo):
    _breath,_sound,_age_grow,_grow_food="Breathe oxygen from water","Hum Hum",1,0.2
    def __init__(self,age_in_months, breed, required_food_in_kgs):self.make_instance(age_in_months, breed, required_food_in_kgs)
class Snake(Zoo):
    _breath,_sound,_age_grow,_grow_food="Breathe in air","Hiss Hiss",1,0.5
    def __init__(self,age_in_months, breed, required_food_in_kgs):self.make_instance(age_in_months, breed, required_food_in_kgs)
