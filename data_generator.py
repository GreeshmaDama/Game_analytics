import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

EVENT_TYPES = ["login", "logout", "battle", "purchase", "level_up"]

def generate_data(n=10000):
    data = []

    start_date = datetime.now() - timedelta(days=30)

    for _ in range(n):
        event = {
            "user_id": random.randint(1, 1000),
            "event_type": random.choice(EVENT_TYPES),
            "timestamp": start_date + timedelta(minutes=random.randint(0, 60*24*30)),
            "country": fake.country(),
            "session_duration": random.randint(1, 300),
            "revenue": round(random.uniform(0, 20), 2) if random.random() < 0.1 else 0
        }
        data.append(event)

    df = pd.DataFrame(data)
    df.to_csv("game_events.csv", index=False)
    print("Data generated: game_events.csv")

if __name__ == "__main__":
    generate_data(50000)