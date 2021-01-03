import requests
import datetime

class Location:
    def get_location():
        # Get Location
        res = requests.get('https://ipinfo.io/')
        data = res.json()

        city = data['city']
        country = data['country']
        ip = data['ip']
        location = data['org']
        region = data['region']
        loc = data['loc']


        #location = ("You're computer (IP: " + ip + ") just turned on in: \n\nCOUNTRY: " + country + "\nREGION: " + region + "\nCITY: " + city + "\nLOCATION: " + location + "\nLOC: " + loc + "\nTIME: ")
        return city