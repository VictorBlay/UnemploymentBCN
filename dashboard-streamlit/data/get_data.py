import requests

url ="http://127.0.0.1:8000"


def anual_pop_gender(year,gender):
    return requests.get(url+f"/Population/DataGender/{year}/{gender}").json()

def anual_pop(year):
    return requests.get(url+f"/Population/Year/{year}").json()

def neighborhood():
    return requests.get(url+"/Population/Neighborhood").json()

def meses():
    return requests.get(url+"/Unemployment/Month").json()

def unemploy_demand(year):
    return requests.get(url+"/Unemployment/Demand/{year}").json()

def unemploy_gender(year,month):
    return requests.get(url+"/Unemployment/DataGender/{year}/{month}").json()

def unemploy_neigh(year,month):
    return requests.get(url+"/Unemployment/Neighborhood/{year}/{month}").json()     