from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
model = pipeline("sentiment-analysis")

class PredictionRequest(BaseModel):
    query_string: str

@app.get("/health")
def health():
    return "Service is online."


@app.post("/endpoint")
def endpoint(request: PredictionRequest):
    data = request.query_string
    result = model(data)
    label = result[0]["label"].lower()
    score = result[0]["score"]
    out = {"query": data, "label": label, "score": score}
    return out
