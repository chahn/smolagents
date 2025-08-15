from pydantic import BaseModel, Field
from smolagents import CodeAgent, LiteLLMModel, tool

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
    # Create the Pydantic model internally for validation and type safety
    weather_model = WeatherInfo(
        location=city,
        temperature=22.5,
        conditions="partly cloudy",
        humidity=65
    )
    # Return as dictionary for agent dictionary access
    return weather_model.model_dump()

# 🎉 The output_schema is now AUTOMATICALLY detected from the -> WeatherInfo type annotation!
# No manual assignment needed: get_weather_info.output_schema = WeatherInfo.model_json_schema()

if __name__ == "__main__":
    # Let's first verify the automatic schema detection worked
    print("=== Automatic Pydantic Schema Detection ===")
    import json
    print("✅ output_schema automatically extracted:")
    print(json.dumps(get_weather_info.output_schema, indent=2))
    
    # Initialize the model
    model = LiteLLMModel(model_id="gpt-4.1")
    
    # Create agent  
    agent = CodeAgent(
        tools=[get_weather_info], 
        model=model
    )
    
    # Test the agent with structured output
    print("\n=== Weather Agent with Automatic Schema ===")
    result = agent.run("What's the temperature in fahrenheit like in Paris?")
    print(f"Agent response:\n{result}")
    
    print("\n" + "="*50)
    print("Example of calling the tool directly:")
    weather_data = get_weather_info("Berlin")
    print(f"Location: {weather_data['location']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Conditions: {weather_data['conditions']}")
    print(f"Humidity: {weather_data['humidity']}%")
    
    print("\n" + "="*50)
    print("Testing dictionary access:")
    print(f"weather_data['temperature']: {weather_data['temperature']}°C")
    print(f"weather_data['location']: {weather_data['location']}")
    print(f"'temperature' in weather_data: {'temperature' in weather_data}")
    print(f"weather_data.keys(): {list(weather_data.keys())}")
    print(f"weather_data.values(): {list(weather_data.values())}")
    print("weather_data.items():")
    for key, value in weather_data.items():
        print(f"  {key}: {value}")
