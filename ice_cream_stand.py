# Exercise 9-6 Ice Cream Stand
class Restaraunt:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cusine_type}")

    def set_number_served(self, number_served):
        number_served = self.number_served
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaraunt):
    def __init__(self, restaurant_name, cusine_type):
        #This initializes the attributes from the parent class.
        super().__init__(restaurant_name, cusine_type)
        
    def flavors(self):
        flavors = ['chocolate', 'vanilla', 'coffee', 'birthday cake', 'peppermint']
        for flavors in flavors:
            print(f"{flavors.title()}")


iceCreamStand = IceCreamStand("Joe's Ice Cream", "Ice Cream")
print(f"{iceCreamStand.describe_restaurant()} and has the following flavors: ")
iceCreamStand.flavors()