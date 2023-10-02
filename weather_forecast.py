## AI model for predicting Montreal's daily temperatures and precipitation
## using air pressure, humidity, dew point, and wind speed
## may be inaccurate depending on time of day as the training independent data
## were daily averages 

import pandas as pd
from sklearn import linear_model

data = pd.read_csv(r'C:\Users\David\Documents\SmallDATA\weatherstats_montreal_daily.csv', encoding='utf8')

X = data[['avg_hourly_relative_humidity', 'avg_hourly_dew_point', 'avg_hourly_wind_speed', 'avg_hourly_pressure_station']]

y_temp = data['avg_temperature']
y_rain = data['rain']
y_snow = data['snow']
y_high = data['max_temperature']
y_low = data['min_temperature']

temp_regression = linear_model.LinearRegression()
temp_regression.fit(X.values,y_temp)

rain_regression = linear_model.LinearRegression()
rain_regression.fit(X.values, y_rain)

snow_regression = linear_model.LinearRegression()
snow_regression.fit(X.values, y_snow)

high_regression = linear_model.LinearRegression()
high_regression.fit(X.values, y_high)

low_regression = linear_model.LinearRegression()
low_regression.fit(X.values, y_low)
todays_temp = temp_regression.predict([[88.0,10.3,5.0,102.80]])
todays_rain = rain_regression.predict([[88.0,10.3,5.0,102.80]])
todays_snow = snow_regression.predict([[88.0,10.3,5.0,102.80]])
todays_high = high_regression.predict([[88.0,10.3,5.0,102.80]])
todays_low = low_regression.predict([[88.0,10.3,5.0,102.80]])

if todays_rain < 0:
    todays_rain = 0
if todays_snow < 0:
    todays_snow = 0
    
print(todays_low, todays_high, todays_temp)    

todays_temp = int(todays_temp.round(0))
todays_high = int(todays_high.round(0))
todays_low = int(todays_low.round(0))

def print_forecast():
    print("there is " + str(todays_rain) + "mm of rain predicted and " + str(todays_snow) + "mm of snow predicted today.")
    print("Today's average temperature is " + str(todays_temp) + " degrees Celsius, with a daily high of " + str(todays_high) + " degrees Celsius and low of " + str(todays_low) + " degrees Celsius.")

print_forecast()
