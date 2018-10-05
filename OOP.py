from abc import ABC

class User(ABC):

	user_count=0

	def __init__(self, username, email, password):
		User.user_count += 1
		self.id = User.user_count
		self.username = username
		self.email = email
		self.password = password
		self.questions = []
		self.answers = []

	def post_question(self, post, tag):
		self.questions.append(post)
		qtn = Question(post,tag)
		
	def post_answer(self, post, question):
		self.answers.append(post)
		ans = Answer(post, question)
		
class Question():
	qstn_count=0
	def __init__(self, post, tag):
		Question.qstn_count +=1
		self.id = Question.qstn_count
		self.post = post
		self.tag = tag
		self.answers = []

	def get_answers(self):
		return self.answers

	def get_owner(self):
		return self.owner


class Answer():
	def __init__(self, post, question, user):
		self.owner = User.user.username
		self.question = Question.id

	def get_question(self):
		return self.question

	def get_owner(self):
		return self.owner

	
		