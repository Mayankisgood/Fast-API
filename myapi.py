from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

# amazon.com/create User
# GET- GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING

users = {
    1:{
        "name":"john",
        "age":17,
        "adress":"Jaipur",
        "gender":"male"
    }
}

class User(BaseModel):
    name:str
    age:int
    adress:str
    gender : str

class UpdateUser(BaseModel):
    name:Optional[str] = None
    age:Optional[int]=None
    adress:Optional[str]=None
    gender:Optional[str]=None


@app.get("/")
def index():
    return {"name":"first data"}

@app.get("/get-user/{user_id}")
def get_user(user_id: int = Path(None,description = "the ID of the user you want to view",gt =0)):
    return users[user_id]

@app.post("/create-user/{user_id}")
def create_user(user_id:int,user:User):
    if user_id in users:
        return {"Error":"User exists"}
    users[user_id]= user
    return users[user_id]

@app.put("/update-user/{user_id")
def update_user(user_id:int, user:UpdateUser):
    if user_id not in users:
         return {"Error":"User does not exists"}
    if user.name != None:
         users[user_id].name =user.name
    if user.age != None:
         users[user_id].age = user.age
    if user.adress != None:
        users[user_id].adress = user.adress
    if user.gender != None:
        users[user_id].gender = user.gender
    
    return users[user_id]

@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
         return {"Error": "User does not exist"}
    del users[user_id]
    return {"Message": "User deleted successfully"}
