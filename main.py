import pip._vendor.requests
s_city = "Moscow,RU"
appid = "4fc5422f978e3dc0e5f536c271be6056"
res = pip._vendor.requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
res = pip._vendor.requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print()
print("Прогноз погоды на неделю:")
print()
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <", i['wind']['speed'],
        "> \r\nВидимость <", i['visibility'],
        "> \r\nТемпература <",'{0:+3.0f}'.format(i['main']['temp']),
        "> \r\nПогодные условия <", i['weather'][0]['description'])
    print("____________________________")
    print()