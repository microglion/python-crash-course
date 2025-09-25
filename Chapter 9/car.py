"""A class that can be used to represent a car"""

class Car:
    #simple attempt to represent a car

    def __init__(self, make, model, year):
        #initialise attributes to describe a car

        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 24


    def get_descriptive_name(self):
        #return neatly formatted descriptive name
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        #print statement showing the car's mileage
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        #set the odometer reading to the given value
        #reject change if it attempts to roll back the odometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        #add the given amount to the odometer reading
        self.odometer_reading += miles



if __name__ == "__main__":
    my_used_car = Car('subaru', 'outback', 2019)
    print(my_used_car.get_descriptive_name())

    my_used_car.update_odometer(23_500)
    my_used_car.read_odometer()

    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()