from .BaseController import BaseController
from fastapi import UploadFile
from Models import EnmsConstence
from .Project_Controller import project_controller
import re

class Data_Controller(BaseController):
    def __init__(self):
        self.Max_Scale=1048576
        super().__init__()
    def Validate_File(self,file:UploadFile):
        if file.content_type not in  self.app_settings.File_Allowed_TYPES:
            return False,EnmsConstence.File_Type_Not_Support.value
        if file.size > self.app_settings.File_MAX_SIZE*self.Max_Scale:
            return False,EnmsConstence.File_Size_Exceeded.value
        return True ,EnmsConstence.File_Uploaded_Sucess.value
  

