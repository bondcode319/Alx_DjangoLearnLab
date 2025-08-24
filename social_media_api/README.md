Key features implemented:

Full CRUD operations for posts and comments
Pagination with customizable page size
Search functionality for posts
Ordering capabilities
Permission controls
Nested serialization of comments within posts
Author-only edit/delete permissions
Automatic author assignment on creation
You can test the API endpoints:

List posts: GET /api/posts/
Create post: POST /api/posts/
Get post: GET /api/posts/{id}/
Update post: PUT /api/posts/{id}/
Delete post: DELETE /api/posts/{id}/
Search posts: GET /api/posts/?search=query
Order posts: GET /api/posts/?ordering=-created_at