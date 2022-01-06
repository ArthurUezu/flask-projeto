from flask.helpers import url_for
from app import app
from app import db
from flask import render_template, redirect
from app.models.tables import Post
from app.models.forms import PostForm

@app.route("/delete_post/<int:id>",methods=['GET','POST'])
def delete_post(id):
    
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/",methods=['GET','POST'])
def index():
    posts = Post.query.order_by(Post.date).all()
    form = PostForm()
    if form.validate_on_submit:
        if(form.title.data != None):
            post = Post(form.title.data,form.content.data)
            db.session.add(post)
            db.session.commit()
            redirect(url_for('index'))
    return render_template('index.html', form=form, posts = posts)