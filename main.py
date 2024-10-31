import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# OpenWeatherMap API details
API_KEY = 'enter_your_api_key_here'
CITY = 'Attard, MT'
def fetch_weather():
    # Fetch current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    current_weather = response.json()

    # Fetch forecast data for the week
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    if current_weather.get("cod") == 200 and forecast_data.get("cod") == "200":
        # Extract current weather details
        city = current_weather["name"]
        temperature = current_weather["main"]["temp"]
        weather_description = current_weather["weather"][0]["description"]
        date = datetime.fromtimestamp(current_weather["dt"]).strftime('%Y-%m-%d %H:%M:%S')

        # Display current weather information
        global weather_info
        weather_info = (
            f"City: {city}\n\n"
            f"Date: {date}\n\n"
            f"Temperature: {temperature}°C\n\n"
            f"Description: {weather_description.capitalize()}"
        )
        
        # Extract forecast details for the current week
        global current_week_forecast
        current_week_forecast = "Weather Forecast for This Week:\n\n"
        for item in forecast_data["list"][:5]:  # Limit to next 5 entries
            forecast_date = datetime.fromtimestamp(item["dt"]).strftime('%a, %Y-%m-%d %H:%M')
            forecast_temp = item["main"]["temp"]
            forecast_desc = item["weather"][0]["description"]
            current_week_forecast += f"{forecast_date}: {forecast_temp}°C, {forecast_desc.capitalize()}\n\n"

        # Extract forecast details for the next week
        global next_week_forecast
        next_week_forecast = "Weather Forecast for Next Week:\n\n"
        for item in forecast_data["list"][5:10]:  # Adjust to get entries for next week
            forecast_date = datetime.fromtimestamp(item["dt"]).strftime('%a, %Y-%m-%d %H:%M')
            forecast_temp = item["main"]["temp"]
            forecast_desc = item["weather"][0]["description"]
            next_week_forecast += f"{forecast_date}: {forecast_temp}°C, {forecast_desc.capitalize()}\n\n"

        # Show the current week's forecast by default
        weather_label.config(text=weather_info)
        forecast_label.config(text=current_week_forecast)
    else:
        messagebox.showerror("Error", "Error fetching weather data")

def show_current_week_forecast():
    forecast_label.config(text=current_week_forecast)

def show_next_week_forecast():
    forecast_label.config(text=next_week_forecast)

# Set up the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("600x700")
root.configure(bg="#34495E")

# Title Label
title_label = tk.Label(root, text="Weather Forecast", font=("Helvetica", 24, "bold"), fg="white", bg="#34495E")
title_label.pack(pady=20)

# Frame for Current Weather
current_frame = tk.Frame(root, bg="#1ABC9C", bd=10, relief="ridge")
current_frame.pack(pady=15, fill="x", padx=30)

# Current Weather Label
current_label_title = tk.Label(current_frame, text="Current Weather", font=("Helvetica", 16, "bold"), bg="#1ABC9C", fg="white")
current_label_title.pack(anchor="w", padx=15, pady=10)

weather_label = tk.Label(current_frame, text="", font=("Helvetica", 14, "bold"), justify="left", bg="#1ABC9C", fg="white", padx=10, pady=10)
weather_label.pack(anchor="w", padx=15, pady=5)

# Frame for Forecast
forecast_frame = tk.Frame(root, bg="#3498DB", bd=10, relief="ridge")
forecast_frame.pack(pady=15, fill="x", padx=30)

# Forecast Title Label
forecast_label_title = tk.Label(forecast_frame, text="Forecast", font=("Helvetica", 16, "bold"), bg="#3498DB", fg="white")
forecast_label_title.pack(anchor="w", padx=15, pady=10)

forecast_label = tk.Label(forecast_frame, text="", font=("Helvetica", 14, "bold"), justify="left", bg="#3498DB", fg="white", padx=10, pady=10)
forecast_label.pack(anchor="w", padx=15, pady=5)

# Buttons to Toggle Forecasts
button_frame = tk.Frame(root, bg="#34495E")
button_frame.pack(pady=10)

current_week_button = tk.Button(button_frame, text="This Week", font=("Helvetica", 12, "bold"), command=show_current_week_forecast)
current_week_button.pack(side="left", padx=20)

next_week_button = tk.Button(button_frame, text="Next Week", font=("Helvetica", 12, "bold"), command=show_next_week_forecast)
next_week_button.pack(side="left", padx=20)

# Fetch and display the weather information
fetch_weather()

# Run the GUI loop
root.mainloop()