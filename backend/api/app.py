from fastapi import FastAPI

from . import models, routers

app = FastAPI()
app.include_router(routers.history_router)


@app.on_event("startup")
async def startup_event():
    models.History.set_meta()
