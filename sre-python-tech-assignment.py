#!/usr/bin/env python3
import json
import requests
from urllib.request import urlretrieve
from datetime import datetime, timedelta

## Define our target url
neows_url = "https://api.nasa.gov/neo/rest/v1/feed"
mykey = "57mwuDVeXDdR9UtDLG4W9Lb7jPN65bggqplSr2FI"


## Request and return NeoWS's feed
def getNeoWSRequest(start_date, end_date):
  ## Define our parameters for the url
  params = {
      "api_key":mykey,
      "start_date":start_date,
      "end_date":end_date
  }
  ## Return the data from NeoWS's feed
  return requests.get(neows_url,params=params).json()


## Step 1:
##
## Get asteroids between the start and end dates
## into a dictionary with urllib's request and JSON
def step1_fetchNeowsAsteroidData():
  print("STEP 1:\n")

  response = getNeoWSRequest("2019-10-31", "2019-11-02")    ## Get the data between the desired dates

  ## For every day in the dictionary,
  ## get every asteroid and print the desired info
  ## 'name', 'id' and 'close_approach_date_full
  for date in response["near_earth_objects"]:
    print(date + ": " + str(len(response["near_earth_objects"][date])) + " asteroids was found\n")
    for asteroid in range(len(response["near_earth_objects"][date])):
      print(f"""Asteroid {asteroid}:
      Name: {response["near_earth_objects"][date][asteroid]["name"]}
      ID: {response["near_earth_objects"][date][asteroid]["id"]}
      Close approach date full: {response["near_earth_objects"][date][asteroid]["close_approach_data"][0]["close_approach_date_full"]}\n""")


## Step 2:
## Get the asteroids from NeoWS's feed
## and calculate: the slowest, fastest,
## mean and median velocity in kilometers_per_second
def step2_calculatespeeds():
  print("STEP 2:\n")

  response = getNeoWSRequest("2020-09-10", "2020-09-17")    ## Get the data between the desired dates

  asteroid_list = {}                                        ## Create empty dictionary to contain all our asteroids
  asteroid_index = 0

  for date in response["near_earth_objects"]:               ## Get all the asteroids into the dictionary
    for asteroid in response["near_earth_objects"][date]:
      asteroid_list[asteroid_index] = asteroid
      asteroid_index += 1

  mean_velocity = 0.0                                       ## Define calculation variables
  median_velocity = 0.0
  velocity_list = []

  for asteroid in asteroid_list:                            ## Get all the kilometers per second velocity into our list
    velocity_list.append(float(asteroid_list[asteroid]["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"]))

  for velocity in velocity_list:                            ## Calculate the mean velocity
    mean_velocity += velocity
  mean_velocity /= len(velocity_list)

  ## "Calculate the median velocity"
  n = len(velocity_list)                                    ## Define variables for length of the list
  velocity_list.sort()                                      ## Sort the list

  if n % 2 == 0:                                            ## Check if the length of the list is even or odd
      median1 = velocity_list[n//2]                         ## If the list is even, get the mean between the 2 median
      median2 = velocity_list[n//2 - 1]
      median_velocity = (median1 + median2)/2
  else:                                                     ## Else, get the velocity in the middle of the list
      median_velocity = velocity_list[n//2]

  print(f"Fastest velocity, in kilometers per second, is: {velocity_list[-1]}")
  print(f"Slowest velocity, in kilometers per second, is: {velocity_list[0]}")
  print(f"Mean velocity: {mean_velocity}")
  print(f"Median is: {median_velocity}\n")


## Step 3: Find the 3 most recent (from today)
## asteroid with the flag is_potentially_hazardous_asteroid set to true
def step3_findRecentHazardousAsteroid():
  print("STEP 3:\n")

  today = datetime.now()                      ## Get the date of today
  potentially_hazardous_list = []             ## Create empty list to hold asteroids with the flag to true
  days_ago = 0                                ## Index counter for the days before today
  date = today.strftime("%Y-%m-%d")           ## Define the date of today in a string in the format YYYY-mm-dd

  while len(potentially_hazardous_list) < 3:  ## Loop until we get 3 asteroids in the list
    response = getNeoWSRequest(date,date)     ## Get the data of the day "date"

    for asteroid in response["near_earth_objects"][date]: ## For every asteroid on that day:
      if asteroid["is_potentially_hazardous_asteroid"]:   ## Check if the flag is set to true
        potentially_hazardous_list.append(asteroid)       ## If so, append it to the list
    
    days_ago += 1                             ## Increment the past days counter
    date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d") ## Set the new day based on the counter
    
  print("The 3 most recent asteroids found with the flag is_potentially_hazardous_asteroid set to true")

  for asteroid in potentially_hazardous_list: ## Print our results
    print(f"""
    Name: {asteroid["name"]}
    ID: {asteroid["id"]}
    Date: {asteroid["close_approach_data"][0]["close_approach_date_full"]}
    Link: {asteroid["links"]["self"]}""")


step1_fetchNeowsAsteroidData()
step2_calculatespeeds()
step3_findRecentHazardousAsteroid()