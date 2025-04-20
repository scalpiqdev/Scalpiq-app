from fastapi import APIRouter
from pydantic import BaseModel
import yfinance as yf
from backend.modules.planner.companion_planner import generate_trade_plan

router = APIRouter()

class PlannerRequest(BaseModel):
    ticker: str

@router.post("/planner/generate")
def generate_plan(req: PlannerRequest):
    try:
        stock = yf.Ticker(req.ticker.upper())
        hist = stock.history(period="2d", interval="1d")

        if hist.shape[0] < 2:
            return {"error": "Not enough historical data"}

        prev_close = hist.iloc[-2]['Close']
        today_open = hist.iloc[-1]['Open']
        high = hist.iloc[-1]['High']
        low = hist.iloc[-1]['Low']

        premarket_gap = ((today_open - prev_close) / prev_close) * 100
        support = round(low - 1, 2)
        resistance = round(high + 1, 2)
        trend = "bullish" if today_open > prev_close else "bearish"

        plan = generate_trade_plan(
            premarket_gap=premarket_gap,
            prev_close=prev_close,
            high=high,
            low=low,
            support=support,
            resistance=resistance,
            trend=trend
        )
        return plan
    except Exception as e:
        return {"error": str(e)}