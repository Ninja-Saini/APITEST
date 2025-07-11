from fastapi import FastAPI, HTTPException

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

@app.get("/get-capital")
def get_capital(country: str):
    country_lower = country.lower()
    capital = country_capitals.get(country_lower)
    if capital:
        return {"country": country.title(), "capital": capital}
    else:
        raise HTTPException(status_code=404, detail="Country not found")
