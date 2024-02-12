from flask import Flask, url_for, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Домашняя страница')


@app.route('/training/<prof>')
def image(prof):
    return render_template('index2.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('index3.html', list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')