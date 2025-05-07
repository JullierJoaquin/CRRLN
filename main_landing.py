from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar archivos estáticos y templates para la landing

app.mount("/css", StaticFiles(directory="landing/static/css"), name="css")
app.mount("/js", StaticFiles(directory="landing/static/js"), name="js")
app.mount("/images", StaticFiles(directory="landing/static/images"), name="images")
app.mount("/static", StaticFiles(directory="landing/static"), name="static")  # opcional

templates = Jinja2Templates(directory="landing")

@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
