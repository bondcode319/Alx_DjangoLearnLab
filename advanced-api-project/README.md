# Book API Documentation

## Endpoints

### Books Endpoint (`/api/books/`)

#### GET /api/books/
- Lists all books
- Publicly accessible
- Supports filtering and searching:
  - Search by title: `?search=harry`
  - Order by: `?ordering=publication_year`

#### POST /api/books/
- Creates a new book
- Requires authentication
- Request body example:
```json
{
    "title": "New Book",
    "publication_year": 2023,
    "author": 1
}
```

### Book Detail Endpoint (`/api/books/<id>/`)

#### GET /api/books/<id>/
- Retrieves a specific book
- Publicly accessible

#### PUT/PATCH /api/books/<id>/
- Updates a book
- Requires authentication
- Validates publication year

#### DELETE /api/books/<id>/
- Deletes a book
- Requires authentication
- Returns success message

## Filtering, Searching, and Ordering

### Filtering
Filter books using query parameters:
- Title: `?title=harry`
- Publication Year Range: 
  - Minimum: `?publication_year_min=2000`
  - Maximum: `?publication_year_max=2023`
- Author Name: `?author_name=rowling`

### Searching
Search across multiple fields:
- General search: `?search=potter`
- Searches through title and author name

### Ordering
Order results by specific fields:
- Publication Year: `?ordering=publication_year`
- Reverse Order: `?ordering=-publication_year`
- Multiple Fields: `?ordering=publication_year,title`

## Example API Requests

```bash
# Filter books by title
curl "http://localhost:8000/api/books/?title=potter"

# Filter books by publication year range
curl "http://localhost:8000/api/books/?publication_year_min=2000&publication_year_max=2023"

# Search books
curl "http://localhost:8000/api/books/?search=harry"

# Order books by publication year descending
curl "http://localhost:8000/api/books/?ordering=-publication_year"

# Combined filtering, searching, and ordering
curl "http://localhost:8000/api/books/?title=potter&publication_year_min=2000&ordering=-publication_year"
```

## Testing Instructions

Using cURL:

1. List all books:
```bash
curl http://localhost:8000/api/books/
```

2. Create a book (authenticated):
```bash
curl -X POST http://localhost:8000/api/books/ \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"title":"New Book","publication_year":2023,"author":1}'
```

3. Update a book:
```bash
curl -X PUT http://localhost:8000/api/books/1/ \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"title":"Updated Title","publication_year":2023,"author":1}'
```

4. Delete a book:
```bash
curl -X DELETE http://localhost:8000/api/books/1/ \
     -H "Authorization: Token YOUR_TOKEN"
```