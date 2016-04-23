import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDFylAsuGtwbOgRz-kxGwGqymkQmXXuA90')


# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
print reverse_geocode_result
