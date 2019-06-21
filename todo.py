class User:

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

class Task:

	def __init__(self, owner, description, due_date):
		self.owner = owner
		self.description = description
		self.due_date = due_date
		self.done = False
