import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QStackedWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from datetime import datetime

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 800, 600)

        # Stacked widget to manage multiple views
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialize the home screen, today's forecast, and 7-day forecast views
        self.init_home_screen()
        self.init_today_forecast()
        self.init_week_forecast()

        # Test to check if the icon loads
        self.test_icon_loading()

    def init_home_screen(self):
        home_screen = QWidget()
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the Weather App", alignment=Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")
        layout.addWidget(welcome_label)

        start_button = QPushButton("Get Started")
        start_button.setStyleSheet("font-size: 18px; padding: 10px; background-color: #007ACC; color: white; border-radius: 5px;")
        start_button.clicked.connect(self.show_today_forecast)
        layout.addWidget(start_button, alignment=Qt.AlignCenter)

        home_screen.setLayout(layout)
        home_screen.setStyleSheet("""
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #87CEEB, stop: 1 #4682B4
            );
        """)
        self.stacked_widget.addWidget(home_screen)

    def init_today_forecast(self):
        today_forecast = QWidget()
        layout = QVBoxLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        self.city_input.setStyleSheet("font-size: 16px; padding: 10px; border-radius: 5px;")
        layout.addWidget(self.city_input)

        search_button = QPushButton("Search Weather")
        search_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #007ACC; color: white; border-radius: 5px;")
        search_button.clicked.connect(self.search_weather)
        layout.addWidget(search_button)

        button_layout = QHBoxLayout()
        today_button = QPushButton("Today's Forecast")
        today_button.clicked.connect(self.show_today_forecast)
        week_button = QPushButton("7-Day Forecast")
        week_button.clicked.connect(self.show_week_forecast)
        button_layout.addWidget(today_button)
        button_layout.addWidget(week_button)
        layout.addLayout(button_layout)

        self.hourly_forecast_container = QHBoxLayout()
        self.hourly_forecast_container.setSpacing(15)
        self.hourly_widgets = []

        for _ in range(8):
            hour_widget = self.create_hour_widget()
            self.hourly_forecast_container.addWidget(hour_widget)
            self.hourly_widgets.append(hour_widget)

        layout.addLayout(self.hourly_forecast_container)
        today_forecast.setLayout(layout)
        today_forecast.setStyleSheet("""
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #87CEEB, stop: 1 #4682B4
            );
        """)
        self.stacked_widget.addWidget(today_forecast)

    def init_week_forecast(self):
        week_forecast = QWidget()
        layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        today_button = QPushButton("Today's Forecast")
        today_button.clicked.connect(self.show_today_forecast)
        week_button = QPushButton("7-Day Forecast")
        week_button.clicked.connect(self.show_week_forecast)
        button_layout.addWidget(today_button)
        button_layout.addWidget(week_button)
        layout.addLayout(button_layout)

        self.forecast_container = QHBoxLayout()
        self.forecast_container.setSpacing(15)
        self.forecast_widgets = []

        for _ in range(7):
            day_widget = self.create_day_widget()
            self.forecast_container.addWidget(day_widget)
            self.forecast_widgets.append(day_widget)

        layout.addLayout(self.forecast_container)
        week_forecast.setLayout(layout)
        week_forecast.setStyleSheet("""
            background: qlineargradient(
                spread: pad,
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 #87CEEB, stop: 1 #4682B4
            );
        """)
        self.stacked_widget.addWidget(week_forecast)

    def create_hour_widget(self):
        hour_widget = QWidget()
        layout = QVBoxLayout()

        time_label = QLabel("Time", alignment=Qt.AlignCenter)
        time_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        layout.addWidget(time_label)

        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        temp_label = QLabel("Temp: 0°C", alignment=Qt.AlignCenter)
        temp_label.setStyleSheet("font-size: 12px; color: #ECF0F1;")
        layout.addWidget(temp_label)

        hour_widget.setLayout(layout)
        hour_widget.setStyleSheet("background-color: #34495E; border-radius: 10px; padding: 10px; border: 1px solid #2C3E50;")
        return hour_widget

    def create_day_widget(self):
        day_widget = QWidget()
        layout = QVBoxLayout()

        day_label = QLabel("Day", alignment=Qt.AlignCenter)
        day_label.setStyleSheet("font-size: 14px; font-weight: bold; color: white;")
        layout.addWidget(day_label)

        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        temp_label = QLabel("High: 0°C / Low: 0°C", alignment=Qt.AlignCenter)
        temp_label.setStyleSheet("font-size: 12px; color: #ECF0F1;")
        layout.addWidget(temp_label)

        day_widget.setLayout(layout)
        day_widget.setStyleSheet("background-color: #34495E; border-radius: 10px; padding: 10px; border: 1px solid #2C3E50;")
        return day_widget

    def test_icon_loading(self):
        # Test to see if the "clear_sky.png" icon loads correctly
        test_icon_label = QLabel()
        icon_path = os.path.abspath(os.path.join("icons", "clear_sky.png"))
        print("Testing Icon Path:", icon_path)  # Debugging statement
        pixmap = QPixmap(icon_path)
        if pixmap.isNull():
            print("Failed to load test image: clear_sky.png")
        else:
            print("Test image loaded successfully: clear_sky.png")

    def show_today_forecast(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_week_forecast(self):
        self.stacked_widget.setCurrentIndex(2)

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

            # Fetch hourly and daily forecasts
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto"
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            if "hourly" in weather_data and "daily" in weather_data:
                # Update hourly forecast
                hourly_data = weather_data["hourly"]["temperature_2m"][:8]
                for i, temp in enumerate(hourly_data):
                    hour_widget = self.hourly_widgets[i]
                    time_label = hour_widget.layout().itemAt(0).widget()
                    icon_label = hour_widget.layout().itemAt(1).widget()
                    temp_label = hour_widget.layout().itemAt(2).widget()

                    time_label.setText(f"{i}:00")
                    temp_label.setText(f"Temp: {temp}°C")

                    # Set the icon
                    weather_code = 0  # Placeholder for actual hourly weather code
                    icon_path = self.get_weather_icon_path(weather_code)
                    print(f"Hourly Icon Path ({i}): {icon_path}")  # Debugging statement

                    if os.path.exists(icon_path):
                        pixmap = QPixmap(icon_path)
                        if pixmap.isNull():
                            print(f"Failed to load icon: {icon_path}")
                        else:
                            icon_label.setPixmap(pixmap)
                    else:
                        print(f"Icon file does not exist: {icon_path}")
                        icon_label.clear()

                # Update 7-day forecast
                daily_forecast = weather_data["daily"]
                dates = daily_forecast["time"]
                temps_max = daily_forecast["temperature_2m_max"]
                temps_min = daily_forecast["temperature_2m_min"]
                weather_codes = daily_forecast["weathercode"]

                for i in range(7):
                    day_widget = self.forecast_widgets[i]
                    day_label = day_widget.layout().itemAt(0).widget()
                    icon_label = day_widget.layout().itemAt(1).widget()
                    temp_label = day_widget.layout().itemAt(2).widget()

                    day_name = datetime.strptime(dates[i], '%Y-%m-%d').strftime('%A')
                    day_label.setText(day_name)
                    temp_label.setText(f"High: {temps_max[i]}°C / Low: {temps_min[i]}°C")

                    # Set the icon
                    icon_path = self.get_weather_icon_path(weather_codes[i])
                    print(f"Daily Icon Path ({i}): {icon_path}")  # Debugging statement

                    if os.path.exists(icon_path):
                        pixmap = QPixmap(icon_path)
                        icon_label.setPixmap(pixmap)
                    else:
                        icon_label.clear()
            else:
                QMessageBox.critical(self, "Error", "Error fetching weather data.")
        else:
            QMessageBox.critical(self, "Error", "City not found. Please enter a valid city name.")

    def get_weather_icon_path(self, weather_code):
        icon_mapping = {
            0: "clear_sky.png",
            1: "partly_cloudy.png",
            2: "partly_cloudy.png",
            3: "overcast.png",
            45: "fog.png",
            48: "fog.png",
            51: "drizzle.png",
            53: "drizzle.png",
            55: "drizzle.png",
            61: "rain.png",
            63: "rain.png",
            65: "rain.png",
            80: "rain_showers.png",
            81: "rain_showers.png",
            82: "rain_showers.png",
            95: "thunderstorm.png",
            96: "thunderstorm.png",
            99: "thunderstorm.png"
        }
        icon_file = icon_mapping.get(weather_code, "unknown.png")
        return os.path.join("icons", icon_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
