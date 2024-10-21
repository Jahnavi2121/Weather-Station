class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"Weather Station: Setting temperature to {temperature}°C")
        self._temperature = temperature
        self.notify_observers()

class TemperatureDisplay:
    def update(self, temperature):
        print(f"Temperature Display: Current temperature is {temperature}°C")

class MobileApp:
    def update(self, temperature):
        print(f"Mobile App: Alert! The temperature is now {temperature}°C")

# Test the Observer pattern
weather_station = WeatherStation()

# Create two observers
display = TemperatureDisplay()
mobile_app = MobileApp()

# Register the observers
weather_station.add_observer(display)
weather_station.add_observer(mobile_app)

# Change temperature and notify observers
weather_station.set_temperature(25)
weather_station.set_temperature(30)
