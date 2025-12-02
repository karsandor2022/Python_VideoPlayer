from .database import get_connection

def get_all_videos():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, title FROM videos")
    videos = c.fetchall()
    conn.close()
    return videos

def get_video_url(video_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT url FROM videos WHERE id=?", (video_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def add_video(title, url):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO videos (title, url) VALUES (?, ?)", (title, url))
    conn.commit()
    conn.close()

def delete_video(video_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()
    conn.close()
