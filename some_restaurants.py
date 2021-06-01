# Exercise 9-10
from restaurant import Restaraunt

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