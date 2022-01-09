from flask.helpers import url_for
from app import app
from app import db
from flask import render_template, redirect
from app.models.tables import Post
from app.models.forms import PostForm
from app.models.forms import PostEditForm


@app.route("/",methods=['GET'])
def index():
    posts = Post.query.order_by(Post.date).all()
    
    return render_template('index.html', posts=posts)