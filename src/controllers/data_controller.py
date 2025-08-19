from .BaseController import BaseController
from fastapi import UploadFile


class Data_Controller(BaseController):
    def __init__(self):
        self.Max_Scale=1048576
        super().__init__()
    def Validate_File(self,file:UploadFile):
        if file is not self.app_settings.File_Allowed_TYPES:
            return False
        if file.size > self.app_settings.File_MAX_SIZE*self.Max_Scale:
            return False
        return True
        
