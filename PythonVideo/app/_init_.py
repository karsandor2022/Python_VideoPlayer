from flask import Flask
from fastapi import FastAPI

# Flask App
flask_app = Flask(__name__)

# FastAPI App
fastapi_app = FastAPI(title="Video API Backend")