from app.models import URL
from app.schemas import URLCreate
import random
import string
from fastapi_cache.decorator import cache
from fastapi import HTTPException


def generate_short_code():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


async def create_url(url_create: URLCreate):
    short_code = generate_short_code()
    existing_url = await URL.filter(url=url_create.url).first()
    if existing_url:
        raise HTTPException(status_code=400, detail="URL already exists.")
    url_entry = await URL.create(url=url_create.url, short_code=short_code)
    return url_entry

@cache(expire=60)
async def get_url(short_code: str):
    return await URL.get_or_none(short_code=short_code)


#Implement update_url()
async def update_url(short_code: str, url_create: URLCreate):

    new_url_entry = await URL.get(short_code=short_code)
    if new_url_entry:
        new_url_entry.url = str(url_create.url)
        await new_url_entry.save()
    return new_url_entry


# TODO: Implement delete_url()

async def delete_url (short_code:str):
    url= await URL.get_or_none(short_code=short_code)
    
    if url:
        await url.delete()
        return {"message": f"URL with shortcode {short_code} deleted successfully."}
    else:
       return {"message":f"URL with short code{short_code} not found"}
# TODO: Implement get_url_statistics()
@cache(expire=60)
async def get_url_status(short_code:str):
    status=await URL.get_or_none(short_code=short_code)
    if not status:
        return None
    return{
        
        "id": status.id,
        "url": status.url,
        "short_code": status.short_code,
        "created_at": status.created_at,
        "updated_at": status.updated_at,
        "access_count": status.access_count
    }
        
