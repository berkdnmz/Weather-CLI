import dotenv
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_data(city):
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"

    if not api_key:
        print("API key not found. Make sure your .env file is set up correctly.")
        return None
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print("Invalid city entered. Please try again.")
    except requests.exceptions.ConnectionError:
        print("There may be an issue with your internet connection.")
    except requests.exceptions.Timeout:
        print("Connection timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
    return None

def parse_data(data):
    try:
        city_name = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description'].capitalize()

        return {
            "city": city_name,
            "temperature": temperature,
            "feels_like": feels_like,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "description": description
        }

    except (KeyError, IndexError) as e:
        print(f"API data error: {e}")
        return None

def print_data(data):
    print("\n___________________________________")
    print(f"Weather for {data['city']}:")
    print(f"Temperature     : {data['temperature']}°C")
    print(f"Feels like      : {data['feels_like']}°C")
    print(f"Humidity        : %{data['humidity']}")
    print(f"Wind speed      : {data['wind_speed']} m/s")
    print(f"Description     : {data['description']}")
    print("___________________________________\n\n")

def convert_turkish_chars(text):
    translation_table = str.maketrans("çğıöüşÇĞİÖÜŞ", "cgiousCGIOUS")
    return text.translate(translation_table)

def ask_for_another_city():
    while True:
        answer = input("Do you want to check another city? (y/n): ")
        if not answer.isalpha() or answer.lower() not in ['y', 'n']:
            print("Invalid input, please enter only 'y' or 'n'.")
            continue

        if answer.lower() == 'n':
            return False
        else:
            return True

def weather_app():
    while True:
        user_input = input("Which city's weather do you want to check? ")
        city = convert_turkish_chars(user_input.strip().lower().capitalize())

        data = fetch_data(city)
        if not data:
            continue

        parsed = parse_data(data)
        if not parsed:
            continue

        print_data(parsed)

        if not ask_for_another_city():
            break

if __name__ == '__main__':
    weather_app()
