from flask import Flask, render_template, request, redirect, session, url_for
from oauth import Oauth
# import flask_sqlalchemy

app = Flask(__name__)
app.secret_key = Oauth.client_secret
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(300), nullable=False)

# @app.route("/")
# def index():
#     return render_template('index.html')


@app.route("/", methods = ["get"])
def index():
    return render_template('index.html')
    # return redirect(Oauth.discord_login_url)

@app.route("/login", methods = ["get"])
def login():
    code = request.args.get("code")
    at = Oauth.get_access_token(code)

    user_json = Oauth.get_user_json(at)
    username, avatar, id = user_json.get("global_name"), user_json.get("avatar"), user_json.get("id")
    avatar_url = f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png"

    session['username'] = username
    session['avatar_url'] = avatar_url

    return redirect(url_for('index'))

@app.route("/logout", methods = ["get"])
def logout():
    session.clear()  # Удаляет информацию о пользователе из сессии
    return redirect(url_for('index'))  # Перенаправляет пользователя на главную страницу


if __name__ == '__main__':
    app.run(debug=False)
