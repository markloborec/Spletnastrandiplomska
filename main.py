from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"sps":123,"teps":424,"thss":52525,"oimtbi": 5123, "tnpss":1255})
@app.get("/sps", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("sps.html", {"request": request})
@app.get("/teps", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("teps.html", {"request": request})
@app.get("/thss", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("thss.html", {"request": request})
@app.get("/tnpss", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("tnpss.html", {"request": request})
@app.get("/oimtbi", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("oimtbi.html", {"request": request})
@app.get("/statistika", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("statistika.html", {"request": request})
@app.get("/opcije", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("opcije.html", {"request": request})
@app.get("/informacije", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("informacije.html", {"request": request})