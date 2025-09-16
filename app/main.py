from fastapi import FastAPI

app = FastAPI()
users = []

@app.get("/")
def get_root():
    return {
        "status": "success",
        "message": "Welcome to the User Management API",
    }

# post api for creating user
@app.post("/users")
def create_user(
    name:str,
    email:str,
    password:str,
):
   users.append({"id":len(users)+1,"name":name,"email":email,"password":password})
   
   return {
    "status": "success",
    "data": users[len(users)-1],
   }

# get api for getting user by id
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return {
        "status": "success",
        "data": users[user_id-1],
    }

# get api for getting all users
@app.get("/users")
def get_users():
    return {
        "status": "success",
        "data": users,
    }


# put api for updating user
@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    name: str,
    email: str,
    password: str,
):
    users[user_id-1]["name"] = name
    users[user_id-1]["email"] = email
    users[user_id-1]["password"] = password
    return {
        "status": "success",
        "data": users[user_id-1],
    }

# patch api for updating user
@app.patch("/users/{user_id}")
def patch_user(
    user_id: int,
    name:str,
    email:str,
):
    users[user_id-1]["email"] = email
    users[user_id-1]["name"] = name

    return {
        "status": "success",
        "data": users[user_id-1],
    }

# delete api for deleting user
@app.delete("/users/{user_id}") 
def delete_user(user_id: int):
    
    users.remove(users[user_id-1])
    
    return {
        "status": "success",
        "data": None,
    }
