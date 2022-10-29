from gettext import find
import uvicorn
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class URL(BaseModel):
    url: HttpUrl


@app.get("/")
def home():
    return {"message":"let's go faster"}

@app.post("/scrape_url")
async def scrape_url(url:URL):

    page = requests.get(str(url.url))

    soup = BeautifulSoup(page.text,"html.parser")

    def get_title():
        return soup.head.find("title").text if "title" in soup.head else None

    # def get_description():


    return {
        "title":get_title()
    }


