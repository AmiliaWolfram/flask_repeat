from flask_login import UserMixin

from . import db, bcrypt, login_manager


# функция обратного вызова, чтобы получить объект через айдишку
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code = db.Column(db.String)

    # Отображение экхемпляра при обращении к нему
    def __repr__(self):
        return f"{self.name} - {self.code}"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    code_end = db.Column(db.String)
    summ = db.Column(db.Integer)
    amort_period = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # Просто теперь из айтема можно обратится к классу из одного в другой
    # lazy - отправляет второй запрос для айтемов, если нужны они, то он их отобразит
    category = db.relationship('Category', backref=db.backref('items', lazy='dynamic'))

    def __repr__(self):
        return f'{self.name} - {self.category.code}{self.code_end}'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, new_password):
        # берет наш пароль и делает шифрацию. Доступны будут только в скрытом виде
        self.password_hash = bcrypt.generate_password_hash(new_password).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.username

