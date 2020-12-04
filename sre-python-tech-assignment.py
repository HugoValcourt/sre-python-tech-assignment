#!/usr/bin/env python3
import json
import requests
from urllib.request import urlretrieve

mykey = "57mwuDVeXDdR9UtDLG4W9Lb7jPN65bggqplSr2FI"
start_date = "2019-10-31"
end_date = "2019-11-02"

def fetchAsteroidNeowsFeed():
  neows_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2019-10-31&end_date=2019-11-02&detailed=false"
  params = {
      'api_key':mykey,
      'start_date':'2020-01-22',
      'end_date':'2020-01-23'
  }
  response = requests.get(neows_url,params=params).json()
  print(response)
fetchAsteroidNeowsFeed()

"""## Variable definition. I got the url from NeoWS Api's website
neows_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=STARTING_DATE&end_date=ENDING_DATE&detailed=true&api_key="
mykey = "57mwuDVeXDdR9UtDLG4W9Lb7jPN65bggqplSr2FI"

## Start and End dates could also be user input
start_date = "2019-10-31"
end_date = "2019-11-02"

## Set the proper search date
neows_url = neows_url.replace("STARTING_DATE", start_date)
neows_url = neows_url.replace("ENDING_DATE", end_date)

## Request our object from NeoWs
neows_obj = urllib.request.urlopen(neows_url + mykey)

## Get info from file
neows_read = neows_obj.read()

## Decode JSON to Python data
decodeneows = json.loads(neows_read.decode("utf-8"))

print(decodeneows)"""