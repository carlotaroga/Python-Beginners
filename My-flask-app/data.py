from flask import Flask, render_template

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    return render_template('templates/hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)