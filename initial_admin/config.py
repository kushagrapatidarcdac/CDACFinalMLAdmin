import os
from dotenv import load_dotenv

class Settings():
    MONGO_URI: str
    MONGO_DB: str
    
    def __init__(self):
        load_dotenv()
        self.MONGO_URI = os.getenv("MONGO_URI")
        self.MONGO_DB = os.getenv("MONGO_DB")

settings = Settings()


if __name__ == "__main__":
    print("Configuration settings:")
    print(f"MongoDB URI: {settings.MONGO_URI}")
    print(f"MongoDB Database: {settings.MONGO_DB}")