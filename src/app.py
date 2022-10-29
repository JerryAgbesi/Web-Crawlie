import uvicorn
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class URL(BaseModel):
    url: HttpUrl

#Home route
@app.get("/")
def home():
    return {"msg":"Welcome to web Crawlie"}

@app.post("/scrape_url")
async def scrape_url(url:URL):

    #get url requested by the user
    page = requests.get(str(url.url))

    soup = BeautifulSoup(page.text,"html.parser")

    #get website's title,decription,keywords and image
    def get_title():
        return soup.head.find("title").text if soup.head.find("title") else None

    def get_description():
        main_desc = soup.head.find("meta",attrs={'name':'description'}).get("content") if soup.head.find("meta",attrs={'name':'description'}) else None 
        
        og_desc = soup.find("meta",property="og:description").get("content") if soup.find("meta",property="og:description") else None

        return main_desc or og_desc

    def get_keywords():
        return soup.head.find("meta",attrs={'name':'keywords'}).get('content') if soup.head.find("meta",attrs={'name':'keywords'}) else None 

    def get_image():
        return soup.find("meta",property="og:image").get("content") if soup.find("meta",property="og:image") else None    

    return {
        "title":get_title(),
        "Description":get_description(),
        "Keywords":get_keywords(),
        "Image":get_image()
    }


