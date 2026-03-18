import httpx

async def fetch_market_data(sector: str):
    url = f"https://api.duckduckgo.com/?q={sector}+india+market&format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    data = response.json()
    
    return data.get("RelatedTopics", [])[:5]