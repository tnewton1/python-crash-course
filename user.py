class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    def greet_user(self):
        print(f"Greetings of the day, {self.first_name}!")

user1 = User("Mike", "Roe Soft")
user2 = User("John", "Smith")
user3 = User("Ben", "Dover")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()