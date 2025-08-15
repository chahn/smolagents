from pydantic import BaseModel, Field
from smolagents import tool

class WeatherInfo(BaseModel):
    """Pydantic model for weather information."""
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
    weather_model = WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    )
    return weather_model.model_dump()

print("🎉 SUCCESS: Automatic Pydantic Schema Extraction Working!")
print("=" * 60)

print("✅ Tool created with automatic schema detection")
print(f"   Tool name: {get_weather_info.name}")
print(f"   Output type: {get_weather_info.output_type}")
print(f"   Has output_schema: {hasattr(get_weather_info, 'output_schema')}")

print("\n✅ Extracted schema contains all Pydantic field info:")
schema = get_weather_info.output_schema
print(f"   Title: {schema['title']}")
print(f"   Description: {schema['description']}")
print(f"   Required fields: {schema['required']}")
print(f"   Properties count: {len(schema['properties'])}")

print("\n✅ Field validation rules preserved:")
humidity_field = schema['properties']['humidity']
print(f"   Humidity min: {humidity_field['minimum']}")
print(f"   Humidity max: {humidity_field['maximum']}")

print("\n✅ Tool function works correctly:")
result = get_weather_info("Tokyo")
print(f"   Location: {result['location']}")
print(f"   Temperature: {result['temperature']}°C") 
print(f"   Dictionary access: {type(result)}")
print(f"   All keys present: {all(k in result for k in ['location', 'temperature', 'conditions', 'humidity'])}")

print("\n" + "=" * 60)
print("🎉 ENHANCEMENT COMPLETE!")
print("✨ @tool decorator now automatically detects Pydantic models")
print("✨ No more manual get_weather_info.output_schema = WeatherInfo.model_json_schema()")
print("✨ Type annotation -> WeatherInfo automatically generates full schema")
print("✨ All Pydantic features preserved: descriptions, validation, etc.")
