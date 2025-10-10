from city_functions import get_formatted_city_country

def test_city_country():
    """Does it work for names like 'Athens', 'Greece'"""
    formatted_city_country = get_formatted_city_country('Athens', 'Greece')
    assert formatted_city_country == 'Athens, Greece'

def test_city_country_population():
    """does it work for 'Athens', 'Greece' and 'population=8000000' """
    formatted_city_country_population = get_formatted_city_country('Athens', 'Greece', 8000000)
    assert formatted_city_country_population == 'Athens, Greece - population 8000000'