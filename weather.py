from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Annapolis"):
    
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n**Get the current weather conditions**\n')

    city = input("\nEnter a city name please: ")

    #Checked for empty strings or a string with only spaces
    if not bool(city.strip()):
        city = "Annapolis"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)



