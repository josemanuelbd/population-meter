import sys
from flask import Flask, abort, jsonify, request
from populartimes import populartimes 

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works and running, use getPopularTimes/ service'

@app.route('/getPopularTimes')
def getPopularTimes():
  apiKey = request.args.get('apiKey', type = str)
  lat = request.args.get('lat', type = float)
  lon = request.args.get('lon', type = float)
  distance = request.args.get('distance', type = float, default = 0.0003)

  if apiKey is None:
        abort(400, description="apiKey param required")
  if lat is None:
        abort(400, description="lat param required")
  if lon is None:
        abort(400, description="lon param required")
  
  threads = 20
  radius = 100
  allPlaces = False
  placeTypes = []

  # Calculate an area around the user using the distance
  coordinateInitial = (round(lat - distance, 6), round(lon - distance, 6))
  coordinateEnd = (round(lat + distance, 6), round(lon + distance, 6))

  times = populartimes.get(
    apiKey, 
    placeTypes,
    coordinateInitial,
    coordinateEnd,
    threads,
    radius,
    allPlaces
  )

  return jsonify(times)

