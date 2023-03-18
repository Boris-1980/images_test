from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cоздаем функцию для главной страницы
# эта функция определяет, что будет происходить, когда пользователь заходит на главную страницу приложения. 
# в данном случае, мы просто возвращаем HTML-шаблон "index.html", который мы создадим позже.
@app.route('/')
def index():
    return render_template('index.html')

# Добавляем конфигируацию для БД MySQL

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://<root>:<49166127a>@localhost/<dbname>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import os
from flask import request, redirect, url_for

@app.route('/upload', methods=['POST'])
def upload():
    # проверяем, что файл был загружен
    if 'image' not in request.files:
        return redirect(url_for('index'))

    # сохраняем загруженный файл на сервере
    image = request.files['image']
    filename = image.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    # сохраняем информацию об изображении в базе данных
    image = Image(filename=filename, url=filepath)
    db.session.add(image)
    db.session.commit()

    return redirect(url_for('index'))

import os

def create_app():
    app = Flask(__name__)
    ...
    
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
