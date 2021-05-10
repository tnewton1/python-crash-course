# Exercise 9-4 Number Served

class Restaraunt:
    def __init__(self, restaurant_name, cusine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is {self.cusine_type}")
        print(f"{self.restaurant_name} has served {self.number_served} customers.")
        print("-----------------------------------------------------------------------")

    def set_number_served(self):
        number_served = self.number_served

restaraunt = Restaraunt("McDonalds", "Fast Food", 100000)
restaraunt.describe_restaurant()

another_restaraunt = Restaraunt("Chilis", "Fake Mexican or TexMex")
another_restaraunt.describe_restaurant()