from fastapi import FastAPI
from typing import Optional
app= FastAPI()

@app.get("/")
def index():
    return {"message":"Helo"}


@app.get("/home")
def home():
    return {"I am Home"}

@app.get('/blog/{id}')
def blog(id:int):
    """ This ai ID"""
    return {"data":id }

@app.get("/blog/{id}/comment")
def blog(id:int):
    return {"data:{'1','2','3'}"}

@app.get("/blog1/unpublished")
def blog1():
    return {"All": "Draft Blog"}

@app.get("/blog1")
def blog(limit=10,draft:bool=True,sort:Optional[str]=None):
    if draft:
        return {'data':f'{limit} from Query Parameter Draft {draft}',"Draft":{draft}}
    else:
        return {'data':f'{limit} ELSE ELSE from Query Parameter Draft {draft}',"Draft":{draft}}