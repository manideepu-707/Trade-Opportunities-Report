from fastapi import APIRouter, Depends, Request
from core.auth import verify_token
from core.rate_limiter import limiter
from core.session import track_session
from services.data_collector import fetch_market_data
from services.ai_analyzer import analyze_data
from services.report_generator import generate_markdown

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request,sector: str, user: str = Depends(verify_token)):
    
    track_session(user)

    market_data = await fetch_market_data(sector)

    ai_response = await analyze_data(sector, market_data)
    if not ai_response:
        return {"report": "AI analysis failed. Try again later."}

    analysis_text = ai_response

    report = generate_markdown(sector, analysis_text)

    return {"report": report}