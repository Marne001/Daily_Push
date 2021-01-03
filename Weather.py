from Location import Location
import requests, json
# using openweathermap api

# import required modules

class Weather:
    def get_Weather():
        # Enter your API key here
        api_key = "52b8e14fa88148db2bada6de1ff2d273"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        city_name = Location.get_location()

        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":
            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = round((y["temp"] - 273.15),2)

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            return("Temperature: \t\t\t" +
                  str(current_temperature) + "°C" +
                  "\nAtmospheric pressure: \t" +
                  str(current_pressure) + "hPa"
                  "\nHumidity: \t\t\t\t" +
                  str(current_humidiy) + "%" +
                  "\nDescription: \t\t\t" +
                  str(weather_description))

        else:
            return(" City Not Found ")