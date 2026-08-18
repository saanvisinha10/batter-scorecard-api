from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import BatterScorecardResponse
from services import calculate_batter_scorecard

app = FastAPI(
    title="Batter Scorecard API",
    description="Microservice for retrieving batter-wise performance cards.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Batter Scorecard API is live"}

@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}

@app.get("/batter-scorecard/{innings_id}", response_model=BatterScorecardResponse, tags=["Batter Scorecard"])
def get_batter_scorecard(innings_id: str):
    result = calculate_batter_scorecard(innings_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Innings '{innings_id}' not found.")
    return result
