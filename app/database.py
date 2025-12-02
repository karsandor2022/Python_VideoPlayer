import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "videos.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')
    c.execute("SELECT COUNT(*) FROM videos")
    if c.fetchone()[0] == 0:
        c.executemany(
            "INSERT INTO videos (title, url) VALUES (?, ?)",
            [
                ("Sample Video 1", "https://www.youtube.com/embed/dQw4w9WgXcQ"),
                ("Sample Video 2", "https://www.youtube.com/embed/3JZ_D3ELwOQ")
            ]
        )
    conn.commit()
    conn.close()
