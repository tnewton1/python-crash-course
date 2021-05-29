class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f"First name: {self.first_name}, Last name: {self.last_name}")
    def greet_user(self):
        print(f"Greetings of the day, {self.first_name}!")

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


user1 = User("Mike", "Roe Soft")
user2 = User("John", "Smith")
user3 = User("Ben", "Dover")

admin1 = Admin("John", "Doe")

admin1.privileges.show_privileges()
admin1_privileges = [ 
    "can reset passwords",
    "can change usernames",
    "can delete user accounts"
]

admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()
