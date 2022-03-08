from fastapi import APIRouter

router = APIRouter()

@router.get("/persona/{name}")
async def person_name(name):
    return {"message":f"Endpoint parametrizado, {name}"}

@router.get("/persona/{name}/{age}")
async def person_name(name:str, age:int):
    return {
        "name":{
            "value":name,
            "type":str(type(name))
        },
        "age":{
            "value":age,
            "type":str(type(age))
        }
    }
  