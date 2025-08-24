Key features implemented:

- Full CRUD operations for posts and comments
- Pagination with customizable page size
- Search functionality for posts
- Ordering capabilities
- Permission controls
- Nested serialization of comments within posts
- Author-only edit/delete permissions
- Automatic author assignment on creation
- User following system
- Personalized feed based on followed users

You can test the API endpoints:

Posts and Comments:
- List posts: GET /api/posts/
- Create post: POST /api/posts/
- Get post: GET /api/posts/{id}/
- Update post: PUT /api/posts/{id}/
- Delete post: DELETE /api/posts/{id}/
- Search posts: GET /api/posts/?search=query
- Order posts: GET /api/posts/?ordering=-created_at
- Get feed: GET /api/posts/feed/

User Following:
- Follow user: POST /api/users/{id}/follow/
- Unfollow user: POST /api/users/{id}/unfollow/
- List followers: GET /api/users/followers_list/
- List following: GET /api/users/following_list/