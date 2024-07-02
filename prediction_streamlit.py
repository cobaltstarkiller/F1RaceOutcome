import streamlit as st
import pandas as pd
import numpy as np

# Load the CSV file
file_path = 'new_pred.csv'
df = pd.read_csv(file_path)

# Create selections for race and driver
races = df['races_name'].unique()
drivers = df['drivers_code'].unique()
year=df['date'].unique()

st.title("Race Prediction Display")

selected_race = st.selectbox("Select Race", races)
selected_driver = st.selectbox("Select Driver", drivers)
selected_year = st.selectbox("Select Year", year)

# Filter the dataframe based on selections
filtered_df = df[(df['races_name'] == selected_race) & (df['drivers_code'] == selected_driver) & (df['date'] == selected_year)]

if not filtered_df.empty:
    prediction_label = filtered_df['prediction_label'].values[0]
    actual_result = filtered_df['results_positionOrder'].values[0]

    st.write(f"Prediction Label: {prediction_label}")
    st.write(f"Actual Result: {actual_result}")
else:
    st.write("No data available for the selected race and driver.")
