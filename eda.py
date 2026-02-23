import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"synthetic_airport_data.csv")

# Basic info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# Convert Time column properly
df["Time"] = pd.to_datetime(df["Time"])

# Extract hour
df["Hour"] = df["Time"].dt.hour

# Group by hour
hourly_passengers = df.groupby("Hour")["Passengers"].sum()

print("\nPassengers per Hour:")
print(hourly_passengers)

# Plot passenger trend
plt.figure()
hourly_passengers.plot()
plt.title("Total Passengers Per Hour")
plt.xlabel("Hour")
plt.ylabel("Total Passengers")
plt.show()