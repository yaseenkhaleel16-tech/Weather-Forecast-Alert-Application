# Weather Forecast & Alert Application

A beginner-friendly Python project that fetches live weather and a 7-day forecast using the public Open-Meteo API, checks simple alert rules, displays results, and saves a CSV report.

## Features
- City search and geocoding
- Current temperature, humidity, wind and condition
- 7-day forecast
- Rain, heat, humidity, wind and thunderstorm alerts
- CSV report generation
- Streamlit dashboard
- No API key required for the included version

## Project flow
User enters city → geocoding → weather API → JSON parsing → alert rules → display → CSV report.

## Folder structure
```
Weather-Forecast-Alert-Application/
├── data/
├── docs/
├── images/
├── outputs/
├── reports/
├── src/
│   ├── __init__.py
│   ├── alerts.py
│   ├── report.py
│   └── weather_service.py
├── .env.example
├── .gitignore
├── app.py
├── main.py
└── requirements.txt
```

## Windows setup
1. Install Python 3.11+ from python.org and tick **Add Python to PATH** during installation.
2. Open this project folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Create a virtual environment:
   `python -m venv .venv`
5. Activate it:
   `.venv\Scripts\activate`
6. Install libraries:
   `python -m pip install -r requirements.txt`

## Run the beginner terminal version
`python main.py`

Enter a city such as `Bengaluru`.

## Run the dashboard
`python -m streamlit run app.py`

A browser window will open. Enter a city and click **Get Weather**.

## Outputs
The terminal program creates a CSV file in `outputs/`.

## GitHub safety
Never upload `.env` or real private API keys. The `.gitignore` already ignores `.env`.

## Interview explanation
“I built a Python weather application that retrieves live weather from a public API, parses JSON data, applies rule-based thresholds for rain, heat, humidity, wind and thunderstorms, and presents the forecast through a CLI and Streamlit dashboard. It also saves forecast data as a CSV report.”

## Future improvements
FastAPI endpoints, scheduled refresh, email/Telegram notifications, AQI, maps, multi-city tracking, database storage, and automated tests.
