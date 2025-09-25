from restaurant import Restaurant
class IceCreamStand(Restaurant):
    #model an ice cream stand, a specific kind of restaurant
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint chocolate chip', 'cookie dough', 'tin roof']

    def display_flavors(self):
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Carluto's")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
