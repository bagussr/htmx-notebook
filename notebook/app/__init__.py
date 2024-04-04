import os
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient

templates = Jinja2Templates(directory="./notebook/templates")

components = Jinja2Templates(directory="./notebook/components")

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.notebook
