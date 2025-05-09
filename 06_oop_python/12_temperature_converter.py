# Create a class TemperatureConverter
class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Convert Celsius to Fahrenheit

# Convert 25°C to Fahrenheit
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)

# Print the result
print("25°C is equal to", fahrenheit, "°F")
