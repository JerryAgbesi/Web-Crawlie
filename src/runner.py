import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run("runner:app",host='127.0.0.1',port=4200,reload=True)
