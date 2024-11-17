from flask_login import LoginManager
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

sqlite_database = "sqlite:///users.db"

# создаем движок SqlAlchemy
engine = create_engine(sqlite_database)


class Base(DeclarativeBase): pass


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)
@app.route('/')

def index():
    return render_template('KURSpoBD.html')


@app.route('/base1')

def base1():
    return render_template('KURS_BASE_1.html')

@app.route('/base2')

def base2():
    return render_template('KURS_BASE_2.html')

@app.route('/base3')

def base3():
    return render_template('KURS_BASE_3.html')

@app.route('/base4')

def base4():
    return render_template('KURS_BASE_4.html')

@app.route('/base5')

def base5():
    return render_template('KURS_BASE_5.html')

@app.route('/profil')

def profil():
    return render_template('KURS_Profil.html')

@app.route('/reg')

def reg():
    return render_template('register.html')

@app.route('/log')

def log():
    return render_template('login.html')

@app.route("/contact", methods=["POST"])
def contact():
    if request.method == 'POST':
        print(request.form)

    return render_template('KURSpoBD.html')

if __name__ == '__main__':
    app.run(debug=True)

login_manager =LoginManager(app)