from typing import Optional

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

import core.application as application_core
from templates import templates

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
    description: Optional[str] = Form(None),
    prefix: str = Form(),
):
    (res, err) = application_core.create_new_application(
        name=name, description=description, prefix=prefix
    )

    if err:
        return templates.TemplateResponse(
            "application/new-application.html", {"request": request, "error": err}
        )

    else:
        return RedirectResponse(f"applicaiton/{name}")
