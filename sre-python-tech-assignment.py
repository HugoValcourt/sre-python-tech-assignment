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
  ## 'name', 'id' and 'close_approach_date_full
  for date in response["near_earth_objects"]:
    print(date + ": " + str(len(response["near_earth_objects"][date])) + " asteroids was found on that day")
    for asteroid in range(len(response["near_earth_objects"][date])):      
      print(f"""Asteroid {asteroid}:
      Name: {response["near_earth_objects"][date][asteroid]["name"]}
      ID: {response["near_earth_objects"][date][asteroid]["id"]}
      Close approach date full: {response["near_earth_objects"][date][asteroid]["close_approach_data"][0]["close_approach_date_full"]}\n""")

def step2_calculatespeeds():
  ## Define our parameters for the url
  params = {
      "api_key":mykey,
      "start_date":"2020-09-10",
      "end_date":"2020-09-17"
  }

  ## Get the data from NASA's feed
  response = requests.get(neows_url,params=params).json()

  ## Create empty dictionary to contain all our asteroids
  asteroid_list = {}
  asteroid_index = 0

  ## Get all the asteroids into the dictionary
  for date in response["near_earth_objects"]:
    for asteroid in response["near_earth_objects"][date]:      
      asteroid_list[asteroid_index] = asteroid
      asteroid_index += 1  

  mean_velocity = 0.0
  median_velocity = 0.0
  velocity_list = []

  ## Get all the kilometers per second velocity into our list
  for asteroid in asteroid_list:
    velocity_list.append(float(asteroid_list[asteroid]["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]))
  
  ## Calculate the mean velocity
  for velocity in velocity_list:
    mean_velocity += velocity
  mean_velocity /= len(velocity_list)

  ## Calculate the median velocity
  n = len(velocity_list)
  velocity_list.sort()

  if n % 2 == 0: 
      median1 = velocity_list[n//2] 
      print(median1)
      median2 = velocity_list[n//2 - 1] 
      print(median2)
      median_velocity = (median1 + median2)/2
  else: 
      median_velocity = velocity_list[n//2] 

  print(f"Fastest velocity, in kilometers per second, is: {velocity_list[-1]}")
  print(f"Slowest velocity, in kilometers per second, is: {velocity_list[0]}")
  print(f"Mean velocity: {mean_velocity}")
  print(f"Median is: {median_velocity}")


#step1_fetchNeowsAsteroidData()
step2_calculatespeeds()