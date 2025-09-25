print(f"In restaurant.py, __name__ is: {__name__}")

class Restaurant:
    #model different restaurants
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Method running in file where __name__ = {__name__}")
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")
       
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, numCustomers):
        if numCustomers >=self.number_served:
            self.number_served = numCustomers
            print(f"{self.restaurant_name} has served {self.number_served} customers.")      

    def increment_number_served(self, newCustomersToday):
        if newCustomersToday > 0:
            self.number_served += newCustomersToday
            print(f"{self.restaurant_name} has served {newCustomersToday} new customers today, and has served {self.number_served} customers in total.")
        elif newCustomersToday == 0:
            print(f"There were no new customers today. {self.restaurant_name} has served {self.number_served} customers in total.")
        else: #catches negative numbers
            print(f"Cannot have negative customers!")

if __name__ == "__main__":
    restaurant = Restaurant('Vincenco\'s', 'Italian')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant2 = Restaurant('Nando\'s', 'Portuguese Chicken')
    restaurant3 = Restaurant('Byron', 'Premium Burger')
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()
    restaurant3.set_number_served(23)
    restaurant3.increment_number_served(0)

