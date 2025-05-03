"""

# URL Shortener API

## Setup

1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run the server: `poetry run uvicorn app.main:app --reload`

## API Endpoints

### 1. This endpoint allows you to shorten a URL.

**Endpoint**: `POST /shorten`
```{
  "url": "https://example.com"
}
```
**Response**:

```json
{
  "id": 1,
  "url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-04-05T12:34:56",
  "access_count": 0
}
```

### 2. Retrieve Original URL

**Endpoint**: `GET /shorten/{short_code}`

**Response**:

```json
{
  "id": 1,
  "url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-04-05T12:34:56",
  "access_count": 1
}
```

### 3. Update a Short URL

**Endpoint**: `GET /shorten/{short_code}`

**Request Body**:
{
  "url": "https://new-example.com"
}

```json
{
  "id": 1,
  "url": "https://new-example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-05-05T12:34:56",
  "access_count": 1
}
```

### 4. Delete a Short URL
**Endpoint**:`DELETE /shorten/{short_code}`
**Request Body**:
```json
{
  "message": "URL with shortcode deleted successfully."
}
```

### 5. Retrieve URL Statistics

**Endpoint**: `GET /shorten/{short_code}/stats`

**Request Body**:

```json
{
  "id": 1,
  "url": "https://example.com",
  "short_code": "abc123",
  "created_at": "2025-04-05T12:34:56",
  "updated_at": "2025-04-05T12:34:56",
  "access_count": 10
}
```
