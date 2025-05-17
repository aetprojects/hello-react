from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve React build
app.mount("/", StaticFiles(directory="static", html=True), name="static")