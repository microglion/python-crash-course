def make_car(manufacturer, model, **car_info):
    """make a dictionary representing a car"""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('toyota', 'land cruiser', color='black', sun_roof=True, tow_package=True)
print(car)