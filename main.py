from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from starlette.responses import RedirectResponse


app = FastAPI()
model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
    query_string: str


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    return "Service is online."


@app.post("/analyze")
def endpoint(request: PredictionRequest):
    data = request.query_string
    result = model(data)
    label = result[0]["label"].lower()
    score = result[0]["score"]
    out = {"query": data, "label": label, "score": score}
    return out
