from pydantic import BaseModel


class Room(BaseModel):
    id: int
    floor: int
    name: str


class CreateRoom(BaseModel):
    floor: int
    name: str
