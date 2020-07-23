class Zoo:
    _list=[]
    def __init__(self):
        Zoo._list.append(self)
        self._reserved_food_in_kgs,self._animals_count,self._animal=0,0,[]
   
    def add_animal(self,animal):
        self._animals_count+=1
        self._animal.append(animal)
        
    def feed(self,animal):
        if (self._reserved_food_in_kgs-animal._required_food_in_kgs)>=0:
            self._reserved_food_in_kgs-=animal._required_food_in_kgs
            animal.grow()
            
    def add_food_to_reserve(self,food):self._reserved_food_in_kgs+=food
    
    def count_animals(self):return self._animals_count
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        _total_animals=0
        for i in cls._list:_total_animals+=i._animals_count
        return _total_animals
        
    @staticmethod
    def count_animals_in_given_zoos(list=None):
        _total_animals=0
        for i in list:_total_animals+=i._animals_count
        return _total_animals
    
    @property
    def reserved_food_in_kgs(self):return self._reserved_food_in_kgs
    
class Animals:
    _age_grow,_food_grow,_breath,_sound=0,0,"",""
    def create_instance(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:
            raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self._age_in_months, self._breed, self._required_food_in_kgs=age_in_months, breed, required_food_in_kgs
    
    def grow(self):
        self._required_food_in_kgs+=self._food_grow
        self._age_in_months+=self._age_grow
        
    @classmethod
    def make_sound(cls):print(f"{cls._sound}")
    
    @classmethod
    def breathe(cls):print(f'{cls._breath}')
        
    @property
    def age_in_months(self):return self._age_in_months
    
    @property
    def breed(self):return self._breed
    
    @property
    def required_food_in_kgs(self):return self._required_food_in_kgs

class Land_hunter(Zoo,Animals):
    def hunt(self,zoo_name):
        _hunted_animal=-1
        if not(isinstance(self,Deer)):        
            for i in range(len(zoo_name._animal)):
                #print(zoo_name._animal[i])
                if isinstance(zoo_name._animal[i],Deer):
                    print("ok")
                    zoo_name._animals_count-=1
                    _hunted_animal=i
                    break
            if _hunted_animal==-1:print("No deers to hunt")
            else:zoo_name._animal.pop(_hunted_animal)
            
class Water_hunter(Zoo,Animals):
    def hunt(self,zoo_name):
        _hunted_animal=-1
        if not (isinstance(self,GoldFish)):
            for i in range(len(zoo_name._animal)):
                if isinstance(zoo_name._animal[i],GoldFish):
                    zoo_name._animals_count-=1
                    _hunted_animal=i
                    break
            if _hunted_animal==-1:print("No GoldFish to hunt")
            else:zoo_name._animal.pop(_hunted_animal)
        
class Land_animal(Land_hunter):_breath="Breathe in air"

class Water_animal(Water_hunter):_breath="Breathe oxygen from water"

class Deer(Land_animal):
    _age_grow,_food_grow,_sound=1,2,"Buck Buck"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.create_instance(age_in_months, breed, required_food_in_kgs)

class Lion(Land_animal):
    _age_grow,_food_grow,_sound=1,4,"Roar Roar"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.create_instance(age_in_months, breed, required_food_in_kgs)

class Shark(Water_animal):
    _age_grow,_food_grow,_sound=1,8,"Shark Sound"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.create_instance(age_in_months, breed, required_food_in_kgs)

class GoldFish(Water_animal):
    _age_grow,_food_grow,_sound=1,0.2,"Hum Hum"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.create_instance(age_in_months, breed, required_food_in_kgs)

class Snake(Land_animal):
    _age_grow,_food_grow,_sound=1,0.5,"Hiss Hiss"
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self.create_instance(age_in_months, breed, required_food_in_kgs)

# zoo = Zoo()
# print(zoo.reserved_food_in_kgs)
# zoo.add_food_to_reserve(10000000)
# print(zoo.reserved_food_in_kgs)
# print(zoo.count_animals())
# deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# zoo.add_animal(deer)
# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# zoo.add_animal(gold_fish)
# print(zoo.count_animals())
# zoo.feed(gold_fish)
# lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
# lion.breathe()
# zoo.add_animal(lion)
# lion.make_sound()
# lion.hunt(zoo)
# lion.hunt(zoo)
# print(zoo.reserved_food_in_kgs)
# print(gold_fish.age_in_months)
# shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
# zoo.add_animal(shark)
# shark.hunt(zoo)
# print(zoo.count_animals(),"ok")
# zoo1 = Zoo()
# print(zoo.count_animals_in_all_zoos())
# print(zoo1.reserved_food_in_kgs)
# zoo1.add_food_to_reserve(10000000)
# print(zoo1.reserved_food_in_kgs)
# print(zoo1.count_animals())
# gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
# zoo1.add_animal(gold_fish)
# print(zoo1.count_animals())
# zoo1.feed(gold_fish)
# print(zoo1.reserved_food_in_kgs)
# print(gold_fish.age_in_months)
# shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
# zoo1.add_animal(shark)
# shark.breathe()
# print(zoo1.count_animals(),"ok1")
# print(zoo.count_animals_in_given_zoos([zoo,zoo1]))
# print(zoo.count_animals_in_all_zoos())