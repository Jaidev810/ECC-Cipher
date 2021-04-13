from curve import curves, db
from flask import render_template, redirect, flash, session, url_for
from curve.forms import CurveInput
from curve.models import ScatterMade
from coreCode.maker import Grapher
import matplotlib.pyplot as plt
import os

## for logging out redirect to a url which pops out the username

base_dir = os.path.abspath(os.path.dirname(__file__))


def prime(number):
	if number == 2: return True
	if number%2 == 0: return False

	if number == 3: return True
	if number%3 == 0: return False

	if number == 5: return True
	
	t = 5
	inc = 2
	while t*t <= number:
		if number%t == 0:
			return False
		t += inc
		inc = 6 - inc
	return True

def getName(a,b,p):
	return "im"+str(a)+"&"+str(b)+"&"+str(p)+".png"

def saveImage(counter,a,b,p):
	image_name = getName(a,b,p)
	points = list(counter.keys())
	size = list(counter.values())
	plt.scatter([p.x for p in points],[p.y for p in points],s=size)
	plt.savefig(base_dir+"/static/"+image_name)
	plt.close()

def getGenerators(degree):
	lisi = [(degree[x],x.x,x.y) for x in degree]
	sorted(lisi,reverse=True)
	return [(lisi[i][1],lisi[i][2]) for i in range(min(len(lisi),5))]

def getVariance(counter):
	lisi = [counter[x] for x in counter]
	s = sum(lisi)
	average = s/len(lisi)
	temp = 0
	for i in lisi:
		temp += pow(average-i,2)
	return (average,pow((temp/(len(lisi)-1)),0.5))


def getDict(a,b,p):
	params = dict()
	params["a"] = a
	params["b"] = b
	params["p"] = p
	previous = ScatterMade.query.filter_by(name=getName(a,b,p)).first()
	params["image"] = getName(a,b,p)
	grapher = Grapher()
	counter,degree = grapher.makeCurve(a,b,p)
	params['generators'] = getGenerators(degree)
	## 5 generator points and then the variance of the counter
	params['avgStd'] = getVariance(counter)
	if not previous:
		saveImage(counter,a,b,p)
		n = ScatterMade(name=getName(a,b,p))
		db.session.add(n)
		db.session.commit()
	return params
	

@curves.route("/")
def red1():
	return redirect("/made")


@curves.route("/made")
def made():
	previous = ScatterMade.query.all()
	return render_template("prev.html",previous=previous)



@curves.route("/curve", methods=["GET","POST"])
def take_input():
	form = CurveInput()
	if form.validate_on_submit():
		if form.p.data > 150 or not prime(form.p.data):
			flash("Invalid Input")
			return redirect(url_for("cy.take_input"))
		return redirect("/curve/%d&%d&%d"%(form.a.data,form.b.data,form.p.data))
	return render_template('curveinp.html',form=form)



@curves.route("/curve/<numbers>", methods=["GET","POST"])
def put_curve(numbers):
	a,b,p = map(int,numbers.split("&"))
	return render_template("final_curve.html",params=getDict(a,b,p))


