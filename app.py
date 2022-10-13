from flask import Flask, render_template
from random import choice
"""    // <link href="./my_site/styles.css" rel="stylesheet" /> 
    <div class="menu">"""

menu = [{"title": 'Главная', "url": "hello"},
        {"title": 'Помощь', "url": "help"},
        {"title": "О программе", "url": "about"},
        {"title": "Nyan Cat", "url": "NyanCat"}]

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html', menu=menu)


@app.route('/help/')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp), menu=menu)


@app.route('/Nyan Cat/')
def NyanCat():
    return render_template('Nyan Cat.html', title="Nyan Cat", menu=menu)


@app.route('/about/')
def about():
    return render_template('about.html', title="about", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
