from flask.helpers import url_for
from app import app
from app import db
from flask import render_template, redirect
from app.models.tables import Post
from app.models.forms import PostForm
from app.models.forms import PostEditForm
@app.route("/edit_post/<int:id>&<content>",methods=['GET','POST'])
def edit_post(id,content):
    edit_form = PostEditForm()
    if(edit_form.validate_on_submit):
        if edit_form.title.data != None:
            post = Post.query.get(edit_form.id.data)
            post.title = edit_form.title.data
            post.content = edit_form.content.data
            db.session.add(post)
            db.session.commit()
    return redirect(url_for('index'))

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
    edit_form = PostEditForm()
    if form.validate_on_submit:
        if(form.title.data != None and edit_form.id.data == None):
            post = Post(form.title.data,form.content.data)
            db.session.add(post)
            db.session.commit()
            redirect(url_for('index'))
    if(edit_form.validate_on_submit):
        try:
            edit_post = Post.query.get(edit_form.id.data)
            edit_post.title = edit_form.title.data
            edit_post.content = edit_form.content.data
            db.session.add(edit_post)
            db.session.commit()
            redirect(url_for('index'))
        except:
            print()
    return render_template('index.html', form=form, posts=posts, edit_form = edit_form)