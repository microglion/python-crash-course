from car import Car

class Battery:
    #a simple attempt to model a battery for an electric car
    def __init__(self, battery_size=40):
        #initialise the battery's attributes
        self.battery_size = battery_size

    def describe_battery(self):
        #print statement describing the battery size
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        #print a statement about the range this battery provides
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 300

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    #represent aspects of a car, specific to electric vehicles
        def __init__(self, make, model, year):
         #initialise attributes of the parent class
            super().__init__(make, model, year)
            self.battery = Battery()


        def fill_gas_tank(self):
            #electric cars don't have gas tanks
            print("This car doesn't need a gas tank!")

if __name__ == "__main__":
    my_pogo = ElectricCar('honda', 'pogo', 2025)
    print(my_pogo.get_descriptive_name())
    my_pogo.battery.battery_size = 100
    my_pogo.battery.get_range()
    my_pogo.battery.upgrade_battery()
    my_pogo.battery.get_range()

