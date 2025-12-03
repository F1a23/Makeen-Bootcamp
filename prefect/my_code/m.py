import pymysql
from prefect import flow, task
import pandas as pd

# --------------------- SAMPLE DATA ---------------------
def create_sample_data():
    data = {
        "PassengerId": [1, 2, 3, 4, 5],
        "Survived": [0, 1, 1, 0, 1],
        "Pclass": [3, 1, 3, 1, 2],
        "Name": ["John Doe", "Jane Smith", "Alice Brown", "Bob White", "Charlie Black"],
        "Sex": ["male", "female", "female", "male", "male"],
        "Age": [22, 38, None, 35, None],
        "Fare": [7.25, 71.2833, 7.925, None, 15.5]
    }
    df = pd.DataFrame(data)
    df.to_csv("sample_titanic.csv", index=False)
    return "sample_titanic.csv"

# --------------------- TASKS ---------------------

@task
def extract(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows")
    return df

@task
def transform(df: pd.DataFrame) -> pd.DataFrame:
    df["Age"] = df["Age"].fillna(df["Age"].mean()).astype(int)
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean()).astype(float)
    df = pd.get_dummies(df, columns=["Sex"], drop_first=True)
    print("Data transformed")
    return df

@task
def load(df: pd.DataFrame, host, user, password, database, table_name: str):
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            PassengerId INT PRIMARY KEY,
            Survived INT,
            Pclass INT,
            Name VARCHAR(100),
            Age INT,
            Fare FLOAT,
            Sex_male TINYINT
        )
    """)

    # Insert data row by row
    for _, row in df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        columns = ", ".join(row.index)
        sql = f"REPLACE INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Loaded {len(df)} rows into {table_name}")

# --------------------- FLOW ---------------------

@flow
def etl_flow(
    host,
    user,
    password,
    database,
    table_name
):
    csv_file = create_sample_data()
    df = extract(csv_file)
    df_transformed = transform(df)
    load(df_transformed, host, user, password, database, table_name)


# --------------------- RUN ONCE ---------------------

if __name__ == "__main__":
    etl_flow(
        host="localhost",
        user="root",
        password="Oman99690050#",
        database="mydb33",
        table_name="passengers"
    )
