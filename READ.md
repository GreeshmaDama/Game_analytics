# 🎮 Game Analytics Pipeline (End-to-End Data Engineering Project)

## 📌 Overview

This project simulates a real-world mobile game analytics system where user activity data is generated, processed, stored, analyzed, and visualized.

It mimics how gaming companies track player behavior, engagement, retention, and revenue at scale.

The goal is to demonstrate end-to-end Data Engineering skills including:
- Data generation
- ETL pipelines
- SQL data modeling
- Analytics
- Dashboarding

---

## 🧠 Problem Statement

Modern mobile games generate millions of events daily (logins, battles, purchases, etc.). To understand player behavior, companies need a system that:

- Collects raw game events
- Cleans and processes data
- Stores it efficiently
- Generates business insights
- Visualizes key metrics

This project builds a simplified version of that system.

---

## 🏗️ Architecture

Data Generator → CSV (Raw Data)
        ↓
ETL Pipeline (Cleaning & Transformation)
        ↓
Database (SQLite)
        ↓
Analytics Layer (SQL + Python)
        ↓
Dashboard (Streamlit)

---

## 📁 Project Structure

game-analytics-pipeline/
│
├── data_generator.py     # Simulates game event data
├── etl_pipeline.py       # Cleans and loads data into DB
├── database.py           # Database connection setup
├── schema.sql            # Database schema design
├── analytics.py          # Business metrics & insights
├── dashboard.py          # Interactive Streamlit dashboard
├── game_events.csv       # Generated dataset
├── game.db               # SQLite database
├── requirements.txt      # Dependencies
└── README.md

---

## ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- SQLite / SQLAlchemy
- Streamlit
- Faker

---

## 🎮 Data Description

Each row represents a game event:

| Column | Description |
|--------|------------|
| user_id | Unique player ID |
| event_type | Action (login, battle, purchase, etc.) |
| timestamp | Event time |
| country | Player location |
| session_duration | Time spent in game |
| revenue | Money spent |

---

## 🔄 Pipeline Steps

### 1️⃣ Data Generation
- Simulates 50,000+ game events
- Creates realistic player behavior
- Includes revenue distribution (only ~10% paying users)

Output:
game_events.csv

---

### 2️⃣ ETL Pipeline
- Removes duplicates
- Handles missing values
- Converts timestamps
- Loads data into SQLite database

---

### 3️⃣ Database Layer
- Stores structured game events
- Enables SQL queries for analytics

Table:
game_events

---

### 4️⃣ Analytics Layer
Computes key metrics:

- Daily Active Users (DAU)
- Total Revenue
- Country distribution
- Retention rate (simplified)

---

### 5️⃣ Dashboard
Interactive Streamlit dashboard showing:

- DAU trends
- Revenue trends
- Country distribution
- Raw data preview

---

## 📊 Key Metrics

- DAU (Daily Active Users)
- Revenue
- Retention Rate
- Engagement trends
- Geographic distribution

---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

---

### 2. Generate data
python data_generator.py

---

### 3. Run ETL pipeline
python etl_pipeline.py

---

### 4. Run analytics
python analytics.py

---

### 5. Launch dashboard
streamlit run dashboard.py

---
## 📊 Output

When you run the project:

```bash
python analytics.py

--- ANALYTICS ---
Total Revenue: 50699.8

DAU Sample:
date
2026-04-22  590
2026-04-23  800
2026-04-24  824
2026-04-25  792
2026-04-26  819

Top Countries:
Korea        446
Congo        415
Netherlands  241
Niger        238
Saint Lucia  237

Retention (approx): 1.0
---

# 🖼️ 2. DASHBOARD screenshot

First:
- 
## 🎯 Skills Demonstrated

- Data Engineering (ETL pipelines)
- SQL & Data Modeling
- Python data processing
- Analytics & KPI design
- Data visualization
- End-to-end system thinking

---

## 💡 Why This Project Matters

This project replicates real-world gaming analytics systems used to:
- Understand player behavior
- Improve retention
- Optimize monetization
- Drive product decisions

---

## 🔥 Future Improvements

- Add real-time streaming (Kafka simulation)
- Use cloud warehouse (BigQuery / Snowflake)
- Add Airflow orchestration
- Use Spark for large-scale processing
- Deploy dashboard online

---

## 👨‍💻 Author

Data Engineering portfolio project focused on gaming analytics systems.
