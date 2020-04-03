import sys
from populartimes import populartimes 
print("Popular times by your coordinates using Google Places API & populartimes crawler");

# Coordinates of the user
lat = 40.284645
lon = -3.798970

# API key
apiKey = sys.argv[1]

distance = 0.0003
threads = 20
radius = 100
allPlaces = False
placeTypes = []

# Draw rectangle from the coordinates position
coordinateInitial = (round(lat - distance, 6), round(lon - distance, 6))
coordinateEnd = (round(lat + distance, 6), round(lon + distance, 6))


print(populartimes.get(
  apiKey, 
  placeTypes,
  coordinateInitial,
  coordinateEnd,
  threads,
  radius,
  allPlaces
))