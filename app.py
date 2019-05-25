
# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from models import db, Node, User, Question


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://admin:HhXkh5UGNNgrjpk@cluster0-txgpn.mongodb.net/test?retryWrites=true',
    'connect': False,
    'maxPoolSize':  1,
}
db.init_app(app)

@app.route('/')
def index():
    nodes = Node.objects()

    return render_template('index.html', nodes=nodes)

@app.route('/question/<id>')
def question(id):
    from random import choice, sample
    question = choice(Question.objects(node=id))
    question.choices = sample([ question.correct_answer ] + sample(question.distractors, 3), 4)
    return render_template('question.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
    question = Question.objects.get(id=request.form['id'])
    if question.correct_answer == request.form['answer']:
        return render_template('correct_answer.html', question=question, answer=request.form['answer'])
    else:
        return render_template('wrong_answer.html', question=question, answer=request.form['answer'])
