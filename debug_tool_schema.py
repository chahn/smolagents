from pydantic import BaseModel, Field
from smolagents import tool

class WeatherInfo(BaseModel):
    location: str = Field(description="The location name")
    temperature: float = Field(description="Temperature in Celsius")
    conditions: str = Field(description="Weather conditions")
    humidity: int = Field(description="Humidity percentage", ge=0, le=100)

@tool
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

print("=== Tool Analysis ===")
print(f"Tool name: {get_weather_info.name}")
print(f"Tool output_type: {get_weather_info.output_type}")
print(f"Tool output_schema: {get_weather_info.output_schema}")
print(f"Tool has output_schema attr: {hasattr(get_weather_info, 'output_schema')}")

# Check class attributes
print(f"\n=== Class Analysis ===")
print(f"Class output_schema: {getattr(get_weather_info.__class__, 'output_schema', 'NOT_FOUND')}")
print(f"Instance output_schema: {getattr(get_weather_info, 'output_schema', 'NOT_FOUND')}")

# Check JSON schema
from smolagents._function_type_hints_utils import get_json_schema
import json
print(f"\n=== JSON Schema Analysis ===")
schema = get_json_schema(get_weather_info.forward.__wrapped__)
print(f"Has return: {'return' in schema['function']}")
if 'return' in schema['function']:
    return_info = schema['function']['return']
    print(f"Return type: {return_info.get('type')}")
    print(f"Has schema: {'schema' in return_info}")
    if 'schema' in return_info:
        print("Schema found!")
        print(json.dumps(return_info['schema'], indent=2))
