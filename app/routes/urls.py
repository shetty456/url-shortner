# app/routes/urls.py
from fastapi import APIRouter, HTTPException,Response
from app.schemas import URLCreate, URLResponse
from app.crud import create_url, get_url,update_url

router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
async def shorten_url(url_create: URLCreate,response:Response):
    url_entry = await create_url(url_create)
    response.status_code  
    return url_entry


@router.get("/shorten/{short_code}", response_model=URLResponse)
async def retrieve_url(short_code: str,response:Response):
    url_entry = await get_url(short_code)
    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
   
    response.status_code  
    return url_entry


# TODO: Implement update_url route
@router.patch("/shorten/{short_code}", response_model=URLResponse)
async def create_url_new(short_code: str,new_url_create:URLCreate,response:Response):
    new_url_entry = await update_url(short_code,new_url_create)
    
    if not new_url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")
    response.status_code  
    return new_url_entry

# TODO: Implement delete_url route
# TODO: Implement get_url_statistics route
