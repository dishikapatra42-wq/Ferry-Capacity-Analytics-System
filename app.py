import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🚢 Ferry Capacity Utilization & Operational Efficiency Analytics System")

df = pd.read_csv("Final_Ferry_Analysis.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("KPI Summary")

st.metric("Total Sales", int(df["Sales Count"].sum()))
st.metric("Total Redemptions", int(df["Redemption Count"].sum()))
st.metric("Average Activity", round(df["Total Activity Load"].mean(),2))

st.subheader("Hourly Activity")

hourly = df.groupby("Hour")["Total Activity Load"].mean()

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(hourly.index, hourly.values, marker='o')
ax.set_xlabel("Hour")
ax.set_ylabel("Activity")
st.pyplot(fig)