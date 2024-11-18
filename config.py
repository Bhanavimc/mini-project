import os

class Config:
    SECRET_KEY = os.urandom(24)  # Secret key for Flask sessions
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Optional to disable unnecessary modifications tracking
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Update with your database URI if needed
