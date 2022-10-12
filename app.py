from flask import Flask, render_template
from random import choice

"""https://colorhunt.co/palette/064635519259f0bb62f4eea9           <---цветовая палитра"""

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('home.html')


@app.route('/help/')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp))


@app.route('/Nyan Cat/')
def NyanCat():
    return render_template('Nyan Cat.html', title="Nyan Cat")


if __name__ == '__main__':
    app.run(debug=True)
