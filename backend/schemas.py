
from pydantic import BaseModel, Field
from typing import List, Type

class KickOffRequest(BaseModel):
    """
    Request Schema for Travel Planning crew
    """
    current_location: str = Field(..., description="Current location of the user.")
    place_of_interest: str = Field(..., description="Place of interest for user to travel to.")
    date_range: str = Field(..., description="Date range of travel.")
    interests: List[str] = Field(..., description="User's activities of interest.")


