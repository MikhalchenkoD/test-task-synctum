from fastapi import FastAPI
from database import Database
from schemas import Person, Exception

app = FastAPI()
db = Database()


@app.get('/persons', response_model=list[Person])
def get_persons_list() -> list[Person]:
    return db.get_all_persons()


@app.get('/persons/{person_name}', response_model=Person, responses={404: {'model': Exception}})
def get_person(person_name: str) -> Person:
    return db.get_person_by_name(person_name)


@app.post('/persons', response_model=Person, responses={400: {'model': Exception}})
def create_person(person: Person) -> Person:
    return db.add_person(person)
