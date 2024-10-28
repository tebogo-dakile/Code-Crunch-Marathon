import requests

API_KEY = 
BASE_URL = 

"""
Weather Codes:

200-232: Thunderstorms
300-321: Drizzle
500-531: Rain 
600-622: Snow
701-781: Atmosphere (e.g mist, smoke)
800: Clear skies
801-804: Clouds
"""
city_name = #city name#
response = requests.get() 

if 500 <= weather_code <= 531:
    print(f"It's raining in {city_name}")


    