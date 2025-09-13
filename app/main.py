from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {
        "status": "success",
        "message": "Welcome to the User Management API",
    }
