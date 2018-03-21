import urllib2, json
from pprint import pprint

def getWeatherCondition(station_data):
    cond = str(station_data[0]['station']['condition'])
    return cond

url = 'https://brevard.weatherstem.com/api'
indata = {'api_key':'lfee7tq5','stations':['hms']}

request = urllib2.Request(url)
request.add_header('Content-Type','application/json')
outdata = json.dumps(indata)
response = urllib2.urlopen(request, outdata)

station_data = json.load(response)
condition = getWeatherCondition(station_data)
print condition
