class Dog:
    #a simple attempt to model a dog

    def __init__(self, name, age):
        #initialise name and age attributes
        self.name = name
        self.age = age
    
    def sit(self):
        #simulate a dog sitting in response to a command
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        #simulate rolling over in response to a command
        print(f"{self.name} rolled over!")

my_dog = Dog('Cooper', 6)
my_2nd_dog = Dog('Wilbur', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.roll_over()
my_dog.sit()

print(f"My dog's name is {my_2nd_dog.name}.")
print(f"{my_2nd_dog.name} is {my_2nd_dog.age} years old.")
my_2nd_dog.roll_over()
my_2nd_dog.sit()