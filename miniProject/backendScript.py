from fastapi import FastAPI
from projectFile1 import Developer,Project

app = FastAPI()

@app.post('/developers')
async def posting(developer:Developer):
    return {'message':'Developer Created Successfully',
            'developer':developer.name}


@app.post('/projects')
async def create_project(projekti:Project):
    return {'message':f'{projekti} Created Sucessfully'}

@app.get('/projects/')
async def get_projects():
    Programeri = Developer(name='Dren')
    sample_projects = Project(name='Sample Project',
                              description='This Is Sample Project',
                              language=['Python','C++','Java'],
                              lead_developer=Programeri)

    return {'projects':[sample_projects]}


