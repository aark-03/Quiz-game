# Class Question
# properties: The question, The Options, The Answer
# methods: answer, ask

class Question:
  def __init__(self, question, options, answer):
    self.question = question
    self.options = options
    self.answer = answer
  def giveanswer(self):
    print(self.answer)
  def ask(self):
    print(self.question)
    for opt in self.options:
      print(opt)
    answer = input("Enter answer: ")
    if answer == self.answer:
      return True
    else: 
      return False

q1 = Question("how old am I?", ["13","17","57","12"], "12")
print(q1.ask())

# Class Quiz
# properties: Questions, name, grade
# methods: get question, score

class Quiz:
  def _init_(self, Question, name, grade):
    self.question = Question
    self.name = name
    self.grade = grade
