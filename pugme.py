# The most important function
# Modeled after https://github.com/tadeuszwojcik/hubot-on-heroku/blob/master/scripts/pugme.coffee

# http://pugme.herokuapp.com/random



import urllib.request
import json

results = urllib.request.urlopen('http://api.apixu.com/v1/forecast.json?key=cd2906dac8974993837183130171804&q=Bryan')
json_results = json.loads(results.read().decode("utf-8") )
print(json_results)

def get_pug_me(count=None):
    results = None
    if count:
        #pug bomb
        results = urllib.request.urlopen('http://pugme.herokuapp.com/bomb?count='+str(count))

    else:
        results = urllib.request.urlopen('http://pugme.herokuapp.com/random')

    results = json.loads(results.read().decode("utf-8"))
    print(results)
    return results
