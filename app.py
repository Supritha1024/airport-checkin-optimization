import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("synthetic_airport_data.csv")
df.columns = df.columns.str.strip()
st.write("Actual columns:",df.columns)

st.title("Airport Check-in Desk Optimization Dashboard")

# User Inputs
static_counters = st.slider("Number of Static Counters", 1, 10, 3)
capacity_per_counter = st.slider("Capacity per Counter per Hour", 10, 50, 20)

# Static Model
df['Static_Capacity'] = static_counters * capacity_per_counter
df['Static_Overload'] = df['Passengers'] - df['Static_Capacity']
df['Static_Overload'] = df['Static_Overload'].apply(lambda x: max(x, 0))

# Dynamic Model
df['Dynamic_Counters'] = (df['Passengers'] / capacity_per_counter).apply(lambda x: int(x) + 1)
df['Dynamic_Capacity'] = df['Dynamic_Counters'] * capacity_per_counter
df['Dynamic_Overload'] = df['Passengers'] - df['Dynamic_Capacity']
df['Dynamic_Overload'] = df['Dynamic_Overload'].apply(lambda x: max(x, 0))

# Metrics
st.subheader("Performance Metrics")
st.write("Total Static Overload:", df['Static_Overload'].sum())
st.write("Total Dynamic Overload:", df['Dynamic_Overload'].sum())

# Plot
st.subheader("Overload Comparison")

fig, ax = plt.subplots()
ax.plot(df['Hour'], df['Static_Overload'], label="Static")
ax.plot(df['Hour'], df['Dynamic_Overload'], label="Dynamic")
ax.set_xlabel("Hour")
ax.set_ylabel("Overload")
ax.legend()

st.pyplot(fig)