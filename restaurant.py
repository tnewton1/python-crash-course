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