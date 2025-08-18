from fastapi import FastAPI, APIRouter,Depends
import os
from Helper.config import get_settings,Setting

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome():
    app =get_settings()
    app_name = app.APP_Name
    app_version = app.App_version

    return {
        "app_name": app_name,
        "app_version": app_version,
    }