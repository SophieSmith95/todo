from flask import Flask, request, jsonify
import uuid

users_array = []
tasks_array = []

class User:

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

	def to_dict(self):
		return {
			'username' : self.name,
			'email' : self.email
		}

class Task:

	def __init__(self, owner, description, due_date):
		self.owner = owner
		self.description = description
		self.due_date = due_date
		self.done = False
		self.id = uuid.uuid4()

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def users():
	if request.method == 'POST':
		message = request.json
		new_user = User(message['username'], message['email'], message['password'])
		users_array.append(new_user)
		return message['username'] + " has been created"
	else:
		return jsonify([n.to_dict() for n in users_array])

@app.route('/users/<username>', methods=['GET'])
def user(username):
	pass

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
	if request.method == 'POST':
		pass
	else:
		pass

@app.route('/tasks/<id>', methods=['GET'])
def task(id):
	pass
