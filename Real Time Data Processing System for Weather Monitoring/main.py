import time
import requests
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from datetime import datetime

# API configuration
API_KEY = "b4288257c72a5ac468fa46a7390a2bd7"  
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data from the OpenWeatherMap API
def fetch_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

# Function to process the fetched weather data
def process_weather_data(weather_data):
    temp_k = weather_data["main"]["temp"]
    temp_c = temp_k - 273.15  # Convert Kelvin to Celsius
    condition = weather_data["weather"][0]["main"]
    timestamp = pd.to_datetime(weather_data["dt"], unit='s')

    processed_data = {
        "temperature": temp_c,
        "condition": condition,
        "timestamp": timestamp
    }

    return processed_data

# Function to check alerts based on processed data
def check_alerts(processed_data):
    temperature_threshold = 35  # Set threshold for alerts
    if processed_data["temperature"] > temperature_threshold:
        return True
    return False

# Function to visualize daily weather summary
def plot_weather_summary(weather_summary):
    df = pd.DataFrame(weather_summary)
    df['date'] = df['timestamp'].dt.date

    # Group by date for daily aggregates
    daily_summary = df.groupby('date').agg(
        avg_temp=('temperature', 'mean'),
        max_temp=('temperature', 'max'),
        min_temp=('temperature', 'min'),
        dominant_condition=('condition', lambda x: x.mode()[0])  # Most frequent condition
    ).reset_index()

    # Create a line chart for average temperatures
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(x=daily_summary['date'], y=daily_summary['avg_temp'],
                                   mode='lines+markers', name='Avg Temperature (°C)', line=dict(color='royalblue')))
    fig_temp.add_trace(go.Scatter(x=daily_summary['date'], y=daily_summary['max_temp'],
                                   mode='lines+markers', name='Max Temperature (°C)', line=dict(color='red')))
    fig_temp.add_trace(go.Scatter(x=daily_summary['date'], y=daily_summary['min_temp'],
                                   mode='lines+markers', name='Min Temperature (°C)', line=dict(color='green')))
    
    fig_temp.update_layout(title='Daily Temperature Trends',
                           xaxis_title='Date',
                           yaxis_title='Temperature (°C)',
                           legend_title='Legend',
                           template='plotly_dark')

    # Bar chart for dominant weather conditions
    condition_counts = df['condition'].value_counts()
    fig_cond = go.Figure()
    fig_cond.add_trace(go.Bar(x=condition_counts.index, y=condition_counts.values, name='Conditions',
                               marker=dict(color='lightcoral')))
    fig_cond.update_layout(title='Weather Conditions Distribution',
                           xaxis_title='Condition',
                           yaxis_title='Count',
                           template='plotly_dark')

    return fig_temp, fig_cond

def main():
    st.set_page_config(page_title="Weather Monitoring Dashboard", layout="wide")
    st.title("🌦️ Real-Time Weather Monitoring System")
    st.sidebar.header("Settings")
    
    # Choose cities to monitor
    selected_cities = st.sidebar.multiselect("Select cities to monitor", CITIES, default=CITIES)

    weather_summary = []  # To store daily weather summaries

    # Display a button to start fetching weather data
    if st.sidebar.button("Start Monitoring"):
        with st.spinner("Fetching weather data..."):
            while True:
                for city in selected_cities:
                    weather_data = fetch_weather(city)
                    if weather_data.get("cod") != 200:
                        st.error(f"Failed to retrieve data for {city}: {weather_data.get('message')}")
                        continue
                    
                    processed_data = process_weather_data(weather_data)
                    st.success(f"Weather data for {city} retrieved successfully!")
                    st.write(f"**Current Weather in {city}:**")
                    st.json(processed_data)  # Display processed data in JSON format
                    weather_summary.append(processed_data)  # Append processed data for summary
                    
                    # Check for alerts
                    if check_alerts(processed_data):
                        st.warning(f"⚠️ Alert! High temperature detected in {city}: {processed_data['temperature']:.2f}°C")
                
                # Plot weather summary
                if weather_summary:
                    temp_fig, cond_fig = plot_weather_summary(weather_summary)
                    st.plotly_chart(temp_fig, use_container_width=True)  # Display temperature trend
                    st.plotly_chart(cond_fig, use_container_width=True)  # Display weather conditions distribution

                time.sleep(300)  # Fetch data every 5 minutes

if __name__ == "__main__":
    main()
