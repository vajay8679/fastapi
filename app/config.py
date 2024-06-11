# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # databasse_password: str = "localhost"
    # path: int
    # secret_key: str = "2348uidkksndl"
    # database_username: str = "root"


    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str 
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
print(settings.database_username)