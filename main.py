import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = '28b83cfcbf2c2c6495acf3762eabb84e'
CITY = "London"
url = BASE_URL + "appid=" + '28b83cfcbf2c2c6495acf3762eabb84e' + "&q=" + CITY
Kelvin = 273.15

response = requests.get(url).json()
sum = response['main']['temp'] - Kelvin
print('Weather in ', CITY, ' - ', sum, 'C')