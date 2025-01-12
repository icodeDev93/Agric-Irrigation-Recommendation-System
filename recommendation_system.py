# Irrigation Recommendation System with Data Analysis and Streamlit

# Importing necessary libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

# Load the CSV file containing soil moisture, weather, and irrigation data
df = pd.read_excel('C:/Users/Eben/PycharmProjects/Agric_Recommendation_Systm/soil_moisture_weather_data_with_irrigation.xlsx')

data = df.drop(['Date'],axis=1)
# Title for the Streamlit app
st.title('Irrigation Recommendation System')

# Exploratory Data Analysis (EDA)
st.header('Exploratory Data Analysis (EDA)')

# Display dataset summary
st.write('### Dataset Summary')
st.write(data.describe())

# Visualize the distribution of Soil Moisture Percentage
st.write('### Distribution of Soil Moisture Percentage')
fig, ax = plt.subplots()
sns.histplot(data['Soil_Moisture_Percentage'], bins=20, ax=ax)
st.pyplot(fig)

# Visualize the distribution of Temperature
st.write('### Distribution of Temperature')
fig, ax = plt.subplots()
sns.histplot(data['Temperature_Celsius'], bins=20, ax=ax)
st.pyplot(fig)

# Visualize the relationship between Soil Moisture and Crop Type
st.write('### Soil Moisture vs Crop Type')
fig, ax = plt.subplots()
sns.boxplot(x='Crop_Type', y='Soil_Moisture_Percentage', data=data, ax=ax)
st.pyplot(fig)

# Visualize the relationship between Rainfall and Weather Condition
st.write('### Rainfall vs Weather Condition')
fig, ax = plt.subplots()
sns.boxplot(x='Weather_Condition', y='Rainfall_mm', data=data, ax=ax)
st.pyplot(fig)

# End of EDA, proceed to user input for irrigation recommendation
st.write('---')

# User inputs for irrigation recommendation
st.write('### Enter the following details:')

# Input fields for the user
crop_type = st.selectbox('Crop Type', ['Wheat', 'Corn', 'Soybean'])
soil_moisture = st.number_input('Soil Moisture Percentage', min_value=0, max_value=100)
temperature = st.number_input('Temperature (Celsius)', min_value=-30, max_value=50)
rainfall = st.number_input('Rainfall (mm)', min_value=0, max_value=500)
weather_condition = st.selectbox('Weather Condition', ['Sunny', 'Cloudy', 'Rainy', 'Dry'])


# Function to recommend irrigation based on soil moisture, crop type, and weather

def recommend_irrigation(soil_moisture, weather, crop):
    # Different crops have different soil moisture thresholds for irrigation
    if crop == 'Wheat':
        if soil_moisture < 40 and weather in ['Sunny', 'Dry']:
            return 'Irrigation recommended'
        else:
            return 'No irrigation needed'
    elif crop == 'Corn':
        if soil_moisture < 50 and weather in ['Sunny', 'Dry']:
            return 'Irrigation recommended'
        else:
            return 'No irrigation needed'
    elif crop == 'Soybean':
        if soil_moisture < 45 and weather in ['Sunny', 'Dry']:
            return 'Irrigation recommended'
        else:
            return 'No irrigation needed'
    return 'No irrigation needed'


# Button to get the irrigation recommendation
if st.button('Get Irrigation Recommendation'):
    # Get the irrigation recommendation based on inputs
    recommendation = recommend_irrigation(soil_moisture, weather_condition, crop_type)

    # Display the recommendation
    st.write(f'Recommendation for {crop_type}: {recommendation}')

