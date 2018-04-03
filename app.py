# imports
from flask import Flask, render_template, logging, redirect, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

# Initializing MongoDB
client = MongoClient('localhost', 27017)
db = client.iitdost

# Collections
staffs = db.staffs
students = db.students
appointments = db.appointments

# Initializing app
app = Flask(__name__)
# app.config["MONGO_DBNAME"]='iitdost'
# mongo = PyMongo(app)


# Homepage
@app.route('/')
def index():
	# online_users = mongo.db.users.find({'online': 'True'})
	online_users = staffs.find({'online': True})
	return render_template('index.html', online_users=online_users)
	# app.logger.info(app.name)

# Adding staffs
@app.route('/add_staff/<string:name>/<string:dept>/<string:typef>/<string:room>')
def add_staff(name,dept,typef,room):
	staff = {'name':name, 'dept':dept, 'type':typef, 'room':room, 'online':True}
	staffs.insert(staff)
	return redirect(url_for('index'))

# All Staffs
@app.route('/staff')
def staff():
	staff_ = staffs.find({})
	return dumps(staff_)

# All Students
@app.route('/student')
def student():
	student_ = students.find({})
	return dumps(student_)

# All Appointments
@app.route('/appointment')
def appointment():
	appointment_ = appointments.find({})
	return dumps(appointment_)


# Remove all the data
@app.route('/refresh')
def refresh():
	# db.users.drop()
	db.staffs.drop()
	db.students.drop()
	db.appointments.drop()
	return redirect(url_for('index'))


# Starting App
if __name__ == '__main__':
	app.run(debug=True)