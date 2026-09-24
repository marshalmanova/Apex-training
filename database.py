import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "2121",
    "database": "bank_db",
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
