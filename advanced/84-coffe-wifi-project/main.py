from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes
@app.route("/")
def home():
    return render_template("index.html")