from fastapi.exceptions import HTTPException
from pymongo import MongoClient
from schemas import Person


class Database:
    def __init__(self):
        self.cluster = MongoClient('mongodb://root:root@mongodb:27017/')
        self.db = self.cluster['persons_db']
        self.collection = self.db['persons']

    def get_all_persons(self) -> list[Person]:
        persons = []

        for person in self.collection.find():
            new_person = Person(name=person['name'], age=person['age'], job=person['job'], salary=person['salary'])
            persons.append(new_person)

        return persons

    def add_person(self, person: Person) -> Person:
        person_in_db = self.collection.find_one({'name': person.name})

        if person_in_db:
            raise HTTPException(400, 'person already has been created')

        self.collection.insert_one(person.model_dump())

        return person

    def get_person_by_name(self, name: str) -> Person:
        person = self.collection.find_one({'name': name})

        if not person:
            raise HTTPException(404, 'person not found')

        new_person = Person(name=person['name'], age=person['age'], job=person['job'], salary=person['salary'])

        return new_person
