from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import router

# Initialize FastAPI app
app = FastAPI(title="Public Holiday Calendar API")

# Register API routes
app.include_router(router)

# Serve static files (HTML, JS, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Root endpoint -> loads the frontend UI
@app.get("/")
def home():
    return FileResponse("static/index.html")