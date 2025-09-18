from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory storage for config values
config_store = {}

@app.get("/config", response_class=HTMLResponse)
async def get_config(request: Request):
    return templates.TemplateResponse("config.html", {"request": request})

@app.post("/config")
async def post_config(
    request: Request,
    weight: str = Form(...),
    rivalry: str = Form(...),
    home_field: str = Form(...),
    travel: str = Form(...),
    bye: str = Form(...),
    lookahead: str = Form(...)
):
    global config_store
    config_store = {
        "weight": float(weight),
        "rivalry": float(rivalry),
        "home_field": float(home_field),
        "travel": float(travel),
        "bye": float(bye),
        "lookahead": float(lookahead),
    }
    return RedirectResponse(url="/", status_code=302)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "config": config_store})

