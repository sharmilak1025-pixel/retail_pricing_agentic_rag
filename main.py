from fastapi import FastAPI
from pydantic import BaseModel
from agents.pricing_agent import run_agent

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/compare-prices")
def compare_prices(req: QueryRequest):
    response = run_agent(req.query)
    return {"answer": response}