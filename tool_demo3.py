# How to run with uv:
#   uv run tool_demo.py
#
# Modify the smolagents dependency to point to the local smolagents repo or
# remove `@ file:////workspaces/smolagents`
#
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "smolagents[mcp,litellm] @ file:////workspaces/smolagents",
#   "pydantic",
# ]
# ///

from smolagents import tool, CodeAgent, LiteLLMModel
from pydantic import BaseModel, Field

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
    return WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    )

# Add output schema attribute to the tool for structured output
get_weather_info.output_schema = {
    "type": "object",
    "properties": {
        "location": {
            "type": "string",
            "description": "The location name"
        },
        "temperature": {
            "type": "number",
            "description": "Temperature in Celsius"
        },
        "conditions": {
            "type": "string",
            "description": "Weather conditions"
        },
        "humidity": {
            "type": "integer",
            "description": "Humidity percentage",
            "minimum": 0,
            "maximum": 100
        }
    },
    "required": ["location", "temperature", "conditions", "humidity"]
}

if __name__ == "__main__":
    # Initialize the model
    model = LiteLLMModel(model_id="gpt-4.1")
    
    # Create agent with structured output enabled internally
    # This allows the agent to understand and use the output_schema of tools
    agent = CodeAgent(
        tools=[get_weather_info], 
        model=model, 
        use_structured_outputs_internally=True
    )
    
    # Test the agent with structured output
    print("=== Weather Agent with Structured Output ===")
    result = agent.run("What's the temperature in fahrenheit like in Paris?")
    print("Agent response:")
    print(result)
    
    # Example of calling the tool directly
    print("\n" + "="*50)
    print("Example of calling the tool directly:")
    weather_data = get_weather_info("Berlin")
    print(f"Location: {weather_data.location}")
    print(f"Temperature: {weather_data.temperature}°C")
    print(f"Conditions: {weather_data.conditions}")
    print(f"Humidity: {weather_data.humidity}%")