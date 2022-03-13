import requests

url ="https://api-test-bcn.herokuapp.com"


def anual_pop_gender(year,gender):
    return requests.get(url+f"/Population/DataGender/{year}/{gender}").json()

def anual_pop_neigh(year):
    return requests.get(url+f"/Population/Neighborhood/{year}").json()

def meses():
    return requests.get(url+"/Unemployment/Month").json()

def years():
    return requests.get(url+"/Unemployment/Year").json()

def años():
    return requests.get(url+"/Population/Year").json()

def genero():
    return requests.get(url+"/Population/Gender").json()

def unemploy_demand(year, month):
    return requests.get(url+f"/Unemployment/Demand/{year}/{month}").json()

def unemploy_gender(year,month):
    return requests.get(url+f"/Unemployment/DataGender/{year}/{month}").json()

def unemploy_neigh(year,month):
    return requests.get(url+f"/Unemployment/Neighborhood/{year}/{month}").json()     