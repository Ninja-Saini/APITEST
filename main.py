from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Hardcoded country-capital data
country_capitals = {
    "india": "New Delhi",
    "united states": "Washington, D.C.",
    "france": "Paris",
    "germany": "Berlin",
    "japan": "Tokyo",
    "canada": "Ottawa",
    "australia": "Canberra",
    "brazil": "Brasília",
    "china": "Beijing"
}

# Request body model
class CountryRequest(BaseModel):
    country: str

# POST endpoint to get capital from body
@app.post("/get-capital")
def get_capital(request: CountryRequest):
    country_lower = request.country.lower()
    capital = country_capitals.get(country_lower)
    if capital:
        return {"country": request.country.title(), "capital": capital}
    else:
        raise HTTPException(status_code=404, detail="Country not found")
