import json
from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from json import loads

router = APIRouter()

@router.get("/Genero/{Gender}")
async def genero(Gender):
    res = list(db["poblacion"].find({"Gender":Gender}))[0]
    return loads(json_util.dumps(res))