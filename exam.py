from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(66))
    password = db.Column(db.String(66))


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/index/")
def index():
    uu = User.query.all()
    return render_template("index.html", uu=uu)


@app.route("/insert/", methods=["GET", "POST"])
def insert():
    gg = User.query.all()
    if request.method == "GET":
        return render_template("insert.html", uu=gg)
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        a = User(name=name, password=password)
        db.session.add(a)
        db.session.commit()
        return redirect("/index/")


@app.route("/delete/<id>")
def delete(id):
    uu = User.query.filter(User.id == id).first()
    if uu:
        db.session.delete(uu)
        db.session.commit()
        return redirect("/index/")


@app.route("/update/<u_id>", methods=["GET", "POST"])
def update(u_id):
    uu = User.query.filter(User.id == u_id).first()
    if request.method == "GET":
        return render_template("update.html", uu=uu)
    else:
        name = request.form.get("name")
        password = request.form.get("password")
        if name == "":
            pass
        else:
            uu.name = name
        if password == "":
            pass
        else:
            uu.password = password
        db.session.commit()
        return redirect("/index/")


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    u1 = User(name="sab", password="123456")
    u2 = User(name="二哥", password="654321")
    u3 = User(name="三哥", password="789jqk")
    db.session.add_all([u1, u2, u3])
    db.session.commit()
    app.run(debug=True)
