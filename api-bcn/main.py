from fastapi import FastAPI
from routers import persona

app = FastAPI()
app.include_router(persona.router)


@app.get("/")
async def root():
    return {"message":"Hello"}

#lanzar la API en la terminal: uvicorn main:app
#lanzar y que se puede modificar: uvicorn main:app --reload
#primero los endpoints fijos y después parametrizados por niveles

@app.post("/adios")
async def root():
    return {"message":"Adios Hello"}


#web params
@app.get("/suma")
async def suma(a:int, b:int):
    return {"result":a+b}