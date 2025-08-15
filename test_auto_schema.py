# Test script to verify automatic Pydantic schema extraction
# How to run with uv:
#   uv run test_auto_schema.py

# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "smolagents[mcp,litellm] @ file:////workspaces/smolagents",
#   "pydantic",
# ]
# ///

from smolagents import tool, CodeAgent, LiteLLMModel
from pydantic import BaseModel, Field
import json

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
    """
    # Create the Pydantic model internally for validation and type safety
    weather_model = WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    )
    # Return as dictionary for agent dictionary access
    return weather_model.model_dump()

if __name__ == "__main__":
    print("=== Debugging Pydantic Detection ===")
    
    # Let's test the Pydantic detection logic directly
    from typing import get_type_hints
    
    hints = get_type_hints(get_weather_info.forward.__wrapped__)
    return_type = hints['return']
    print(f"Return type: {return_type}")
    print(f"Type of return_type: {type(return_type)}")
    print(f"Is it a type? {isinstance(return_type, type)}")
    
    # Test our Pydantic detection
    try:
        from pydantic import BaseModel
        print(f"Pydantic imported successfully")
        print(f"Is subclass of BaseModel? {issubclass(return_type, BaseModel)}")
        if issubclass(return_type, BaseModel):
            schema = return_type.model_json_schema()
            print(f"Generated schema: {schema}")
    except (ImportError, TypeError) as e:
        print(f"Error in Pydantic detection: {e}")
    
    # Test our _get_json_schema_type function directly
    from smolagents._function_type_hints_utils import _get_json_schema_type
    result = _get_json_schema_type(return_type)
    print(f"Result from _get_json_schema_type: {result}")
    
    # Test with agent
    model = LiteLLMModel(model_id="gpt-4.1")
    agent = CodeAgent(tools=[get_weather_info], model=model)
    
    print("\n=== Testing Agent with Auto-Generated Schema ===")
    result = agent.run("What's the temperature in fahrenheit like in Paris?")
    print("Agent response:")
    print(result)
