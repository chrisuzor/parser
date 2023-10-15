from typing import List, Optional

from pydantic import BaseModel, Field


class MewsRoom(BaseModel):
    """Message model for Mews Room data."""
    RoomNumber: str = Field(..., alias="RoomNumber")
    RoomId: str = Field(..., alias="RoomId")
    RoomName: str = Field(..., alias="RoomName")
    RoomDescription: str = Field(..., alias="RoomDescription")
    Status: str = Field(..., alias="Status")
    IsCleaningRequired: bool = Field(..., alias="IsCleaningRequired")
    IsCleaningInProgress: bool = Field(..., alias="IsCleaningInProgress")
    IsCleaningFinished: bool = Field(..., alias="IsCleaningFinished")


class MewsData(BaseModel):
    """Base model for Mews data."""

    Id: str = Field(..., alias="Id")
    Name: str = Field(..., alias="Name")
    Description: str = Field(..., alias="Description")
    Rooms: List[MewsRoom] = Field(..., alias="Rooms")
    IsActive: Optional[bool] = Field(..., alias="IsActive")


class OptionalSchema(BaseModel):
    id: int = None
    name: str = None
    description: str = None
    is_active: bool = None
