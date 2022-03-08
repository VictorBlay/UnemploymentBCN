import json
from fastapi import APIRouter
from database.mongo import get_data, distinct
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Population/DataGender/{Gender}")
async def genero(Gender):
    res = get_data("poblacion", {"Gender":Gender}, {'Age':1,'Number':1,'_id':0})
    return loads(json_util.dumps(res))


@router.get("/TotalPopulation/Year/{Year}")
async def poblacion_total(Year):
    res = get_data("poblacion", {"Year":int(Year)}, {'Number':1,'_id':0})
    total_pop = [tot["Number"] for tot in res]
    suma = sum(total_pop)
    return loads(json_util.dumps(suma))


@router.get("/Population/Neighborhood")
async def genero():
    res = distinct("poblacion", "Neighborhood.Name")
    return loads(json_util.dumps(res))


