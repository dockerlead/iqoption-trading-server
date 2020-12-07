from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.views.home import home_html

router = APIRouter()


@router.get("/")
async def root():
    return HTMLResponse(home_html)
