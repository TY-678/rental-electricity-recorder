from fastapi import APIRouter, Depends, HTTPException

from rental_electricity_recorder.schema import SingleResponse
from rental_electricity_recorder.schema.room import Room, CreateRoom

room = APIRouter()


@room.get("/{id}", response_model=SingleResponse[Room])
async def get_room(id: int):
    results = Room(id=id, floor=8, name="801")
    return SingleResponse(results=results)


@room.post("/", response_model=SingleResponse[Room])
async def create_room(request: CreateRoom) -> Room:
    results = Room(id=id, floor=8, name="801")
    return SingleResponse(results=results)
