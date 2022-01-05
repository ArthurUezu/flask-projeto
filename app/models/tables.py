from datetime import datetime
from app import db

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    def __init__(self, title, content):
        self.title = title
        self.content = content
        