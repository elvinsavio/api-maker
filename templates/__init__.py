from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
templates.env.auto_reload = True