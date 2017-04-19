# using api from https://www.apixu.com/doc/forecast.aspx

from configobj import ConfigObj
import urllib.request
import json
config = ConfigObj('config.ini')


def get_forecast():
    token = config['weather_api_key']

    results = urllib.request.urlopen('http://api.apixu.com/v1/forecast.json?key=cd2906dac8974993837183130171804&q=Bryan')
    json_results = json.loads(results.read().decode("utf-8") )
    print(json_results)
    forecast = json_results['forecast']['forecastday']
    return forecast