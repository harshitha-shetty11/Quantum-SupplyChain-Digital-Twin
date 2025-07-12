from fastapi import FastAPI, Request
from src.digital_twin.core.graph_model import SupplyChainTwin

app = FastAPI()
twin = SupplyChainTwin()

@app.get("/twin/state")
def get_twin_state():
    return twin.get_state()

@app.post("/twin/optimize")
async def optimize(request: Request):
    data = await request.json()
    scenario = data.get("scenario", "Normal Operation")
    twin.update_state(scenario)
    return twin.get_state()

@app.get("/health")
def health_check():
    return {"status": "ok"}
