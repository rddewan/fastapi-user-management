from fastapi import FastAPI

from app.features.admin.country import v1_admin_country_router

app = FastAPI()
app.include_router(v1_admin_country_router, tags=["v1 Admin Country"])
