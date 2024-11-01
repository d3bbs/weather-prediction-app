# Weather App - Interactive GUI for Current & Weekly Forecasts

Welcome to the **Weather App** project! This interactive Python application provides users with up-to-date weather information and forecasts using a graphical user interface (GUI) built with `tkinter`. The app fetches weather data from the OpenWeatherMap API and displays both the current weather and a 7-day forecast with an intuitive, TV-style design.

---

## 📌 Features

- **Current Weather Information**: Displays the latest temperature, weather description, and date for your chosen city.
- **7-Day Forecast**: Provides detailed weather predictions, including temperature and conditions, for the current and upcoming weeks.

## ⚙️ How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/d3bbs/weather-prediction-app
   ```
2. **Install Dependencies**:
   - Make sure you have Python installed on your system. Then, install the `requests` library if you haven't already:
     ```bash
     pip install requests
     pip install tkinter
     ```
3. **Set Up Your OpenWeatherMap API Key**:
   - Sign up on [OpenWeatherMap](https://openweathermap.org/api) to get your API key.
   - Replace `'your_api_key'` in the script with your actual API key.
4. **Run the Script**:
   ```bash
   python main.py
   ```

---

## 🔧 Configuration

- **API Key**: Make sure to set your OpenWeatherMap API key in the script.
- **City**: Update the `CITY` variable with the city name for which you want to display the weather.  

---

## 📸 Screenshots

![{2D02B18C-5B80-4534-9C22-E2A67D58BB01}](https://github.com/user-attachments/assets/e152015f-902c-4507-bd9f-41f8f391e86f)

---

## 📚 Known Issues
- **Limited Forecast Data**: The app currently retrieves only a limited number of forecast data points, which may not cover a full 7 days in some cases.
- **API Dependency**: The app requires an active internet connection and a valid OpenWeatherMap API key to function properly.

## 🔍 Future Enhancements
- **Customizable City Selection**: Allow users to select different cities within the app.
- **Error Handling**: More robust error handling for API failures or incorrect data input.
- **Weather Icons**: Display weather icons to visually represent different weather conditions.

---

## 👨‍💻 Author

- **Aaron Debattista**: IT Support Officer, Studying Bachelors in Computer Systems and Networks 
- [LinkedIn](https://www.linkedin.com/in/aaron-debattista-932792276/)
- [GitHub](https://github.com/d3bbs)

---

## 💬 Contact

For any inquiries or feedback, please feel free to reach out through [LinkedIn](https://www.linkedin.com/in/aaron-debattista-932792276/).
