import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys

# --- CONFIGURATION ---
# API_KEY = "05f371fbb4e1278251cf280860e4a8d"
API_KEY =  "https://api.openweathermap.org/data/2.5/forecast?q=Nagpur&appid=05f371fbb4e1278251cf280860e4a8d9&units=metric"
UNITS = "metric"  # or "imperial"
DAYS = 5  # This API gives data in 3-hour intervals (so ~8 entries/day)

# --- FETCH WEATHER DATA ---
def fetch_weather_data(city, api_key, units):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q=Nagpur&appid=05f371fbb4e1278251cf280860e4a8d9"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data:", response.json().get("message", "Unknown error"))
        sys.exit(1)
    return response.json()

# --- PARSE DATA ---
def parse_weather_data(raw_data):
    dates, temps, humidities, descriptions = [], [], [], []

    for item in raw_data['list']:
        dt = datetime.fromtimestamp(item['dt'])
        dates.append(dt)
        temps.append(item['main']['temp'])
        humidities.append(item['main']['humidity'])
        descriptions.append(item['weather'][0]['description'])

    return dates, temps, humidities, descriptions

# --- VISUALIZATION ---
def create_dashboard(city, dates, temps, humidities, descriptions):
    sns.set(style="darkgrid")

    plt.figure(figsize=(12, 6))
    plt.plot(dates, temps, label="Temperature (°C)", color="tomato")
    plt.xticks(rotation=45)
    plt.title(f"Temperature Trend - {city}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(dates, humidities, label="Humidity (%)", color="skyblue")
    plt.xticks(rotation=45)
    plt.title(f"Humidity Trend - {city}")
    plt.xlabel("Date and Time")
    plt.ylabel("Humidity (%)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.countplot(x=descriptions, order=sorted(set(descriptions)))
    plt.xticks(rotation=45)
    plt.title(f"Weather Condition Frequency - {city}")
    plt.xlabel("Description")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# --- MAIN ---
def main():
    city = input("Enter the city name: ").strip()
    raw_data = fetch_weather_data(city, API_KEY, UNITS)
    dates, temps, humidities, descriptions = parse_weather_data(raw_data)
    create_dashboard(city, dates, temps, humidities, descriptions)

if __name__ == "__main__":
    main()