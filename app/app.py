from flask import (
    Flask,
    render_template,
)


application = Flask(__name__)


@application.route('/')
def hello_world():
    return render_template('index.html')


@application.route('/buddyzm')
def buddyzm():
    return render_template('buddyzm.html')


if __name__ == '__main__':
    application.run()
