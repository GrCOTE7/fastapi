from fastapi import FastAPI, Path, HTTPException
import flet as ft
from typing import Union, List, Optional
from pydantic import BaseModel

# import uvicorn

# uvicorn main:app --reload

app = FastAPI()

# get, put, post, delete


class CoordIn(BaseModel):
    pw: str
    lat: float
    lon: float
    zoom: Optional[int] = None
    desc: Optional[str] = None


class CoordOut(BaseModel):
    lat: float
    lon: float
    zoom: Optional[int] = None
    desc: Optional[str] = None


@app.get("/hi")
async def hello() -> dict:
    return {"msg": "Salut !"}


@app.get("/")
async def hello() -> dict:
    return {"msg": "Salut !"}


@app.get("/component/{component_id}")
async def get_component(component_id: int) -> dict:
    return {"component_id": component_id}


@app.post("/position", response_model=CoordOut, response_model_exclude={"lat", 'desc'})
async def create_position(coord: CoordIn) -> dict:
    return coord


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    print("Ready.")
