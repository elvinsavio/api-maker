from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controller import routers

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



for router in routers:
    app.include_router(router)
