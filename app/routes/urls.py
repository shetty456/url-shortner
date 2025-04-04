# app/routes/urls.py
from fastapi import APIRouter, HTTPException
from app.schemas import URLCreate, URLResponse
from app.crud import create_url, get_url,update_url

router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
async def shorten_url(url_create: URLCreate):
    url_entry = await create_url(url_create)
    return url_entry


@router.get("/shorten/{short_code}", response_model=URLResponse)
async def retrieve_url(short_code: str):
    url_entry = await get_url(short_code)
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_entry


# TODO: Implement update_url route
@router.post("/shorten/{short_code}", response_model=URLResponse)
async def create_url_new(short_code: str,new_url_create:URLCreate):
    new_url_entry = await update_url(short_code,new_url_create)
    if not new_url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return new_url_entry

# TODO: Implement delete_url route
# TODO: Implement get_url_statistics route
