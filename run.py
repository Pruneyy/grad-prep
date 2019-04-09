from flask import Flask, render_template, redirect, url_for, request
from database import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        route = request.form['submit']
        return redirect(url_for(route))
    return render_template('index.html')
@app.route('/add', methods=['GET', 'POST'])

def add():
    message = None
    flag = None

    if request.method == 'POST':

        if request.form['submit'] == 'home':
            return redirect(url_for('index'))

        question = request.form['question']
        answer = request.form['answer']
        add_db(question, answer)
        message = "Successfully added to database"
        flag = True

    return render_template('add.html', message=message, flag=flag)

@app.route('/view', methods=['GET', 'POST'])
def view():
    responses = query_db()

    if request.method == 'POST':

        if request.form['submit'] == 'home':
            return redirect(url_for('index'))
    
    return render_template('view.html', responses=responses)

if __name__ == '__main__':
    if not check_db():
        create_db()
    query_db()
    app.run()

