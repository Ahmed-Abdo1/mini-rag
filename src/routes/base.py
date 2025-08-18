from fastapi import FastAPI, APIRouter,Depends
import os
from Helper.config import get_settings,Setting

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(app_Sett:Setting =Depends(get_settings)):
    # app =get_settings()
    app_name = app_Sett.APP_Name
    app_version = app_Sett.App_version
    app_OPENAI_API = app_Sett.OPENAI_API_KEY

    return {
        "app_name": app_name,
        "app_version": app_version,
        "app_OPEN":app_OPENAI_API
    }