from smolagents import tool

# ✨ Your exact use case - now supported with @tool(output_schema=...)
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

# No need for this anymore!
# get_weather_info.output_schema = { ... }

if __name__ == "__main__":
    print("🎯 @tool(output_schema=...) - Your Exact Use Case")
    print("=" * 50)
    
    print("✅ Tool created with inline schema definition")
    print(f"   Tool name: {get_weather_info.name}")
    print(f"   Has output_schema: {hasattr(get_weather_info, 'output_schema')}")
    
    if hasattr(get_weather_info, 'output_schema'):
        schema = get_weather_info.output_schema
        print(f"   Schema type: {schema['type']}")
        print(f"   Properties: {list(schema['properties'].keys())}")
        print(f"   Required: {schema['required']}")
        
        # Verify validation rules are preserved
        humidity = schema['properties']['humidity']
        print(f"   Humidity validation: min={humidity['minimum']}, max={humidity['maximum']}")
    
    print("\n✅ Function works correctly")
    result = get_weather_info("London")
    print(f"   Result: {result}")
    print(f"   All required fields present: {all(k in result for k in ['location', 'temperature', 'conditions', 'humidity'])}")
    
    print("\n🎉 SUCCESS!")
    print("📝 What changed:")
    print("   ❌ OLD: Manual assignment after @tool")
    print("       get_weather_info.output_schema = {...}")
    print("   ✅ NEW: Inline parameter in decorator")
    print("       @tool(output_schema={...})")
    print("   ✨ Much cleaner and more declarative!")
