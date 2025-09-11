from typing import Union, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json

with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)

list_pokemons = {k + 1: v for k, v in enumerate(pokemons_list)}


class Pokemon(BaseModel):
    id: int
    name: str
    types:list[str]
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: Optional[int] = None
    sp_def: Optional[int] = None
    speed: int
    evolution_id: Optional[int] = None


app = FastAPI()


@app.get("/total_pokemons")
def get_pokemons_count() -> dict:
    return {"total": len(pokemons_list)}


@app.get("/pokemons", response_model=List[Pokemon])
def get_all_pokemons():
    return [Pokemon(**list_pokemons[id]) for id in list_pokemons]


if __name__ == "__main__":
    poks = get_all_pokemons()
    print(get_all_pokemons()[0].types)
