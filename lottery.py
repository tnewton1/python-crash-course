# Exercise 9-14
from random import choice
lotto_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []

lotto_ball = choice(lotto_choice)

""" while len(winning_ticket) < 4:
    lotto_ball = choice(lotto_choice)
    if lotto_ball not in lotto_choice:
        print(f" - Ball: {lotto_ball}")
        winning_ticket.append(lotto_ball) """

# print(f"Winning Ticket: {winning_ticket}")

print(f"{lotto_ball}")