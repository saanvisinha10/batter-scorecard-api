from typing import Dict, Any, Optional

MOCK_BALL_DB: Dict[str, Dict[str, Any]] = {
    "innings_101_1": {
        "match_id": "match_101",
        "batting_team": "Royal Challengers Bengaluru",
        "ball_events": [
            {"over_ball": "0.1", "striker": "Virat Kohli", "runs": 4, "is_wicket": False, "is_extra": False},
            {"over_ball": "0.2", "striker": "Virat Kohli", "runs": 1, "is_wicket": False, "is_extra": False},
            {"over_ball": "0.3", "striker": "Faf du Plessis", "runs": 0, "is_wicket": False, "is_extra": False},
            {"over_ball": "0.4", "striker": "Faf du Plessis", "runs": 6, "is_wicket": False, "is_extra": False},
            {"over_ball": "0.5", "striker": "Faf du Plessis", "runs": 0, "is_wicket": True, "is_extra": False},
            {"over_ball": "0.6", "striker": "Rajat Patidar", "runs": 1, "is_wicket": False, "is_extra": False},
            {"over_ball": "1.1", "striker": "Virat Kohli", "runs": 6, "is_wicket": False, "is_extra": False},
            {"over_ball": "1.2", "striker": "Virat Kohli", "runs": 4, "is_wicket": False, "is_extra": False},
        ]
    }
}

def calculate_batter_scorecard(innings_id: str) -> Optional[Dict[str, Any]]:
    data = MOCK_BALL_DB.get(innings_id)
    if not data:
        return None

    events = data["ball_events"]
    batters_stat = {}

    for b in events:
        striker = b["striker"]
        if striker not in batters_stat:
            batters_stat[striker] = {"runs": 0, "balls": 0, "fours": 0, "sixes": 0, "is_out": False}

        batters_stat[striker]["runs"] += b["runs"]
        if not b.get("is_extra", False):
            batters_stat[striker]["balls"] += 1
        if b["runs"] == 4:
            batters_stat[striker]["fours"] += 1
        elif b["runs"] == 6:
            batters_stat[striker]["sixes"] += 1
        if b["is_wicket"]:
            batters_stat[striker]["is_out"] = True

    batters_list = []
    for name, stats in batters_stat.items():
        sr = round((stats["runs"] / stats["balls"]) * 100, 2) if stats["balls"] > 0 else 0.0
        batters_list.append({
            "name": name,
            "runs": stats["runs"],
            "balls": stats["balls"],
            "fours": stats["fours"],
            "sixes": stats["sixes"],
            "strike_rate": sr,
            "is_out": stats["is_out"]
        })

    return {
        "match_id": data["match_id"],
        "innings_id": innings_id,
        "batting_team": data["batting_team"],
        "batters": batters_list
    }
