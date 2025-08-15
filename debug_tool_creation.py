from pydantic import BaseModel, Field
from smolagents import tool

class WeatherInfo(BaseModel):
    location: str = Field(description="The location name")
    temperature: float = Field(description="Temperature in Celsius")
    conditions: str = Field(description="Weather conditions")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)

@tool
def get_weather_info(city: str) -> WeatherInfo:
    """
    Get the current weather information for a given city.
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        Weather information for the specified city
    """
    # This is a mock function for testing
    return WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    ).model_dump()

print("=== Creating tool ===")
print(f"Tool created: {get_weather_info}")
print(f"Tool name: {get_weather_info.name}")
print(f"Tool description: {get_weather_info.description}")
print(f"Tool inputs: {get_weather_info.inputs}")
print(f"Tool output_schema: {getattr(get_weather_info, 'output_schema', 'Not found')}")
print("Tool attributes:", dir(get_weather_info))
