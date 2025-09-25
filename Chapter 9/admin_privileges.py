from user2 import User

class Admin(User):
    def __init__(self, first_name, last_name, sex, age):
        super().__init__(first_name, last_name, sex, age)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ("can add post", "can delete post", "can ban user")

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"- {privilege}")
if __name__ == "__main__":
    Admin1 = Admin("clark", "kent", "Male", 26 )
    Admin1.privileges.show_privileges()
