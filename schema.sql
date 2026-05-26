CREATE TABLE IF NOT EXISTS game_events (
    user_id INT,
    event_type TEXT,
    timestamp TIMESTAMP,
    country TEXT,
    session_duration INT,
    revenue FLOAT
);