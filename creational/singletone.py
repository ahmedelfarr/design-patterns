import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")