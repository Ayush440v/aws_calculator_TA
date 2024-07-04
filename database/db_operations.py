from .db_connection import create_connection

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS costs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            features TEXT,
            total_users INTEGER,
            monthly_active_users INTEGER,
            concurrent_users INTEGER,
            total_cost REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_costs(features, total_users, monthly_active_users, concurrent_users, total_cost):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO costs (features, total_users, monthly_active_users, concurrent_users, total_cost)
        VALUES (?, ?, ?, ?, ?)
    """, (",".join(features), total_users, monthly_active_users, concurrent_users, total_cost))
    conn.commit()
    conn.close()
