class chikenpizza():
    def __init__(self):
        self.name="chikenpizza"
class cheesepizza():
    def __init__(self):
        self.name="cheesepizza"

class meatpizza():
    def __init__(self):
        self.name="meatpizza"
class factory():
    @staticmethod
    def create_pizza(some_property):
        if some_property == "chiken":
            return chikenpizza
        if some_property == "cheese":
            return cheesepizza
        if some_property == "meat":
            return meatpizza
        
#the client 
PIZZA = factory.create_pizza("cheese")
print(PIZZA.__name__)



