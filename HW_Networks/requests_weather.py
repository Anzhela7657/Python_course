'''2. Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію,
по цій локації повернеться погода, вологість і тд) https://openweathermap.org'''

import requests

city_name = input("Enter your city: ")
link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=afe30ddf220e794aa31309a24702b1ec"
req = requests.get(link)

match req.status_code:
  case 200:
   data = req.json()
   weather = data['weather'][0]['description']
   pressure = data ['main']['pressure']
   temp_min = data['main']['temp_min']
   temp_max = data['main']['temp_max']
   humidity = data['main']['humidity']
   wind_speed = data['wind']['speed']
   print(f"The weather in {city_name}\nThe weather conditions: {weather}\nThe temperature between {temp_min}-{temp_max}\nThe humidity: {humidity}%\nThe pressure: {pressure}hPa\nThe wind speed: {wind_speed} m/s")
  case _:
    print(f"Error {req.status_code}")