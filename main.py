from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from controller import routers
from templates import templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



for router in routers:
    app.include_router(router)



@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("application/menu.html", {"request": request})
