# Exercise 9-4 Number Served
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


restaraunt = Restaraunt("McDonalds", "Fast Food")
restaraunt.describe_restaurant()
restaraunt.number_served = 9924
print(f"\nNumber Served: {restaraunt.number_served}")

restaraunt.set_number_served(18294)
print("\nNumber Served: " + str(restaraunt.number_served))

restaraunt.increment_number_served(2456)
print("Number Served: " + str(restaraunt.number_served))

another_restaraunt = Restaraunt("Chilis", "Fake Mexican or TexMex")
another_restaraunt.describe_restaurant()