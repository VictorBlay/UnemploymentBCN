import json
from fastapi import APIRouter
from database.mongo import get_data, distinct
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Unemployment/{year}")
async def ocupation(year):
    res = get_data("desempleo", {"Year":year}, {'Demand_occupation':1,'Number':1,'_id':0})
    rangos_poblacion = {}
    for ran in res:
        if ran["Demand_occupation"] in rangos_poblacion.keys():
            rangos_poblacion[ran["Demand_occupation"]] += ran["Number"]
        else:
            rangos_poblacion[ran["Demand_occupation"]] = ran["Number"]
    return rangos_poblacion