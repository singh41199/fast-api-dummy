from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from books_service.v1.routes import router as books_v1_router
from datetime import datetime
import uvicorn

DATE = datetime.now()
DESCRIPTION = "API to perform CRUD operations on books"
TITLE = "Bookstore API"
ENV = "local"
VERSION = "1.0.0"

app = FastAPI(
    title=TITLE, 
    description=DESCRIPTION,
    version=f'{ENV}-{VERSION}', 
    docs_url="/swagger/index.html",
    swagger_ui_parameters = {"docExpansion":"none","tryItOutEnabled":True,"displayRequestDuration":True},
    )

app.include_router(books_v1_router, tags=["books"])

@app.get("/")
def get_main():
    return RedirectResponse(url="/swagger/index.html")

@app.get("/version")
def get_version():
    return {"version": "1.0.0"}
