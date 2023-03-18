from app import db

# Здесь мы определяем две модели данных: "Image" и "User". 
# Модель "Image" будет использоваться для хранения информации о загруженных изображениях,
# а модель "User" - для хранения информации о пользователях приложения.

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)