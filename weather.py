from abc import ABC, abstractmethod

# Strategy Interface: DisplayStrategy
class weather(ABC):
    @abstractmethod
    def display(self, temperature):
        pass

# Concrete Strategy: CelsiusDisplay
class CelsiusDisplay(DisplayStrategy):
    def display(self, temperature):
        print(f"Temperature: {temperature}°C")

# Concrete Strategy: FahrenheitDisplay
class FahrenheitDisplay(DisplayStrategy):
    def display(self, temperature):
        fahrenheit = (temperature * 9/5) + 32
        print(f"Temperature: {fahrenheit}°F")

# Concrete Strategy: KelvinDisplay
class KelvinDisplay(DisplayStrategy):
    def display(self, temperature):
        kelvin = temperature + 273.15
        print(f"Temperature: {kelvin} K")

# Context: WeatherStation
class WeatherStation:
    def __init__(self, strategy: DisplayStrategy):
        self._temperature = None
        self._strategy = strategy

    # Set a new display strategy dynamically
    def set_display_strategy(self, strategy: DisplayStrategy):
        self._strategy = strategy

    # Set the temperature and display it according to the current strategy
    def set_temperature(self, temperature):
        self._temperature = temperature
        print(f"WeatherStation: New temperature recorded: {temperature}°C")
        self._strategy.display(self._temperature)

# Test the Strategy Pattern with WeatherStation

# Create a WeatherStation with Celsius display strategy
weather_station = WeatherStation(CelsiusDisplay())

# Set the temperature and display in Celsius
weather_station.set_temperature(25)
# Output: Temperature: 25°C

# Change the display strategy to Fahrenheit and display the temperature
weather_station.set_display_strategy(FahrenheitDisplay())
weather_station.set_temperature(25)
# Output: Temperature: 77.0°F

# Change the display strategy to Kelvin and display the temperature
weather_station.set_display_strategy(KelvinDisplay())
weather_station.set_temperature(25)
# Output: Temperature: 298.15 K
