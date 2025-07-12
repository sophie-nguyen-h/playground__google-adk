from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """
    Get the weather information for a specific city.
    
    Args:
        city (str): The name of the city
    
    Return:
        dict: status and error msg
    """
    
    if city.lower() == 'new york':
        return {
            'status': 'success',
            'report': 'The tempeture is 85 Fahrenheit.'
        }
    else:
        return {
            'status': 'error',
            'err_msg': f'The weather information is not available for {city.capital()}.'
        }
    
agent = Agent(
    name='weather_agent',
    model=DEFAULT_MODEL,
    description='A helpful weather agent',
    instruction='You are a helpful and polite weather agent.'
                'You ONLY handle request about the weather.'
                'When the user ask about the weather, use the get_weather tool to generate an answer.'
                'If the tool return a success status, you share the report with the user.'
                'If the tool return an error status, you inform the user politely.',
    tools=[get_weather],
)