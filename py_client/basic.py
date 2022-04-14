# This is similar to postman, manually dictate the consumption the API built on DRF project.

import requests

# setup an endpoint
endpoint = "https://httpbin.org/status/200/"
endpoint = "http://httpbin.org/anything"    # echo back anything, that I sent to this endpoint


get_response = requests.get(endpoint, json={'query': 'Hellow World'})  # HTTP get request, [IMPORTANT]; can pass own JSON alongside using the python's "requests" library.
print(get_response.text)    # prints out raw body response


# HTTP request -> HTML
# REST API HTTP request -> JSON (xml)
print(get_response.json())    # converts into a python-dictionary
print(get_response.status_code) # shows the status-code alongside
