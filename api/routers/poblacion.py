import json
from fastapi import APIRouter
from database.mongo import get_data, distinct
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Population/Neighborhood")
async def barrios():
    res = distinct("poblacion", "Neighborhood.Name")
    return {"barrios":res}

@router.get("/Population/Year")
async def años():
    res = distinct("poblacion", "Year")
    return {"año":res}


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
   

@router.get("/Population/Year/{year}")
async def poblacion_total(year):
    res = get_data("poblacion", {"Year":year}, {'Number':1,'_id':0})
    total_pop = [tot["Number"] for tot in res]
    suma = sum(total_pop)
    return {"Population Year":suma}





