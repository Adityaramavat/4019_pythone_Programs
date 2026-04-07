class Temperature:
    
    def convertFahrenheit(self, celsius):
        """Converts Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32

    def convertCelsius(self, fahrenheit):
        """Converts Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

temp = Temperature()

# Convert 0°C to Fahrenheit
print(f"0°C in Fahrenheit is: {temp.convertFahrenheit(0)}")

# Convert 32°F to Celsius
print(f"32°F in Celsius is: {temp.convertCelsius(32)}")