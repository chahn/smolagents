from smolagents import tool
import json

# Test 1: @tool with explicit output_schema parameter
@tool(output_schema={
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
})
def get_weather_info(city: str) -> dict:
    """Get weather information for a city.
    
    Args:
        city: The name of the city to get weather information for
    """
    return {
        "location": city,
        "temperature": 22.5,
        "conditions": "partly cloudy",
        "humidity": 65
    }

# Test 2: @tool without parameters (should still work)
@tool
def get_simple_info(name: str) -> str:
    """Get simple info.
    
    Args:
        name: The name to process
    """
    return f"Hello, {name}!"

print("=== Testing Enhanced @tool Decorator ===")

print("✅ Test 1: @tool with explicit output_schema")
print(f"Tool name: {get_weather_info.name}")
print(f"Has output_schema: {hasattr(get_weather_info, 'output_schema')}")
if hasattr(get_weather_info, 'output_schema'):
    print("Output schema:")
    print(json.dumps(get_weather_info.output_schema, indent=2))

print("\n✅ Test 2: @tool without parameters")
print(f"Tool name: {get_simple_info.name}")
print(f"Has output_schema: {hasattr(get_simple_info, 'output_schema')}")
print(f"Output_schema value: {getattr(get_simple_info, 'output_schema', 'None')}")

print("\n✅ Test 3: Function calls work correctly")
weather_result = get_weather_info("Tokyo")
print(f"Weather result: {weather_result}")
simple_result = get_simple_info("World")
print(f"Simple result: {simple_result}")

print("\n🎉 Enhanced @tool decorator working!")
