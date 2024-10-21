# Design_Patterns
*I have used two design patterns:

-DisplayStrategy Pattern
-Oberserver Pattern

-I have used python as my programming language 

-Topic: The topic is Weather Station 

The WeatherStation class holds a reference to an instance of DisplayStrategy. This means it can utilize any of the concrete display strategies (CelsiusDisplay, FahrenheitDisplay, or any other future strategies).
It doesn't need a direct connection to CelsiusDisplay or FahrenheitDisplay because it interacts with them through the DisplayStrategy interface.

-DisplayStrategy Interface:
The DisplayStrategy interface defines the display(temperature) method that all display strategies must implement.
When WeatherStation calls the display method, it uses the current strategy, which could be any class implementing the DisplayStrategy interface, including CelsiusDisplay or FahrenheitDisplay.

-Observer Pattern:
The Observer interface (and its concrete implementations, TemperatureDisplay and ForecastDisplay) is separate from the display strategy logic. These classes listen for temperature updates from the WeatherStation and act accordingly.
