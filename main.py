from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Make sure templates are loaded correctly
templates = Jinja2Templates(directory="app/templates")

# Mount static if needed later
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/config", response_class=HTMLResponse)
async def get_config_form(request: Request):
    return templates.TemplateResponse("config_form.html", {"request": request})

@app.post("/config", response_class=HTMLResponse)
async def submit_config_form(
    request: Request,
    weight: int = Form(...),
    rivalry: float = Form(...),
    home_field: float = Form(...),
    travel: float = Form(...),
    bye: float = Form(...),
    lookahead: float = Form(...),
):
    # For now, just print it or log it. Later we'll wire it into your model.
    print("User submitted config:")
    print({
        "weight": weight,
        "rivalry": rivalry,
        "home_field": home_field,
        "travel": travel,
        "bye": bye,
        "lookahead": lookahead,
    })
    return templates.TemplateResponse("config_saved.html", {"request": request})
