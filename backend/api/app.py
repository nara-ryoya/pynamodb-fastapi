from fastapi import FastAPI

from . import routers

app = FastAPI()
app.include_router(routers.tsundoku_router)
