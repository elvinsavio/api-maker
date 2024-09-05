from fastapi import APIRouter
from .application import application_router


routers: list[APIRouter] = [application_router]
