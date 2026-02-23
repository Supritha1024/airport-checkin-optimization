import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# -----------------------------
# Step 1: Generate Synthetic Data
# -----------------------------

# Create time slots (8 AM to 8 PM)
hours = [f"{h}:00" for h in range(8, 21)]

# Simulate passenger arrivals (morning & evening peak)
passengers = [120, 150, 200, 180, 160, 140, 130, 170, 220, 210, 190, 160, 140]

# Average service time per passenger (minutes)
service_time = 3

# Create DataFrame
data = pd.DataFrame({
    "Time": hours,
    "Passengers_Arrived": passengers
})

# -----------------------------
# Step 2: Calculate Required Desks
# -----------------------------

def calculate_desks(passengers, service_time):
    required_desks = []
    for p in passengers:
        desks = math.ceil((p * service_time) / 60)
        required_desks.append(desks)
    return required_desks

data["Required_Desks"] = calculate_desks(data["Passengers_Arrived"], service_time)

# -----------------------------
# Step 3: Display Results
# -----------------------------

print("\nAirport Check-in Desk Optimization Results:\n")
print(data)

# -----------------------------
# Step 4: Visualization
# -----------------------------

plt.figure()
plt.plot(data["Time"], data["Passengers_Arrived"])
plt.title("Passenger Arrivals per Hour")
plt.xlabel("Time")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.plot(data["Time"], data["Required_Desks"])
plt.title("Required Check-in Desks per Hour")
plt.xlabel("Time")
plt.ylabel("Number of Desks")
plt.xticks(rotation=45)
plt.show()