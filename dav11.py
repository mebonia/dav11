import requests
import json
import sqlite3
api_key = "07fcb62a845efeb6eca154031ff40838"
response = requests.get("https://openweathermap.org/api/one-call-3")
status_code = response.status_code
headers = response.headers
content = response.text
def get_weather_data(city):

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    else:
        return 'error'

city = "Tbilisi"

print('statuse code:',response.status_code)
print('text',response.text)
print('header',response.headers)


weather_data = get_weather_data(city)

print("ამინდის მონაცემები, ქალაქი:", city)
print("ტემპერატურა:", weather_data["main"]["temp"], "°C")
print("ტენიანობა:", weather_data["main"]["humidity"], "%")

with open("weather_data.json", "w") as i:
    json.dump(weather_data, i, indent=4)




conn = sqlite3.connect("weatherr.sqlite3")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE  weather
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature varchar(30),
    humidity INTEGER
    );
""")


cursor.execute("""
INSERT INTO weather (city, temperature, humidity)
VALUES (?, ?, ?)
""", (city, weather_data["main"]["temp"], weather_data["main"]["humidity"]))

conn.commit()
conn.close()

#კოდი ემსახურება საიტიდან  კონკრეტული ქალაქის ამინდის ინფორმაციის წამოღებას ეკრანზე დაპრინტვას და შემდეგ სქლტ ბაზაში ატვირთვას ასევე json მონაცემის ინფორმაციის შენახვას.
