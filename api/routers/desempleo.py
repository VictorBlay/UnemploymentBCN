import json
from fastapi import APIRouter
from database.mongo import get_data, distinct
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Unemployment/Month")
async def meses():
    res = distinct("desempleo", "Month")
    return {"meses":res}

@router.get("/Unemployment/Year")
async def years():
    res = distinct("desempleo", "Year")
    return {"años":res}

@router.get("/Unemployment/Demand/{year}")
async def occupation(year):
    res = get_data("desempleo", {"Year":year}, {'Demand_occupation':1,'Number':1,'_id':0})
    demanda_ocup = {}
    for dem in res:
        if dem["Demand_occupation"] in demanda_ocup.keys():
            demanda_ocup[dem["Demand_occupation"]] += int(dem["Number"]/12)
        else:
            demanda_ocup[dem["Demand_occupation"]] = int(dem["Number"]/12)
    return demanda_ocup


@router.get("/Unemployment/DataGender/{year}/{month}")
async def unemploy_month(year, month):
    res = get_data("desempleo", {"Month":month, "Year":year}, {'Gender':1,'Number':1,'_id':0})
    unemploy_gender = {}
    for un in res:
        if un["Gender"] in unemploy_gender.keys():
            unemploy_gender[un["Gender"]] += un["Number"]
        else:
            unemploy_gender[un["Gender"]] = un["Number"]
    return unemploy_gender


@router.get("/Unemployment/Neighborhood/{year}/{month}")
async def unemploy_neighborhood(year, month):
    res = get_data("desempleo", {"Month":month, "Year":year}, {'Neighborhood Name':1,'Number':1,'_id':0})
    unemploy_neigh = {}
    for un in res:
        if un["Neighborhood Name"] in unemploy_neigh.keys():
            unemploy_neigh[un["Neighborhood Name"]] += un["Number"]
        else:
            unemploy_neigh[un["Neighborhood Name"]] = un["Number"]
    return unemploy_neigh

