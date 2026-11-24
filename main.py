"""Weather Forecast & Alert Application - beginner CLI."""
from src.weather_service import get_weather_for_city
from src.alerts import generate_alerts
from src.report import save_report

def main():
    print("\n=== Weather Forecast & Alert Application ===")
    city = input("Enter city name (example: Bengaluru): ").strip()
    if not city:
        print("Please enter a city name.")
        return

    try:
        weather = get_weather_for_city(city)
        alerts = generate_alerts(weather)
        print(f"\nLocation: {weather['location']['name']}, {weather['location']['country']}")
        print(f"Temperature: {weather['current']['temperature_c']} °C")
        print(f"Humidity: {weather['current']['humidity']} %")
        print(f"Wind: {weather['current']['wind_kmh']} km/h")
        print(f"Condition: {weather['current']['condition']}")

        print("\n--- Alerts ---")
        if alerts:
            for alert in alerts:
                print(f"[{alert['severity'].upper()}] {alert['message']}")
        else:
            print("No important weather alerts right now.")

        print("\n--- 7-Day Forecast ---")
        for day in weather["daily"]:
            print(f"{day['date']}: {day['condition']}, {day['min_c']}°C to {day['max_c']}°C, rain probability {day['rain_probability']}%")

        path = save_report(weather, alerts)
        print(f"\nReport saved to: {path}")
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Check your city name and internet connection, then try again.")

if __name__ == "__main__":
    main()
