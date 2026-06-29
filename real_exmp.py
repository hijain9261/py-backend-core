import asyncio, time
from typing import Dict,List
import httpx
from pydantic import BaseModel, Field

# Performance Profiling Decorator
def async_timer(func): 
    async def wrapper(*args, **kwargs):
        start = time.time() # Start time 
        result = func(*args, **kwargs)

        if asyncio.iscoroutine(result): # if result is coroutine then wait otherwise end
            result = await result
        end = time.time()

        print(f"Time for {func.__name__} execution is {end-start: .4f} seconds")
        return result 
    
    return wrapper

# Pydantic based Schema
class weatherMetrics(BaseModel):
    temperature: float = Field(alias = "temperature")
    wind_speed: float = Field(alias = "windspeed")

class LocationPayload(BaseModel):
    city: str
    latitude: float
    longitude: float
    current_weather: weatherMetrics

# Function to actually fetch city weather
async def fetch_city_weather(client: httpx.AsyncClient, city: str, lat: float, lon:float) -> LocationPayload:
    url = "https://api.open-meteo.com/v1/forecast"
    parameter = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    print(f" Request sent for {city}...")
    response = await client.get(url, params = parameter)
    print(f"✅ Raw bytes returned from {city} server")
    raw_json = response.json()

    raw_json["current_weather"]["city"] = city
    raw_json["current_weather"]["latitude"] = lat
    raw_json["current_weather"]["longitude"] = lon

    return LocationPayload(
        city = city,
        latitude=lat,
        longitude=lon,
        current_weather=weatherMetrics(**raw_json["current_weather"])
    )

@async_timer
async def execute_pipeline():
    exmpls = [
        {"city": "Kolkata", "lat": 22.5726, "lon": 88.3639},
        {"city": "London", "lat": 51.5074, "lon": -0.1278},
        {"city": "San Francisco", "lat": 37.7749, "lon": -122.4194}
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_city_weather(client, each["city"], each["lat"], each["lon"]) 
                 for each in exmpls]
        
        validated_payloads: List[LocationPayload] = await asyncio.gather(*tasks)
    for payload in validated_payloads:
        print(payload, "\n\n\n")
        

if __name__ == "__main__":
    asyncio.run(execute_pipeline())
