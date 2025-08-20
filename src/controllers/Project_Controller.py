from fastapi import UploadFile
import os 
from controllers.BaseController import BaseController
# from .Project_Controller import project_controller
class project_controller(BaseController):
    def __init__(self):
        super().__init__()
    def get_project_path(self, project_id:str,base_dir: str = "data/projects"):
        project_dir=os.path.join(
            self.files_dir,
            str(project_id)
        )
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        return project_dir
