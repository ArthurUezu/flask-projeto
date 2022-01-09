from flask.helpers import url_for
from flask.templating import render_template
from flask_login.utils import logout_user
from app import app
from app import db
from app.models.tables import Post
from flask import redirect
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user,login_user,logout_user
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField
from wtforms.validators import data_required
from werkzeug.security import generate_password_hash,check_password_hash
login = LoginManager(app)

class Adm(db.Model,UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    username = db.Column(db.String)
    password = db.Column(db.String[128])
    
    def set_password(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password, password)

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[data_required()])
    password = StringField('Senha',validators=[data_required()])
    submitBtn = SubmitField('Login')

@login.user_loader
def load_user(user_id):
    return Adm.query.get(user_id)
class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('index'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        if form.username.data != None:
            adm = Adm.query.filter_by(username=form.username.data).first()
            if adm.check_password(form.password.data):
                login_user(adm)
                return redirect(url_for('admin.index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
admin = Admin(app, index_view=MyAdminIndexView())

admin.add_view(MyModelView(Post,db.session))