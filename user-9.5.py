class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0
    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    def greet_user(self):
        print(f"Greetings of the day, {self.first_name}!")
    def increment_login_attempts(self):
        self.login_attempt += 1
    def reset_login_attempts(self):
        self.login_attempt = 0


user1 = User("Mike", "Roe Soft")
user2 = User("John", "Smith")
user3 = User("Ben", "Dover")

user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.greet_user()
user2.greet_user()
user3.greet_user()

"""Login Attempts"""
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login Attempts: " + str(user1.login_attempt))
"""Reset the login attempts"""
print("Resetting login attempts of " + str(user1.first_name) + "!")
user1.reset_login_attempts()
print("Login Attempts: " + str(user1.login_attempt))
