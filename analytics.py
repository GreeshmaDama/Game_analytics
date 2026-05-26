from database import get_engine
import pandas as pd

engine = get_engine()

def run_queries():
    df = pd.read_sql("SELECT * FROM game_events", engine)

    # Daily Active Users (DAU)
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date
    dau = df.groupby("date")["user_id"].nunique()

    # Revenue
    revenue = df["revenue"].sum()

    # Top countries
    top_countries = df["country"].value_counts().head(5)

    # Retention (simple version)
    first_login = df[df["event_type"] == "login"].groupby("user_id")["date"].min()
    retention = len(first_login) / df["user_id"].nunique()

    print("\n--- ANALYTICS ---")
    print("Total Revenue:", revenue)
    print("\nDAU Sample:\n", dau.head())
    print("\nTop Countries:\n", top_countries)
    print("\nRetention (approx):", retention)

if __name__ == "__main__":
    run_queries()