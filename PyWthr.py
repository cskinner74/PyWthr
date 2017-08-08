#!/usr/bin/python
#Created by Cody Skinner

import argparse
import sys
import ConfigParser
import json
import requests

#Parser for command line arguments
parser = argparse.ArgumentParser(description="Check weather forecast for a location from the command line.")
parser.add_argument("location", help="City for forecast (ex: Atlanta)")
parser.add_argument("-z", "--zip", help="Use zipcode instead of city name", action="store_true")
args = parser.parse_args()

#Parser for config file
config = ConfigParser.ConfigParser()
config.read("config.py")
apikey = config.get('API', 'apikey')

#API information
url = "http://api.openweathermap.org/data/2.5/weather?q="+args.location+"&appid="+apikey+"&units=imperial"
zipurl = "http://api.openweathermap.org/data/2.5/weather?zip="+args.location+"&appid="+apikey+"&units=imperial"
if args.zip == 1:
    response = requests.get(zipurl)
else:
    response = requests.get(url)
data = response.json()

#get data
expand = data["weather"][0]["description"]
clouds = data["clouds"]["all"]
temp = data["main"]["temp"]
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
windspeed = data["wind"]["speed"]
winddir = data["wind"]["deg"]
#rain = data["rain"]["3h"]
city = data["name"]

print "Current conditions for "+city+": "
print expand 
print "Cloud cover: "+str(clouds)+"%"
print "Temperature: "+str(temp)+" degrees F"
print "Pressure: "+str(pressure)+" hPa"
print "Humidity: "+str(humidity)+"%"
print "Wind speed: "+str(windspeed)+" MPH"
print "Wind direction: "+str(winddir)+" degrees"
#print "Three hour rainfall: "+rain

