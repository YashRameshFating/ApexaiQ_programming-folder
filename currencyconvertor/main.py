from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from routes import router

app = FastAPI(title="Currency Converter API")

# register routes
app.include_router(router)

# serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    """
    Serves the main HTML page
    """
    return FileResponse("templates/index.html")