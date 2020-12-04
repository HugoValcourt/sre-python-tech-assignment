#!/usr/bin/env python3
import json
import requests
from urllib.request import urlretrieve

## Define our target url
neows_url = "https://api.nasa.gov/neo/rest/v1/feed"
mykey = "57mwuDVeXDdR9UtDLG4W9Lb7jPN65bggqplSr2FI"

## Step 1:
##
## Get asteroids between the start and end dates
## into a dictionary with urllib's request and JSON

def step1_fetchNeowsAsteroidData():

  ## Define our parameters for the url
  params = {
      "api_key":mykey,
      "start_date":"2019-10-31",
      "end_date":"2019-11-02"
  }

  ## Get the data from NASA's feed
  response = requests.get(neows_url,params=params).json()

  ## For every day in our dictionary,
  ## get every asteroid and print the desired info
  ## 'name', 'id' and 'close_approach_date_full'
  for date in response["near_earth_objects"]:
    print(date + ": " + str(len(response["near_earth_objects"][date])) + " asteroids was found on that day")
    for asteroid in range(len(response["near_earth_objects"][date])):      
      print(f"""Asteroid {asteroid}:
      Name: {response["near_earth_objects"][date][asteroid]["name"]}
      ID: {response["near_earth_objects"][date][asteroid]["id"]}
      Close approach date full: {response["near_earth_objects"][date][asteroid]["close_approach_data"][0]["close_approach_date_full"]}\n""")

step1_fetchNeowsAsteroidData()