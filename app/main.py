from fastapi import FastAPI

from app.features.admin.country import v1_admin_country_router
from app.core.http_errors import register_exception_handler

app = FastAPI()
app.include_router(v1_admin_country_router, tags=["v1 Admin Country"])
register_exception_handler(app)
