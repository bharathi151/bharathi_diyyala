class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

def  get_string(peron_object):
    return  "{} is {} years old".format(peron_object.name, peron_object.age)

if  __name__  ==  "__main__":
    john =  Person("john", 25)
    david =  Person("david", 30)
    print(get_string(john))
    print(get_string(david))