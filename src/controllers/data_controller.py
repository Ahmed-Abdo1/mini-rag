from .BaseController import BaseController
from fastapi import UploadFile
from Models import EnmsConstence
from .Project_Controller import project_controller
import re
import os 
import uuid
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
    # def Path_ID(self,project_id:str):
    #     os.path.join(
    #         project_controller.get_project_path(project_id=project_id)
    #     )
    def generate_unique_filepath(self, orig_file_name: str, project_id: str):

        random_key = str(uuid.uuid4())
        project_path = project_controller().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_file_name(
            orig_file_name=orig_file_name
        )

        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )

        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
  

