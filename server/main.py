import uvicorn
from fastapi import FastAPI

from mysocketio import sio_app

app = FastAPI()
app.mount('/', app=sio_app)

if  __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
    