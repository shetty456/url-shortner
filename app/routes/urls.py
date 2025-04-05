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
    url_entry.access_count +=1
    await url_entry.save()
    return {
        "id": url_entry.id,
        "url": url_entry.url,
        "short_code":url_entry.short_code,
        "created_at": url_entry.created_at,
        "updated_at": url_entry.updated_at,
        "access_count": url_entry.access_count,
    }


# TODO: Implement update_url route
# TODO: Implement delete_url route

@router.delete("/shorten/{short_code}" )
async  def delete_url_route(short_code:str):
    url_delete = await delete_url(short_code)
    if "not found" in url_delete:
        raise HTTPException(status_code=404,detail="short code URL not found")
    return url_delete
    
# TODO: Implement get_url_statistics route
@router.get("/shorten/{short_code}/status" )
async  def  status_url_route(short_code: str):
    url_status = await get_url_status (short_code)
    if not  url_status:
        raise HTTPException(status_code=404,detail="short  URL not fond")
    return url_status
