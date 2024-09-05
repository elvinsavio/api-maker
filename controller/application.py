from typing import Annotated
from fastapi import APIRouter, Request, Form
from templates import templates

application_router = APIRouter()


@application_router.get("/new-application/", tags=["Application"])
async def new_application_view(request: Request):
    return templates.TemplateResponse("new-application.html", {"request": request})


@application_router.post("/new-application/", tags=["Application"])
async def create_application(
    application_name: Annotated[str, Form()], application_description: Annotated[str, Form()]
):
    ...