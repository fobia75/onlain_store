from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('base.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cloth')
def cloth():
    return render_template('cloth.html')


@app.route('/jackets')
def jackets():
    return render_template('jackets.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


if __name__ == '__main__':
    app.run(debug=True)