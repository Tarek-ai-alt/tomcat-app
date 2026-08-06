from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "tomcat-app"
    database_url: str = "postgresql+asyncpg://tomcat_user:tomcat_password@db:5432/tomcat_db"

settings = Settings()
