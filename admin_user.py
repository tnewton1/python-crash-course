# Exercise 9-11

from admin import Admin

admin1 = Admin("John", "Doe")

admin1.privileges.show_privileges()
admin1_privileges = [ 
    "can reset passwords",
    "can change usernames",
    "can delete user accounts"
]

admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()