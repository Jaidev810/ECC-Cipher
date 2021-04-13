from curve import db



class ScatterMade(db.Model):
	index = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True)