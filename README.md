"""
# URL Shortener API

## Setup
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run the server: `poetry run uvicorn app.main:app --reload`

## API Endpoints
- `POST /shorten` - Shorten a URL
- `GET /shorten/{short_code}` - Retrieve original URL
This endpoint retrieves the original URL corresponding to a given shortened URL code. The access count for the URL is incremented each time this endpoint is accessed.
 ex:-{
  "id": 1,
  "url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-04-05T12:34:56",
  "access_count": 1
}


- TODO: Implement `PUT /shorten/{short_code}` - Update a short URL


- TODO: Implement `DELETE /shorten/{short_code}` - Delete a short URL
This endpoint deletes a shortened URL based on its shortcode.

{"message": "URL with shortcode  deleted successfully."}


- TODO: Implement `GET /shorten/{short_code}/stats` - Retrieve URL statistics
"""
This endpoint retrieves the status of a shortened URL, including information such as creation time, last updated time, and the access count.
 ex:-{
  "id": 1,
  "url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-04-05T12:34:56",
  "access_count": 0
}
