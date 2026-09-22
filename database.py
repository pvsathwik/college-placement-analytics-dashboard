import sqlite3
import pandas as pd

DB_NAME = "placement.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_csv("data/placement_data.csv")

    df.to_sql(
        "placements",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("✅ Placement database created successfully!")


def get_data():
    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM placements",
        conn
    )

    conn.close()

    return df


def get_student(student_id):
    conn = sqlite3.connect(DB_NAME)

    query = """
        SELECT *
        FROM placements
        WHERE Student_ID = ?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(student_id,)
    )

    conn.close()

    return df


if __name__ == "__main__":
    create_database()

    result = get_student("STU001")

    print("\nStudent Search Result:")
    print(result)