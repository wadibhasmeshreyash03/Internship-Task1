Name : Shreyash Rajendra Wadibhasme
Company : Codtech IT solutions
Id : CT08DG1782
Domain : Python programming
Duration : june to august 2025
Mentor : Neela Santosh Kumar 


##**Project Overview: Weather Data Visualization**
![taskpho2](https://github.com/user-attachments/assets/67807014-e459-4395-856c-5baeda64faf5)
![taskpho3](https://github.com/user-attachments/assets/179fa5cb-87c6-47c8-8e86-819a09cb7ed8)
![taskpho4](https://github.com/user-attachments/assets/c22aeec4-3baf-41bf-978d-3f76465947bd)


### **Objective**

The project fetches real-time **5-day weather forecast data** from the OpenWeatherMap API and visualizes it using **Matplotlib** and **Seaborn**. It provides users with insights into temperature, humidity, and weather conditions for a selected city.

### **Key Components**

1. **Data Collection**

   * Uses the OpenWeatherMap API (`requests` library) to fetch weather forecast data in 3-hour intervals.
   * The user is prompted to **enter a city name**.
   * Data includes:
     * Temperature
     * Humidity
     * Weather conditions (e.g., clear, cloudy, rainy).

2. **Data Processing**
   * Extracts:
     * **Dates & times** (`datetime` module)
     * **Temperatures**
     * **Humidity levels**
     * **Weather descriptions**
   * Stores them in lists for plotting.

3. **Data Visualization**
   * **Temperature Trend Plot** – Line chart showing temperature changes over time.
   * **Humidity Trend Plot** – Line chart showing humidity variation over time.
   * **Weather Condition Frequency** – Bar chart (via `Seaborn countplot`) showing how often each condition occurs.

4. **User Interaction**
   * Program runs via command-line.
   * User enters city name.
   * Dashboard with three visualizations is generated.

### **Technologies Used**

* **Python**
* **Requests** → API calls
* **Matplotlib & Seaborn** → Visualization
* **Datetime** → Timestamp conversion

### **Applications**

* Helps track **short-term weather trends**.
* Useful for **weather analysis dashboards**.
* Can be extended to include:

  * Wind speed, pressure, etc.
  * Comparison between multiple cities.
  * Saving plots as images or interactive dashboards.



Do you want me to create a **concise project report** (like abstract, objectives, scope, limitations, conclusion) based on this code?
