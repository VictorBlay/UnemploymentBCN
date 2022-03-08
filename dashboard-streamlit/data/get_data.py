from urllib import request
import requests

url ="http://127.0.0.1:8000"


def anual_pop(Year):
    return request.get(url+f"/TotalPopulation/Year/{Year}").json()