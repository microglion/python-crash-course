class User:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.full_name = self.first_name.title()  + " " + self.last_name.title()
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

if __name__ == "__main__":
    user1 = User('Maddie', 'Cunningham', 'Female', 28)
    user2 = User('Tom', 'Cruise', 'Male', 63)
    user3 = User('Peter', 'Parker', 'Male', 25)
    user4 = User('Ru', 'Paul', 'Transgender Woman', 39)

    user1.describe_user()
    user1.greet_user()
    user2.describe_user()
    user2.greet_user()
    user3.describe_user()
    user3.greet_user()
    user4.describe_user()
    user4.greet_user()
    user4.increment_login_attempts()
    user4.increment_login_attempts()
    user4.increment_login_attempts()
    user4.increment_login_attempts()
    print(f"{user4.login_attempts} login attempts.")
    user4.reset_login_attempts()
    print(f"{user4.login_attempts} login attempts.")


