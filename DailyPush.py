from Location import Location
from Weather import Weather
from News import  News

import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '1130915184:AAF_R4BGTzM7WHmwEgDVGjo7mRmOOuo6EFE'
    #bot_chatID = '1062466771' #Testing Personal
    bot_chatID = '-473488749' #Group
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


message = telegram_bot_sendtext("Daily Push:\n\n" + "Location: " + Location.get_location() +"\n\nWeather:\n" + Weather.get_Weather() + '\n\nNews:\n' + News.getNews())
#print(message)