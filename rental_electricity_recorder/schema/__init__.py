from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class SingleResponse(BaseModel, Generic[T]):
    results: T
