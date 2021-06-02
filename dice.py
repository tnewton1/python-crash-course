# Exercise 9-13

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
        

die1 = Die()

results = []

for roll_num in range(10):
    result = die1.roll_die()
    results.append(result)
print("10 rolls for a 6 sided die:")
print(results)