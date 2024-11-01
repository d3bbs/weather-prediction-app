import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QStackedWidget, QMessageBox
from PyQt5.QtCore import Qt

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 600)

        # Stacked widget to manage multiple screens
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialize the start screen and main screen
        self.init_start_screen()
        self.init_main_screen()

    def init_start_screen(self):
        # Start screen setup
        start_screen = QWidget()
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the Weather App", alignment=Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(welcome_label)

        start_button = QPushButton("Get Started")
        start_button.setStyleSheet("font-size: 16px; padding: 10px;")
        start_button.clicked.connect(self.show_main_screen)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        start_screen.setLayout(layout)
        self.stacked_widget.addWidget(start_screen)

    def init_main_screen(self):
        # Main weather screen setup
        main_screen = QWidget()
        layout = QVBoxLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setStyleSheet("font-size: 16px; padding: 5px;")
        layout.addWidget(self.city_input)

        search_button = QPushButton("Search Weather")
        search_button.setStyleSheet("font-size: 16px; padding: 10px;")
        search_button.clicked.connect(self.search_weather)
        layout.addWidget(search_button)

        self.weather_label = QLabel("", alignment=Qt.AlignCenter)
        self.weather_label.setStyleSheet("font-size: 14px; margin-top: 20px;")
        layout.addWidget(self.weather_label)

        main_screen.setLayout(layout)
        self.stacked_widget.addWidget(main_screen)

    def show_main_screen(self):
        self.stacked_widget.setCurrentIndex(1)

    def search_weather(self):
        city = self.city_input.text()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return

        # Fetch weather data using Open-Meteo API
        geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geocoding_response = requests.get(geocoding_url)
        geocoding_data = geocoding_response.json()

        if "results" in geocoding_data and geocoding_data["results"]:
            latitude = geocoding_data["results"][0]["latitude"]
            longitude = geocoding_data["results"][0]["longitude"]

            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            if "current_weather" in weather_data:
                current_weather = weather_data["current_weather"]
                temperature = current_weather["temperature"]
                weather_code = current_weather["weathercode"]
                self.weather_label.setText(f"City: {city}\nTemperature: {temperature}°C\nWeather Code: {weather_code}")
            else:
                QMessageBox.critical(self, "Error", "Error fetching weather data.")
        else:
            QMessageBox.critical(self, "Error", "City not found. Please enter a valid city name.")

# Main entry point of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
