# app/routes/urls.py
from fastapi import APIRouter, HTTPException
from app.schemas import URLCreate, URLResponse
from app.crud import create_url, get_url

router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
async def shorten_url(url_create: URLCreate):
    url_entry = await create_url(url_create.url)
    return url_entry


@router.get("/shorten/{short_code}", response_model=URLResponse)
async def retrieve_url(short_code: str):
    url_entry = await get_url(short_code)
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_entry


# TODO: Implement update_url route
# TODO: Implement delete_url route
# TODO: Implement get_url_statistics route
