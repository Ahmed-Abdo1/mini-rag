from fastapi import FastAPI, APIRouter,Depends,UploadFile
from Helper.config import get_settings,Setting
import os 
from controllers import Data_Controller
data_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@data_router.post("/upload {project_id}")


async def upload_data( project_id:str,
                      file: UploadFile):
    
    is_valid=Data_Controller().Validate_File(file=file)
    return is_valid