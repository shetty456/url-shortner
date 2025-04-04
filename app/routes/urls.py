# app/routes/urls.py
from fastapi import APIRouter, HTTPException
from app.schemas import URLCreate, URLResponse
from app.crud import create_url, get_url,delete_url,get_url_status

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
# TODO: Implement delete_url route

@router.delete("/shorten/{short_code}" )
async  def delete_url_route(short_code:str):
    url_delete = await delete_url(short_code)
    if "not found" in url_delete["message"]:
        raise HTTPException(status_code=404,detail="short code URL not fond")
    return url_delete
    
# TODO: Implement get_url_statistics route
@router.get("/shorten/{short_code}/status" )
async  def  status_url_route(short_code: str):
    url_status = await get_url_status (short_code)
    if not  url_status:
        raise HTTPException(status_code=404,detail="short  URL not fond")
    return url_status
