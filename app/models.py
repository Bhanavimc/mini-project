# app/models.py
from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skills = db.Column(db.String(500))
    career_interests = db.Column(db.String(200))

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    required_skills = db.Column(db.String(500))
    career_field = db.Column(db.String(200))
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
