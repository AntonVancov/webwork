from flask import Flask, url_for


app = Flask(__name__)


@app.route('/')
def colonization():
    return "Миссия Колонизация Марса!"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def lozung():
    return f'Человечество вырастает из детства.' \
           f'</br>Человечеству мала одна планета.' \
           f'</br>Мы сделаем обитаемыми безжизненные пока планеты.' \
           f'</br>И начнем с Марса!' \
           f'</br>Присоединяйся!'


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс!</h1>
    <img src="{url_for('static', filename='img/Mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')