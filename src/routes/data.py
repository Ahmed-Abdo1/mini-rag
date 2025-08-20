from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from Helper.config import get_settings, Setting
from controllers import Data_Controller  
# from controllers import project_controller
import aiofiles
import os
from Models import EnmsConstence
import logging
# from controllers.BaseController import project_controller
logger=logging.getLogger('uvicorn.error')
data_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
) 

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_Sett: Setting= Depends(get_settings)
):
    from controllers.Project_Controller import project_controller
    is_valid, result_signal = Data_Controller().Validate_File(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=
            {"signal": result_signal}
        )

    project_dir_path = project_controller().get_project_path(project_id=project_id)
    file_path=os.path.join(
        project_dir_path,
        file.filename
    )
    try:
        async with aiofiles.open(file_path,'wb') as f :
            while chunk := await file.read(app_Sett.File_MAX_SIZE):
                await f.write(chunk) 
    except Exception as e:
          logger.error(f"Error While Uploading File{e}")
          return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=
            {"signal": EnmsConstence.File_Uploaded_Failed.value}
        )
    return (
        { 'content':EnmsConstence.File_Uploaded_Sucess }
    )

        
  
    

