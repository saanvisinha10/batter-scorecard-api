from pydantic import BaseModel
from typing import List

class BatterPerformance(BaseModel):
    name: str
    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float
    is_out: bool

class BatterScorecardResponse(BaseModel):
    match_id: str
    innings_id: str
    batting_team: str
    batters: List[BatterPerformance]
