from fastapi import FastAPI, Path, HTTPException
import flet as ft
from typing import Union, List, Optional
from pydantic import BaseModel


app = FastAPI(
    title="Ma super API ToDo",
    version="1.0.0",
    description="Ceci est une super API pour une ToDo liste.",
)


class ToDo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: str
    completed: bool = False


class TodoResponse(BaseModel):
    items: List[ToDo]
    total: int


store_todo = [
    ToDo(
        id=1,
        title="Acheter du lait",
        description="Aller au supermarché et acheter du lait",
        due_date="2023-10-01",
    ),
    ToDo(
        id=2,
        title="Envoyer un email",
        description="Envoyer un email à mon patron",
        due_date="2023-10-02",
    ),
]


@app.get("/", response_model=TodoResponse)
async def todos() -> dict:
    return {"items": store_todo, "total": len(store_todo)}


@app.get("/{id}")
async def get_todo(
    id: int = Path(..., description="The ID of the todo to retrieve", gt=0)
) -> ToDo:
    for todo in store_todo:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="ToDo not found")


@app.post("/todo", response_model=ToDo, status_code=201)
async def create_todo(todo: ToDo) -> ToDo:
    store_todo.append(todo)
    return todo


if __name__ == "__main__":
    print("Ready.")
