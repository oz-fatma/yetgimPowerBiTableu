import pandas as pd
import numpy as np
# 1.Soru

df = pd.read_csv("weather_data.csv")
print("dosya okundu")
# 2.Soru
print(df.head(5))
print(df.tail(5))

print(df.describe)

# 3.Soru
print(df['Date'])
print(df['City'])
print(df['Temperature'])

print(df[['Date','City','Temperature']])

# 4.Soru
print(df[df['Temperature'] > 30 ])

print(df[df['City'] == "Bursa" ])
# 5.Soru
print(df[(df['City']== "İstanbul") & (df['Humidity']>60)])

print(df[(df['City']== "Ankara") | (df['Temperature'] < 5)])

print(df[(df['Temperature'] < 10 ) | (df['Humidity'] > 70 )])

# 6.Soru
print(df.sort_values('Temperature',ascending=False).head(10))

print(df.sort_values('Humidity',ascending= False))

print(df.sort_values('City',ascending= True))

# 7.Soru
df['Temperature_F'] = (df['Temperature'] * 9/5) + 32

print(df[['Temperature', 'Temperature_F']])

df['FeelsLike'] = df['Temperature'] - (df['Humidity'] / 100)

print(df[ 'FeelsLike'])

# 8.Soru

print(df['City'].value_counts())

print(df.groupby('City')['Temperature'].mean())

# 9.Soru
df.loc[df['Temperature'].idxmax()]
print(df.loc[df['Temperature'].idxmax()])


df.loc[df['Temperature'].idxmin()]
print(df.loc[df['Humidity'].idxmin()])

# 10.Soru
sehir_sicakliklari  = df.groupby('City')['Temperature'].mean()

sehir_sicakliklari.to_csv('sehir_sicakliklari.csv')