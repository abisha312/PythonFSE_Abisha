"""
TASK 1

1. Request-Response Cycle

Browser
   | GET /api/courses/
URL Router (urls.py)
   |
View (views.py)
   |
Model (models.py)
   |
Database Query
   |
View prepares response
   |
HttpResponse / JsonResponse
   |
Browser


2. Middleware

Middleware executes before and after the view.

Request
   |
Middleware
   |
View
   |
Middleware
   |
Response

Examples of built-in middleware

1. SecurityMiddleware
   - Adds security headers.
   - Protects against common attacks.

2. AuthenticationMiddleware
   - Associates logged-in users with each request.

3. WSGI vs ASGI

WSGI
- Handles synchronous requests.
- Suitable for traditional web applications.
- Django uses WSGI by default.

ASGI
- Handles asynchronous requests.
- Supports WebSockets and long-lived connections.
- Used for chat applications and real-time systems.


4. MVC vs MVT

MVC

Model
View
Controller

Django follows MVT

Model -> Model

View -> Controller

Template -> View

The Django View contains the application logic,
while Template is responsible for presentation.
"""