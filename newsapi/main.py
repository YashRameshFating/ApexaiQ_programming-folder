from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router

# Create FastAPI application
app = FastAPI(title="News Aggregator API")

# Include API routes
app.include_router(router)

# Mount static files (JS and CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Serve the frontend page
@app.get("/")
def read_home():
    return FileResponse("templates/index.html")