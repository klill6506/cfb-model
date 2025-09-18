from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Config storage
config_store = {}

@app.get("/config", response_class=HTMLResponse)
async def get_config(request: Request):
    return templates.TemplateResponse("config.html", {"request": request})

@app.post("/config")
async def post_config(
    request: Request,
    weight: float = Form(...),
    rivalry_bonus: float = Form(...),
    home_field: float = Form(...),
    travel_fatigue: float = Form(...),
    bye_week: float = Form(...),
    lookahead: float = Form(...)
):
    global config_store
    config_store = {
        "weight": weight,
        "rivalry_bonus": rivalry_bonus,
        "home_field": home_field,
        "travel_fatigue": travel_fatigue,
        "bye_week": bye_week,
        "lookahead": lookahead
    }
    return templates.TemplateResponse("result.html", {"request": request, "config": config_store})


