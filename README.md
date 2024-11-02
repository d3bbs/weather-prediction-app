
# Weather App - Interactive GUI for Current & Weekly Forecasts

Welcome to the **Weather App** project! This interactive Python application provides users with up-to-date weather information and a 7-day forecast using a graphical user interface (GUI) built with `PyQt5`. The app fetches weather data from the Open-Meteo API and features a modern, card-style design for easy readability and an attractive user experience.

---

## 📌 Features

- **Current Weather Information**: Displays the latest temperature, weather conditions, "Feels Like" temperature, wind speed, and UV index for your selected city.
- **7-Day Forecast**: Provides detailed weather predictions for the next week, including high/low temperatures, weather icons, and additional information.
- **Responsive Design**: Card-like widgets and modern UI elements ensure a visually appealing and intuitive experience.
- **Customizable Background**: Options to modify the background color or use a gradient for a unique look.

---

## 🛠️ Technologies Used

- **Python**: Core programming language for the app.
- **PyQt5**: Used to create the interactive graphical user interface.
- **Open-Meteo API**: Provides real-time and forecast weather data.
- **QPixmap**: Used to load and display weather icons in the GUI.

---

## ⚙️ How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/d3bbs/weather-prediction-app
   ```

2. **Install Dependencies**:
   - Make sure you have Python installed on your system. Then, install the required libraries:
     ```bash
     pip install PyQt5
     pip install requests
     ```

3. **Run the Script**:
   ```bash
   python main.py
   ```

---

## 🔧 Configuration

- **City Search**: Enter the city name in the input field to view the current and 7-day forecast.
- **Weather Icons**: Ensure the weather icons are located in the `icons` folder for proper display.
- **Background Customization**: You can modify the `main_screen.setStyleSheet()` line in the script to change the background color or gradient.

---

## 📸 Screenshots

![{EEF4A587-7E9B-4091-91E6-08816B0FACA8}](https://github.com/user-attachments/assets/daf3ec35-98d4-47d6-93d9-616d5cd43331)


---

## 📚 Known Issues

- **Location Detection**: Automatic location detection is a planned feature but not yet implemented.
- **Limited API Data**: The app currently depends on the Open-Meteo API, which may have limitations in some areas.
- **Error Handling**: Basic error handling is implemented, but improvements are planned for more robust data validation and error messages.

---

## 🔍 Future Enhancements

1. ~~**Hourly Forecast**: Show hourly temperature and weather conditions for better planning.~~
2. **Location Detection**: Automatically detect the user's location and show the weather for that area.
3. **Weather Alerts**: Add notifications for severe weather conditions.
4. **Graphical Temperature Trends**: Use graphs to display temperature trends over the week.
5. **Custom Themes**: Allow users to choose between light and dark themes or customize the interface colors.

---

## 👨‍💻 Author

- **Aaron Debattista**: IT Support Officer, studying a Bachelor’s in Computer Systems and Networks.
- [LinkedIn](https://www.linkedin.com/in/aaron-debattista-932792276/)
- [GitHub](https://github.com/d3bbs)

---

## 💬 Contact

For any inquiries, feedback, or collaboration opportunities, feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/aaron-debattista-932792276/).

---

### Thank you for checking out the Weather App! Enjoy staying updated with the latest weather forecasts.
