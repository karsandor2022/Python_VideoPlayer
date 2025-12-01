from . import flask_app, fastapi_app
from .frontend.routes import bp as frontend_bp
from .backend.videos_router import router as videos_router
from .backend.database import init_db
from fastapi.middleware.wsgi import WSGIMiddleware

# Register Flask routes
flask_app.register_blueprint(frontend_bp)

# Register FastAPI routes
fastapi_app.include_router(videos_router, prefix="/api/videos")

# Initialize SQLite DB
init_db()

# Mount FastAPI inside Flask
flask_app.wsgi_app = WSGIMiddleware(fastapi_app)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)