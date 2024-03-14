from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'CHAVE FORTE'

bootstrap = Bootstrap(app)

moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    lastname = StringField('Informe o seu sobrenome:', validators=[DataRequired()])
    insname = StringField('Informe a sua instituição de ensino:', validators=[DataRequired()])
    discname = SelectField('Informe a sua disciplina:', choices=[('SODA5', 'SODA5'), ('DSWA5', 'DSWA5'), ('TCOA5', 'TCOA5')])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    url = request.remote_addr
    ip = request.host_url
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['lastname'] = form.lastname.data
        session['insname'] = form.insname.data
        session['discname'] = form.discname.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), lastname=session.get('lastname'), insname=session.get('insname'), discname=session.get('discname'), url=url, ip=ip, current_time=datetime.utcnow())
