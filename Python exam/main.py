import pandas as pd
import numpy as np

df = pd.read_csv('AQI_Data.csv')

# first 5 rows of the dataset
print("\nFirst five rows of the dataset")
print(df.head())



# last 6 rows of the dataset
print("\nLast six rows of the dataset")
print(df.tail(6))



# Summary statistics for all numeric columns
print("\nSummary statistics for all numeric columns")
print(df.describe())



# Numpy to calculate the mean AQI, PM2.5 and PM10 values for each city
print("\nMean AQI, PM2.5 and PM10 values for each city")
# Convert to NumPy arrays
cities = np.array(df['City'])
aqi = np.array(df['AQI'])
pm25 = np.array(df['PM2.5'])
pm10 = np.array(df['PM10'])
# Unique cities
unique_cities = np.unique(cities)
# Calculate mean values for each city
print("\nMean AQI, PM2.5, and PM10 values for each city")
for city in unique_cities:
    city_mask = cities == city  # Mask for the current city
    mean_aqi = np.mean(aqi[city_mask])
    mean_pm25 = np.mean(pm25[city_mask])
    mean_pm10 = np.mean(pm10[city_mask])
    print(f"{city}: AQI={mean_aqi:.2f}, PM2.5={mean_pm25:.2f}, PM10={mean_pm10:.2f}")
    
    

# Check for missing values in the dataset
print("\nMissing values in the dataset")
print(df.isnull())
print(df.isnull().sum())



# Replace missing values in numeric columns with the column mean
df['AQI'] = df['AQI'].fillna(df['AQI'].mean())
df['PM2.5'] = df['PM2.5'].fillna(df['PM2.5'].mean())
df['PM10'] = df['PM10'].fillna(df['PM10'].mean())
print(df)



# Extract the AQI column and convert it to a numpy array
aqi = df['AQI']
aqi_array = aqi.to_numpy()



# Mean, median and standard deviation of the AQI values
print("Mean, median and standard deviation of the AQI values")
print(np.mean(aqi_array))
print(np.median(aqi_array))
print(np.std(aqi_array))

