def city_country(city, country):
    city_and_country = f"{city}, {country}"
    return city_and_country.title()
    
c = city_country('paris', 'france')
print(c)