import requests, json
error = "I dont know what the fuck happend but i dont know gang"
api_key = "78d8e4adff841676fb09849ffa7467a5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "indianapolis"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name+"&units=imperial"
def weather():

    response = requests.get(complete_url)
    things = []
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        city_name = x['name']
        current_temperature = y["temp"]
        feels_like = y['feels_like']
        min = y['temp_min']
        max = y['temp_max']
        z = x["weather"]
        weather_description = z[0]["description"]
        weatherDesc = city_name + ": \nTemperature = " + str(current_temperature) + "°F \nFeel Like: " + str(feels_like)+ "°F\nMinimum: " + str(min)+ "°F\nMax: " + str(max) + "°F\ndescription: " + str(weather_description)
        print(weatherDesc)
        things.append(weatherDesc)
        message = city_name + "'s current temperature is " + str(current_temperature) +"degrees," + " and feels like " + str(feels_like) + "degrees," + "with a minimum of " + str(min) + "degrees, " + "and a maximum of " + str(max) + "degrees," +  "and is being described to me as " + str(weather_description)
        things.append(message)
        return things
    else:
        print(" City Not Found ")
        return error
