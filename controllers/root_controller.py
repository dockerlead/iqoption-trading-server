from fastapi.responses import HTMLResponse

async def root_controller(html):
    return HTMLResponse(html)
