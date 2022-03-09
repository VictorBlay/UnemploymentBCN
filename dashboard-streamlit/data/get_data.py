from urllib import request
import requests

url ="http://127.0.0.1:8000"


def anual_pop_gender(year,gender):
    return request.get(url+f"/Population/DataGender/{year}/{gender}").json()

def neighborhood():
    return request.get(url+"/Population/Neighborhood").json()