"""
# URL Shortener API

## Setup
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run the server: `poetry run uvicorn app.main:app --reload`

## API Endpoints
- `POST /shorten` - Shorten a URL
- `GET /shorten/{short_code}` - Retrieve original URL
- TODO: Implement `PUT /shorten/{short_code}` - Update a short URL
- TODO: Implement `DELETE /shorten/{short_code}` - Delete a short URL
- TODO: Implement `GET /shorten/{short_code}/stats` - Retrieve URL statistics
"""