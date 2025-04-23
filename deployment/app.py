import streamlit as st

import json
import pickle
import pandas as pd
import numpy as np

from missing_indicator import MissingIndicatorImputer

class MainApp:
    def __init__(self, model_file_path, features_values_path) -> None:
        self.model_path = model_file_path
        self.features_path = features_values_path


    def init(self):
        with open(self.model_path, "rb") as file_1:
            self.model = pickle.load(file_1)

        with open(self.features_path, "r") as file_2:
            self.features_values = json.load(file_2)

    def run(self):
        st.title("Rain Prediction App")

        locations = self.features_values["Location"]
        wind_dir = self.features_values["WindDir"]
        cloud_oktas = self.features_values["CloudOktas"]

        # Input fields
        location = st.selectbox("Weather Station", locations)
        min_temp = st.slider("Minimum Temperature (°C)", min_value=self.features_values["MinTemp"] - 2, max_value=self.features_values["MaxTemp"] + 2)
        max_temp = st.slider("Maximum Temperature (°C)", min_value=self.features_values["MinTemp"] - 2, max_value=self.features_values["MaxTemp"] + 2)
        temp_9am = st.slider("Temperature 9am (°C)", min_value=self.features_values["MinTemp"] - 2, max_value=self.features_values["MaxTemp"] + 2)
        temp_3pm = st.slider("Temperature 3pm (°C)", min_value=self.features_values["MinTemp"] - 2, max_value=self.features_values["MaxTemp"] + 2)
        humidity_9am = st.slider("Humidity 9am (%)", min_value=self.features_values["HumidityMin"], max_value=self.features_values["HumidityMax"])
        humidity_3pm = st.slider("Humidity 3pm (%)", min_value=self.features_values["HumidityMin"], max_value=self.features_values["HumidityMax"])
        pressure_9am = st.slider("Pressure 9am (hpa)", min_value=self.features_values["PressureMin"], max_value=self.features_values["PressureMax"])
        pressure_3pm = st.slider("Pressure 3pm (hpa)", min_value=self.features_values["PressureMin"], max_value=self.features_values["PressureMax"])

        rainfall = st.slider("Rainfall (mm)", min_value=self.features_values["RainfallMin"], max_value=self.features_values["RainfallMax"])
        evaporation = st.slider("Evaporation (mm)", min_value=self.features_values["EvaporationMin"], max_value=self.features_values["EvaporationMax"])
        sunshine = st.slider("Sunshine (hours)", min_value=self.features_values["SunshineMin"], max_value=self.features_values["SunshineMax"])
        wind_gust_dir = st.selectbox("Wind Gust Direction", wind_dir)
        wind_gust_speed = st.slider("Wind Gust Speed (km/h)", min_value=self.features_values["WindGustSpeedMin"], max_value=self.features_values["WindGustSpeedMax"])

        wind_9am_dir = st.selectbox("Wind 9am Direction", wind_dir)
        wind_9am_speed = st.slider("Wind 9am Speed (km/h)", min_value=self.features_values["WindSpeedMin"], max_value=self.features_values["WindSpeedMax"])

        wind_3pm_dir = st.selectbox("Wind 3pm Direction", wind_dir)
        wind_3pm_speed = st.slider("Wind 3pm Speed (km/h)", min_value=self.features_values["WindSpeedMin"], max_value=self.features_values["WindSpeedMax"])

        cloud_cover_9am = st.slider("Cloud Cover 9am (oktas)", min_value=min(cloud_oktas), max_value=max(cloud_oktas), step=1)
        cloud_cover_3pm = st.slider("Cloud Cover 3pm (oktas)", min_value=min(cloud_oktas), max_value=max(cloud_oktas), step=1)

        input = {
            "Location": [location],
            "MinTemp": min_temp,
            "MaxTemp": max_temp,
            "Rainfall": rainfall,
            "Evaporation": evaporation,
            "Sunshine": sunshine,
            "WindGustDir": wind_gust_dir,
            "WindGustSpeed": wind_gust_speed,
            "WindDir9am": wind_9am_dir,
            "WindDir3pm": wind_3pm_dir,
            "WindSpeed9am": wind_9am_speed,
            "WindSpeed3pm": wind_3pm_speed,
            "Humidity9am": humidity_9am,
            "Humidity3pm": humidity_3pm,
            "Pressure9am": pressure_9am,
            "Pressure3pm": pressure_3pm,
            "Cloud9am": cloud_cover_9am,
            "Cloud3pm": cloud_cover_3pm,
            "Temp9am": temp_9am,
            "Temp3pm": temp_3pm,
            "RainToday": "Yes" if rainfall >= 1.0 else "No"
        }


        if st.button("Predict"):
            prediction = self.model.predict(pd.DataFrame(input))
            st.success("Yes, likely chance there will be rain tomorrow" if prediction[0] == "Yes" else "No, no rain tomorrow")

if __name__ == "__main__":
    app = MainApp("model.pkl", "features_values.json")
    app.init()

    app.run()

