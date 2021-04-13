from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, SubmitField
from wtforms.validators import DataRequired


class CurveInput(FlaskForm):
	a = IntegerField("Enter a", validators=[DataRequired()])
	b = IntegerField("Enter b", validators=[DataRequired()])
	p = IntegerField("Enter p", validators=[DataRequired()])
	submit = SubmitField("See Stats")