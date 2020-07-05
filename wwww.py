import pyowm

owm =  pyowm.OWM('36b4de2f395b6ffa741b15be214b74ae',language = "RU") # ключ+агрумент

place = input("В каком городе/стране?: ")
observation = owm.weather_at_place(place)
w = observation.get_weather()

print("В городе " + place + " сейчас " +
w.get_detailed_status())
temp = w.get_temperature('celsius')['temp']
print('Температура в районе: ' + str(temp) + '°C')