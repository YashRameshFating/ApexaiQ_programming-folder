from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router

# Create FastAPI application
app = FastAPI(title="Crypto Price Tracker")

# Register API routes
app.include_router(router)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Homepage
@app.get("/")
def home():
    return FileResponse("static/index.html")