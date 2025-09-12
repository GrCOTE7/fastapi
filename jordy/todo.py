from fastapi import FastAPI, Path, HTTPException
import flet as ft
from typing import Union, List, Optional
from pydantic import BaseModel

app = FastAPI(
    title="Ma super API ToDo",
    version="1.0.0",
    description="Ceci est une super API pour une ToDo liste.",
)


class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: str
    completed: bool = False


class TodoResponse(BaseModel):
    items: List[Todo]
    total: int


store_todo = [
    Todo(
        id=1,
        title="Acheter du lait",
        description="Aller au supermarché et acheter du lait",
        due_date="2023-10-01",
    ),
    Todo(
        id=2,
        title="Envoyer un email",
        description="Envoyer un email à mon patron",
        due_date="2023-10-02",
    ),
]


@app.get("/", response_model=TodoResponse)
async def todos() -> dict:
    return {"items": store_todo, "total": len(store_todo)}


@app.get("/{todo_id}")
async def read_todo(
    todo_id: int = Path(..., description="The ID of the todo to retrieve", gt=0)
) -> Todo:
    for todo in store_todo:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="ToDo not found")


@app.post("/todo", response_model=Todo, status_code=201)
async def create_todo(todo: Todo) -> Todo:
    store_todo.append(todo)
    return todo


if __name__ == "__main__":
    print("Ready.")
