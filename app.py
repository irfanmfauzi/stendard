from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.file import file

app = FastAPI()

app.include_router(file)

app.mount('/', StaticFiles(directory='frontend/dist', html=True))
