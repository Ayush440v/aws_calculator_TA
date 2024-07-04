import sqlite3

def create_connection():
    conn = sqlite3.connect("aws_costs.db")
    return conn
