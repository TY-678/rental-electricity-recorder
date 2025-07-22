from fastapi import APIRouter, Depends, HTTPException

from rental_electricity_recorder.schema import SingleResponse
from rental_electricity_recorder.schema.record import RoomEvent, RoomElectricityRecord


record = APIRouter()


@record.get("/{id}/event", response_model=SingleResponse[RoomEvent])
async def get_event(id: int):
    event = RoomEvent(room_id=id, events=[])
    return SingleResponse(results=event)


@record.get("/{id}/electricity", response_model=SingleResponse[RoomElectricityRecord])
async def get_electricity(id: int):
    event = RoomElectricityRecord(room_id=id, record=[])
    return SingleResponse(results=event)


@record.post("/{id}/event")
async def create_event(id: int, event: str):
    pass


@record.post("/{id}/electricity")
async def record_electricity(id: int, electricity: float):
    pass
