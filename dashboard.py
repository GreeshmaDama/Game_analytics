import streamlit as st
import pandas as pd
from database import get_engine

engine = get_engine()
df = pd.read_sql("SELECT * FROM game_events", engine)

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date

st.title("🎮 Game Analytics Dashboard")

# DAU
dau = df.groupby("date")["user_id"].nunique()
st.line_chart(dau)

# Revenue
revenue = df.groupby("date")["revenue"].sum()
st.line_chart(revenue)

# Top countries
st.bar_chart(df["country"].value_counts().head(10))

st.write("Raw Data Sample")
st.dataframe(df.head())