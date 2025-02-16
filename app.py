from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from fastapi.encoders import jsonable_encoder
from uuid import UUID, uuid4


app = FastAPI()

tanks = []

class Tank(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    location: str
    lat: float
    long: float

class TankUpdate(BaseModel):
    location: str | None = None
    lat: float | None = None
    long: float | None = None

@app.get("/tank")
async def get_tanks():
    return tanks

@app.get("/tank/{id}")
async def get_tank(id: UUID):
    for tank in tanks:
        if tank.id == id:
            return tank
    raise HTTPException(status_code=404, detail = "Tank not found")

@app.post("/tank")
async def create_tank(tank_request: Tank):
    if not tank_request.location or tank_request.lat is None or tank_request.long is None:
        raise HTTPException(status_code=400, detail="Invalid Request")

    tank_json = jsonable_encoder(tank_request)
    tanks.append(tank_request)

    return JSONResponse({"success": True, "result": tank_json},status_code=201)       

@app.patch("/tank/{id}")
async def update_tank(id: UUID, tank_update: TankUpdate):
    for i, tank in enumerate(tanks):
        if tank.id == id:
            tank_update_dict = tank_update.model_dump(exclude_unset=True)
            try: 
                updated_tank = tank.copy(update=tank_update_dict)
                tanks[i] = Tank.model_validate(updated_tank)
                json_updated_tank = jsonable_encoder(updated_tank)
                return JSONResponse(json_updated_tank, status_code=201)
            except ValidationError:
                raise HTTPException(status_code=400, detail="Invalid tank data")
            raise HTTPException(status_code=404, detail="Tank not found")
        
@app.delete("/tank/{id}")        
async def delete_tank(id: UUID):
    for tank in tanks:
        if tank.id == id:
            tanks.remove(tank)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Tank not found")