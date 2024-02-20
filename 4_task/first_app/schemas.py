from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int
    job: str
    salary: int


class Exception(BaseModel):
    detail: str
