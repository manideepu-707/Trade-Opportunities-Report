import os
import asyncio
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv("key")

client = genai.Client(api_key=GEMINI_API_KEY)


async def analyze_data(sector, data):
    prompt = f"""
    Analyze the Indian {sector} sector.

    Data:
    {data}

    Give:
    - Market Overview
    - Opportunities
    - Risks
    """

    try:
        # ✅ run sync function safely in async
        response = await asyncio.to_thread(
            client.models.generate_content,
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("AI ERROR:", e)
        return "AI analysis failed"