import json
from fastapi import APIRouter
from database.mongo import get_data, distinct
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Population/Year")
async def años():
    res = distinct("poblacion", "Year")
    return {"año":res}

@router.get("/Population/Gender")
async def años():
    res = distinct("poblacion", "Gender")
    return {"genero":res}

@router.get("/Population/Neighborhood/{year}")
async def poblacion_barrios(year):
    bar = get_data("poblacion", {"Year":year}, {'Neighborhood.Name':1, 'Number':1, '_id':0})
    poblacion_barrios = {}
    for b in bar:
        if b["Neighborhood.Name"] in poblacion_barrios.keys():
            poblacion_barrios[b["Neighborhood.Name"]] += b["Number"]
        else:
            poblacion_barrios[b["Neighborhood.Name"]] = b["Number"]
    return poblacion_barrios

@router.get("/Population/DataGender/{year}/{gender}")
async def edad_genero(year, gender):
    res = get_data("poblacion", {"Gender":gender, "Year":year}, {'Age':1,'Number':1,'_id':0})
    rangos_poblacion = {}
    for ran in res:
        if ran["Age"] in rangos_poblacion.keys():
            rangos_poblacion[ran["Age"]] += ran["Number"]
        else:
            rangos_poblacion[ran["Age"]] = ran["Number"]
    return rangos_poblacion
   





