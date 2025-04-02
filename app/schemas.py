from pydantic import BaseModel, HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    id: int
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime
    access_count: int
