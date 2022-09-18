from fastapi import FastAPI

from . import routers

app = FastAPI()
app.include_router(routers.history_router)
