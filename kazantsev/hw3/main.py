from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from irony_detector import IronyDetector

class DetectItem(BaseModel):
    text_to_detect: str

Model = IronyDetector()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # prepare models
    Model.init()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/detect-irony/")
def detect_irony(item: DetectItem):
    """Analyzing text for irony"""
    return Model.analyze(item.text_to_detect)
