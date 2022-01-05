from app import app
from app import db
from flask import render_template
from app.models.tables import Post
from app.models.forms import PostForm
@app.route("/",methods=['GET','POST'])
def index():
    posts = Post.query.all()
    form = PostForm()
    if form.validate_on_submit:
        if(form.title.data != None):
            post = Post(form.title.data,form.content.data)
            db.session.add(post)
            db.session.commit()
    return render_template('index.html', form=form, posts = posts)