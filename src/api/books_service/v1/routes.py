from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/main")
def get_main():
    return {"Hello":"Manish"}