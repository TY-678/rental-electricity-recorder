from fastapi import FastAPI

from rental_electricity_recorder.endpoint.room import room
from rental_electricity_recorder.endpoint.record import record

app = FastAPI(title="Rental Electricity Recorder")

app.include_router(room, prefix="/room", tags=["Room"])
app.include_router(record, prefix="/record", tags=["Record"])
