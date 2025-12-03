
import pandas as pd
import pymysql
import requests
from prefect import flow, task

# --------------------- DATABASE CREDENTIALS ---------------------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Oman99690050#"
DB_NAME = "weather_db2"
TABLE_NAME = "hourly_weather"

# --------------------- API KEY ---------------------
API_KEY = "e2ff8e020abb574b3f2eb97c686b2ba6"

# --------------------- TASKS ---------------------
@task
def extract_task():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Muscat&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame([{
        "timestamp": pd.Timestamp.now(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_condition": data["weather"][0]["main"]
    }])
    print(f"Extracted {len(df)} row(s)")
    return df

@task
def transform_task(df: pd.DataFrame):
    df['temperature'] = df['temperature'] - 273.15  # Kelvin → Celsius
    df['humidity'] = df['humidity'].fillna(0)
    df['FeelsLike'] = df['temperature'] - df['humidity']*0.1
    print("Transformed data")
    return df

@task
def load_task(df: pd.DataFrame):
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            timestamp DATETIME PRIMARY KEY,
            temperature FLOAT,
            humidity INT,
            weather_condition VARCHAR(50),
            FeelsLike FLOAT
        )
    """)
    for _, row in df.iterrows():
        placeholders = ', '.join(['%s'] * len(row))
        columns = ', '.join(row.index)
        sql = f"REPLACE INTO {TABLE_NAME} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(df)} row(s)")

# --------------------- FLOW ---------------------
@flow
def weather_etl_flow():
    df = extract_task()
    df_transformed = transform_task(df)
    load_task(df_transformed)

# --------------------- SCHEDULING ---------------------
if __name__ == "__main__":
    # Serve flow hourly at minute 0
    weather_etl_flow.serve(
        name="hourly-weather-etl",
        cron="0 * * * *",  # Every hour
    )
    