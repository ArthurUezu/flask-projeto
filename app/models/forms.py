from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import data_required

class PostForm(FlaskForm):
    title = StringField('Título',validators=[data_required()])
    content = TextAreaField('Conteúdo',validators=[data_required()])
    submit = SubmitField('Postar')

class PostEditForm(FlaskForm):
    id = IntegerField()
    title = StringField()
    content = TextAreaField()
    btSubmit = SubmitField('btnSubmit')