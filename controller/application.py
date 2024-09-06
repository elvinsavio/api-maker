from fastapi import APIRouter, Request, Form
from templates import templates
import core.application as application_core

application_router = APIRouter()


@application_router.get("/")
async def applicaitons_page(request: Request):
    return templates.TemplateResponse("application/menu.html", {"request": request})


@application_router.get("/new-application", tags=["Application"])
async def new_application_view(request: Request):
    return templates.TemplateResponse(
        "application/new-application.html", {"request": request}
    )


@application_router.post("/new-application", tags=["Application"])
async def create_application(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    prefix: str = Form(),
):
    (res, err) = application_core.create_new_application(
        name=name, description=description, prefix=prefix
    )

    if err:
        return templates.TemplateResponse(
            "application/new-application.html", {"request": request, "error": err}
        )
