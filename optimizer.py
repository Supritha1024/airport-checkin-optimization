import pandas as pd
import math

# Load data
df = pd.read_csv("synthetic_airport_data.csv")

# Convert Time properly
df["Time"] = pd.to_datetime(df["Time"])
df["Hour"] = df["Time"].dt.hour

# Group passengers per hour
hourly_data = df.groupby("Hour").agg({
    "Passengers": "sum",
    "Avg_Service_Time": "mean"
}).reset_index()

# Function to calculate required desks
def calculate_desks(passengers, service_time):
    capacity_per_desk = 60 / service_time
    desks = math.ceil(passengers / capacity_per_desk)
    return desks

# Apply function
hourly_data["Required_Desks"] = hourly_data.apply(
    lambda row: calculate_desks(row["Passengers"], row["Avg_Service_Time"]),
    axis=1
)

print("\nOptimization Results:")
print(hourly_data)
STATIC_DESKS = 5

comparison_results = []

for index, row in hourly_data.iterrows():
    passengers = row["Passengers"]
    service_time = row["Avg_Service_Time"]
    dynamic_desks = row["Required_Desks"]

    capacity_per_desk = 60 / service_time

    # Static capacity
    static_capacity = STATIC_DESKS * capacity_per_desk

    # Dynamic capacity
    dynamic_capacity = dynamic_desks * capacity_per_desk

    static_overload = max(0, passengers - static_capacity)
    dynamic_overload = max(0, passengers - dynamic_capacity)

    comparison_results.append([
        row["Hour"],
        passengers,
        static_overload,
        dynamic_overload
    ])

comparison_df = pd.DataFrame(comparison_results, columns=[
    "Hour",
    "Passengers",
    "Static_Overload",
    "Dynamic_Overload"
])

print("\nStatic vs Dynamic Comparison:")
print(comparison_df)