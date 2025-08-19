from fastapi import FastAPI, APIRouter,Depends,UploadFile
from Helper.config import get_settings,Setting
import os 
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.post("/upload {project_id}")

async def upload_data( project_id:str,file:UploadFile,
                app_Sett:Setting=Depends(get_settings) )