from pydantic_settings import BaseSettings , SettingsConfigDict

class Setting(BaseSettings):
    APP_Name: str
    App_version: str
    OPENAI_API_KEY: str

    class congfig:
        env_file=".env"

def get_settings():
    return Setting()