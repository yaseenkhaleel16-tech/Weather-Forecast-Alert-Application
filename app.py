import streamlit as st
import pandas as pd
from src.weather_service import get_weather_for_city
from src.alerts import generate_alerts

st.set_page_config(page_title="Weather Forecast & Alerts", page_icon="🌦️", layout="wide")
st.title("🌦️ Weather Forecast & Alert Application")
st.write("Enter a city to fetch a 7-day forecast and rule-based alerts.")

city = st.text_input("City", "Bengaluru")
if st.button("Get Weather", type="primary"):
    try:
        w = get_weather_for_city(city)
        alerts = generate_alerts(w)
        c = w["current"]

        st.success(f"Weather for {w['location']['name']}, {w['location']['country']}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Temperature", f"{c['temperature_c']} °C")
        col2.metric("Humidity", f"{c['humidity']} %")
        col3.metric("Wind", f"{c['wind_kmh']} km/h")
        col4.metric("Condition", c["condition"])

        st.subheader("Alerts")
        if alerts:
            for a in alerts:
                if a["severity"] == "critical":
                    st.error(a["message"])
                elif a["severity"] == "warning":
                    st.warning(a["message"])
                else:
                    st.info(a["message"])
        else:
            st.success("No important weather alerts right now.")

        df = pd.DataFrame(w["daily"])
        st.subheader("7-Day Forecast")
        st.dataframe(df, use_container_width=True)
        st.subheader("Temperature trend")
        chart = df.set_index("date")[["min_c", "max_c"]]
        st.line_chart(chart)
    except Exception as e:
        st.error(str(e))
