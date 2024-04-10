from typing_extensions import Annotated
from pydantic import AfterValidator
from pydantic_core import core_schema
from datetime import datetime
from typing import TypeVar, Any
from bson import ObjectId
from typing import Any
import json

from app import db

T = TypeVar


def get_datetime():
    return datetime.utcnow().strftime("%Y-%m-%d")


def validate_object_id(v: Any) -> ObjectId:
    if isinstance(v, ObjectId):
        return v
    if ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")


class _PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> ObjectId:
        """Validates if the provided value is a valid ObjectId."""
        if isinstance(value, ObjectId):
            return value
        if isinstance(value, str) and ObjectId.is_valid(value):
            return ObjectId(value)
        raise ValueError("Invalid ObjectId")

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        """
        Defines the core schema for FastAPI documentation.
        Creates a JSON schema representation compatible with Pydantic's requirements.
        """
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.is_instance_schema(ObjectId),
        )


def parse_json(val):
    return json.dumps(val, default=str)


PyObjectId = Annotated[_PyObjectId, AfterValidator(parse_json)]


class FilterClass:
    def __init__(self, collection, model):
        self.db = collection
        self.model = model

    async def __call__(self, *args):
        if args[0] == "id":
            _data = await self.db.find_one({"_id": args[1]})
            if _data:
                return self.model(**_data)
        else:
            _data = await self.db.find_one({args[0]: args[1]})
            if _data:
                return self.model(**_data)
        return None


class MongoController:
    def __init__(self, collection: str, model: T) -> None:
        self.collection = db[collection]
        self.model = model
        self.filter_by = FilterClass(self.collection, model)

    async def insert(self, data: dict):
        try:
            await self.collection.insert_one(data)
            return True
        except Exception as e:
            print(e)
            return False

    async def find_all(self, *args, length: int = 100):
        if args == ():
            _data = await self.collection.find().to_list(length)
            if _data:
                return _data
            return []
        else:
            _data = await self.collection.find(*args).to_list(length)
            if _data:
                return _data
            return []

    async def delete(self, *args):
        _data = await self.collectionb.delete_one({args[0]: args[1]})
        if _data:
            return _data
        return []

    async def delete_all(self, *args):
        _data = await self.collection.delete_many({args[0]: args[1]})
        if _data:
            return _data
        return []

    async def update(self, id: Any, data: dict):
        _data = await self.collection.update_one({"_id": id}, {"$set": data})
        if _data:
            return True
        return False
