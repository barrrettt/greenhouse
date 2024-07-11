import sqlite3
from datetime import datetime

def main():
    conn,cursor = connect()
    # datos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        ip_local TEXT,
        internet INTEGER,
        humidity REAL,
        luminosity REAL,
        pasive_ir INTEGER,
        humidity_ground REAL,
        temperature_air REAL,
        humidity_air REAL
    )
    ''')
    conn.commit()
    conn.close()

def connect():
    conn = sqlite3.connect('sensor_data.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn,cursor


def insert_sensor_data(data):
    conn, cursor = connect()
    timestamp = datetime.now().isoformat()
    ip_local = data.get('ip_local',None)
    internet = data.get('internet',None)
    humidity = data.get('humidity', None)
    luminosity = data.get('luminosity', None)
    pasive_ir = data.get('pasive_ir', None)
    humidity_ground = data.get('humidity_ground', None)
    temperature_air = data.get('temperature_air', None)
    humidity_air = data.get('humidity_air', None)

    cursor.execute('''
        INSERT INTO sensor_data (timestamp, ip_local, internet, humidity, luminosity, pasive_ir, humidity_ground, temperature_air, humidity_air)
        VALUES (?, ?, ? ,?, ?, ?, ?, ?, ?)
    ''', (timestamp, ip_local,internet,humidity, luminosity, pasive_ir, humidity_ground, temperature_air, humidity_air))

    conn.commit()
    conn.close()

def fetch_last_10_rows():
    conn, cursor = connect()
    cursor.execute('''
        SELECT * FROM sensor_data
        ORDER BY id DESC
        LIMIT 10
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows

def count_records():
    conn, cursor = connect()
    cursor.execute('''
        SELECT COUNT(*) FROM sensor_data
    ''')
    count = cursor.fetchone()[0]
    conn.close()
    return count

def clear_table():
    conn, cursor = connect()
    cursor.execute('''
        DELETE FROM sensor_data
    ''')
    conn.commit()
    conn.close()

main()