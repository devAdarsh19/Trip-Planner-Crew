import sys
from pathlib import Path

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import KickOffRequest
from main import TravelCrew

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"]
)

@app.get("/")
def index():
    return {"message": "Hello"}

@app.post("/plan-trip")
async def plan_trip(request: KickOffRequest):
    travelCrew = TravelCrew(
        current_location=request.current_location,
        place_of_interest=request.place_of_interest,
        date_range=request.date_range,
        interests=request.interests
    )
    
    result = travelCrew.run()
    
    return {"result": result}