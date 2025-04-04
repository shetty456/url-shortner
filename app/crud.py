from app.models import URL
from app.schemas import URLCreate
import random
import string


def generate_short_code():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


async def create_url(url_create: URLCreate):
    short_code = generate_short_code()
    url_entry = await URL.create(url=url_create.url, short_code=short_code)
    return url_entry


async def get_url(short_code: str):
    return await URL.get_or_none(short_code=short_code)


# TODO: Implement update_url()
async def update_url(short_code: str, url_create: URLCreate):

    new_url_entry = await URL.get(short_code=short_code)
    if new_url_entry:
        new_url_entry.url = str(url_create.url)
        new_url_entry.save()
    return new_url_entry


# TODO: Implement delete_url()
# TODO: Implement get_url_statistics()
