from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
class student(BaseModel):
    id:int
    name:str
    marks:float
students={}

@app.post("/students")
def add (s:student):
    if s.id in students:
        raise HTTPException(400,"Student already exists")
    students[s.id]=s
    return s 

@app.get("/students")
def getall():
    return students 

@app.get("/students/{id}")
def getone(id:int):
    if id not in students:
        raise HTTPException(404,"Student doesn't exist")
    return students[id]

@app.put("/students/{id}")
def update(id:int,s:student):
    if id not in students:
        raise HTTPException(404,"Student doesn't exist")
    if s.id!=id:
        raise HTTPException(400,"ID Mismatch")
    students[id]=s 
    return s 

@app.delete("/students/{id}")
def delete(id:int):
    if id not in students:
        raise HTTPException(404,"Student doesn't exist")
    del students[id]
    return {"message":"student deleted"}






