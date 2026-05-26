import pandas as pd
from database import get_engine

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def load_data():
    engine = get_engine()

    df = pd.read_csv("game_events.csv")
    df = clean_data(df)

    df.to_sql("game_events", engine, if_exists="replace", index=False)

    print("ETL Completed: Data loaded into database")

if __name__ == "__main__":
    load_data()