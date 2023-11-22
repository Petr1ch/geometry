from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8080

    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "geometry"
    DB_DRIVER: str = "postgresql+asyncpg"

    @property
    def sqlalchemy_database_uri(self) -> str:
        return f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
