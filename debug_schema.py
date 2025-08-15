from pydantic import BaseModel, Field
from smolagents._function_type_hints_utils import get_json_schema

class WeatherInfo(BaseModel):
    location: str = Field(description="The location name")
    temperature: float = Field(description="Temperature in Celsius")
    conditions: str = Field(description="Weather conditions")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)

def get_weather_info(city: str) -> WeatherInfo:
    """Get weather information for a city.
    
    Args:
        city: The name of the city to get weather information for
        
    Returns:
        Weather information including temperature, conditions and humidity
    """
    return WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    ).model_dump()

print("=== Full JSON Schema ===")
import json
schema = get_json_schema(get_weather_info)
print(json.dumps(schema, indent=2))
