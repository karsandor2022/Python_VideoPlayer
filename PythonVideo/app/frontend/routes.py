from flask import Blueprint, render_template
from .services import get_videos

bp = Blueprint("frontend", __name__)

@bp.route("/")
def index():
    videos = get_videos()
    return render_template("index.html", videos=videos)