from flask import Flask, render_template, request, redirect, url_for
from .models import get_all_videos, get_video_url, add_video, delete_video

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        selected_video = None
        videos = get_all_videos()

        if request.method == "POST":
            video_id = request.form.get("video_id")
            if video_id:
                selected_video = get_video_url(video_id)

        return render_template("index.html", videos=videos, selected_video=selected_video)

    @app.route("/add", methods=["POST"])
    def add():
        title = request.form.get("title")
        url = request.form.get("url")
        if title and url:
            add_video(title, url)
        return redirect(url_for("index"))

    @app.route("/delete/<int:video_id>")
    def delete(video_id):
        delete_video(video_id)
        return redirect(url_for("index"))

    return app
