from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_settings import BaseSettings


app = FastAPI()

class Person(BaseModel):
    name:str
    age:int

@app.post('/create_person')
async def create_person(person:Person):
    return {'message':f"Person {person.name} created successfully"}




