# Population-meter
This service use the populartimes project (https://github.com/m-wrzr/populartimes) which use a crawler to recover information about popular times of near places given a coordinates due there aren't a proper API of Google to do it.

## requisites
Python 3
pipenv
Google Places API KEY https://developers.google.com/places/web-service/get-api-key

# Install
```git clone https://github.com/josemanuelbd/population-meter.git```
```pipenv install .```

# Run server
```flask run```
It will open a api rest server on http://127.0.0.1:5000/

GET http://127.0.0.1:5000/getPopularTimes
PARAMS
  - apiKey : YOUR GOOGLE PLACES API KEY
  - lat: Latitude 
  - lon: Longitude


