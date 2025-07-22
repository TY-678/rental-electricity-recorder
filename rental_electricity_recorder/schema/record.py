from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class EventEnum(str, Enum):
    ENTER = "enter"
    LEAVE = "leave"


class Event(BaseModel):
    event: EventEnum
    created_at: datetime


class RoomEvent(BaseModel):
    room_id: int
    events: list[Event]


class ElectricityRecord(BaseModel):
    electricity: float
    created_at: datetime


class RoomElectricityRecord(BaseModel):
    room_id: int
    record: list[ElectricityRecord]
