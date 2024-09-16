from fastapi import FastAPI

myapp= FastAPI()

@myapp.get("/")
def index():
    return {"Hello"}