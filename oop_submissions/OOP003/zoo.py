class Zoo:
    all_animals,no_of_deers,no_of_lions,no_of_sharks,no_of_gold_fish=0,0,0,0,0
    def __init__(self,animals=None):
        if animals is None or len(animals)<=0:self.animals=[]
        else:self.animals=animals
        self.count_animals=0
        self.breath=""
        self.reserved_food_in_kgs=0
    def add_food_to_reserve(self,food):
        self.reserved_food_in_kgs+=food
    def add_animal(self,animal):
        self.count_animals+=1
    def feed(self,animal):
        self.reserved_food_in_kgs-=animal.required_food_in_kgs
    def breathe(self):
        print(f'{self.breath}')
class Deer(Zoo):
    breath="Breathe in air"
    sound="Buck Buck"
    age_grow=1
    grow_food=2
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self.age_in_months=age_in_months
        self.breed=breed
        self.required_food_in_kgs=required_food_in_kgs
        type(self).all_animals+=1
        type(self).no_of_deers+=1
class Lion(Zoo):
    breath="Breathe in air"
    sound="Roar Roar"
    age_grow=1
    grow_food=4
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self.age_in_months=age_in_months
        self.breed=breed
        self.required_food_in_kgs=required_food_in_kgs
        type(self).all_animals+=1
        type(self).no_of_lions+=1
class Shark(Zoo):
    breath="Breathe oxygen from water"
    sound="Shark Sound"
    age_grow=1
    grow_food=8
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self.age_in_months=age_in_months
        self.breed=breed
        self.required_food_in_kgs=required_food_in_kgs
        type(self).all_animals+=1
        type(self).no_of_sharks+=1
class GoldFish(Zoo):
    breath="Breathe oxygen from water"
    sound="Hum Hum"
    age_grow=1
    grow_food=0.2
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        if age_in_months!=1:raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        if required_food_in_kgs<=0:raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self.age_in_months=age_in_months
        self.breed=breed
        self.required_food_in_kgs=required_food_in_kgs
        type(self).all_animals+=1
        type(self).no_of_gold_fish+=1
zoo=Zoo()
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
gold_fish.breathe()