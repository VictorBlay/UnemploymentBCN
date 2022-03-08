import json
from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads
from error.error import error

router = APIRouter()

@router.get("/Population/DataGender/{Gender}")
@error
async def genero(Gender):
    res = list(db["poblacion"].find({"Gender":Gender}))
    return loads(json_util.dumps(res))

@router.get("/Population/DataGender/{Gender}")
@error
async def genero(Gender):
    res = list(db["poblacion"].find({"Gender":Gender}))
    return loads(json_util.dumps(res))

@router.get("/Population/DataGender/{Gender}")
@error
async def genero(Gender):
    res = list(db["poblacion"].find({"Gender":Gender}))
    return loads(json_util.dumps(res))