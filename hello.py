import time
from slackclient import SlackClient
from configobj import ConfigObj
import json
import random
from flask import Flask
import urllib.request
import weather

config = ConfigObj('config.ini')

token = config['access_token']
bot_token = config['bot_user_access_token']
id = config['client_id']
secret = config['client_secret']

print(token)

sc = SlackClient(bot_token)

def post_to_channel():
    pass

channels = sc.api_call("channels.list") # channels.list for public channesl
channels = (channels['channels'])


def get_channel_id(name):
    for channel in channels:
        #print(channel['name_normalized'])
        if channel['name_normalized'] == name:
            return channel['id']

get_channel_id('bot_testing') # sticht to general


def send_message(channel,text):
    channel_id = get_channel_id(channel)
    message = { "type": "message"}
    message["channel"] = channel_id
    message['id'] = random.randint(1,1000) # i dont think it matters that this is random
    message['text'] = text

    m = json.dumps(message)
    print(m)
    sc.api_call("chat.postMessage",channel=channel_id,text=text)

import pugme
def post_pug():
    results = pugme.get_pug_me()
    send_message('bot_testing',results['pug'])

post_pug()

"""
def main():
    if sc.rtm_connect():
        while True:
            # look for pug triggers, see what time it is
            time.sleep(1)
    else:
        print ("Connection Failed, invalid token?")

if __name__ == "__main__":
    main()
"""

# start thread to ping whenever its 12:00
from threading import Thread
from time import sleep
import datetime


def post_weather():
    weather.get_forecast()


def threaded_function(arg):
    while True:
        now = datetime.datetime.now()
        # weekday tuesday == 1 and thursday == 3
        if now.hour == 12 and (now.weekday() == 1 or now.weekday() == 3):
            # ping the server
            #urllib.request.urlopen('/weather')
            post_weather()
            sleep(60*60*22) # make it sleep for 22 hours

        sleep(1)


# server crap
app = Flask(__name__)


@app.route("/weather")
def weather_hook():
    weather.get_forecast()
    return "Hello World!"

@app.route("/pug")
def pug_hook():
    count = None
    #count comes from reading the message that triggered this
    pugme.get_pug_me(count)
    return "Hello World!"

if __name__ == "__main__":
    thread = Thread(target=threaded_function, args=(10,))
    thread.start() # the thread should never stop haha
    app.run()