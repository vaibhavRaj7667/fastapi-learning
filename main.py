from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


post: list[dict]=[
    {
        "id": 1,
        "author":"Corey Schafer",
        "title": "FastAPI is awesome",
        "content": "This framework is really easy",
    },
    {
        "id": 2,
        "author":"Jane doe",
        "title": "FastAPI",
        "content": "This framework is really easy language",
    }
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "Home.html",{"posts":post})


@app.get("/api/posts")
def get_post():
    return post