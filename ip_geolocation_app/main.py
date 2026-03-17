from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router

# Initialize FastAPI application
app = FastAPI(title="IP Geolocation API")

# Register routes
app.include_router(router)

# Serve static frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Homepage route
@app.get("/")
def home():
    return FileResponse("static/index.html")