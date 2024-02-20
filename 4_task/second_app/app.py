import uvicorn
from fastapi import FastAPI
import httpx
app = FastAPI()


@app.get('/persons')
async def get_persons_list():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://first_app:8000/persons')
        return {"persons": response.json()}


@app.get('/persons/{person_name}')
async def get_person(person_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://first_app:8000/persons/{person_name}')
        return response.json()



