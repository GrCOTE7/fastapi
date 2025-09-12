from fastapi import FastAPI, Path, HTTPException
import flet as ft
# import uvicorn

# uvicorn main:app --reload

app = FastAPI()

# get, put, post, delete

@app.get("/hi")
async def hello() -> str:
    return "Salut !"

@app.get("/")
async def hello() -> dict:
    return {"msg": "Salut !"}


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    print("Ready.")
