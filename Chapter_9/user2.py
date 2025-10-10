class User:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.full_name = self.first_name.title() + " " + self.last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user\'s name is {self.first_name} {self.last_name}")
        print(f"They are {self.sex} and {self.age} years old.")

    def greet_user(self):
        print(f"Hello and welcome {self.full_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

