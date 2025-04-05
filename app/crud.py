from app.models import URL
from app.schemas import URLCreate
import random
import string
from fastapi_cache.decorator import cache

def generate_short_code():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


async def create_url(url_create: URLCreate):
    short_code = generate_short_code()
    url_entry = await URL.create(url=url_create.url, short_code=short_code)
    return url_entry

@cache(expire=60)
async def get_url(short_code: str):
    return await URL.get_or_none(short_code=short_code)


# TODO: Implement update_url()
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
        
