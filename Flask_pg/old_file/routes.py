from flask import render_template, request, url_for, abort, session, redirect
import json
from db import news_db, flowers_db, user_db
from forms import LoginForms, Sign_inForm
from datetime import timedelta
from my_app import app


@app.route("/homework_home")
def home_page():
    session_id = session.get('username', 'UNKNOWN USER')
    return render_template('home.html', data=news_db, session_id=session_id)


@app.route('/list_of_flowers')
def list_of_flowers_page():
    return render_template('list_of_flowers.html', data=flowers_db, title='List of flowers',
                           session_id=session['username'])


@app.route("/list_of_flowers/flower/<string:flower_name>")
def flower_page(flower_name):
    flower_name_1 = (flowers_db.get(flower_name))['name']
    flower_image = (flowers_db.get(flower_name))['image']
    flower_meaning = (flowers_db.get(flower_name))['meaning']
    return render_template('flower.html', flower_name_1=flower_name_1, flower_image=flower_image,
                           flower_meaning=flower_meaning, title='Flower', session_id=session['username'])


def check_flowers(flower_name: str) -> bool:
    return flower_name in flowers_db.keys()


@app.route('/all_flower')
def get_all_flower():
    return do_get_all()


@app.route('/all_flower/<string:flower_name>', methods=['GET', 'POST', 'DELETE'])
def test_methods(flower_name=None):
    if request.method == 'POST':
        return do_post(flower_name)
    if request.method == 'DELETE':
        return do_delete(flower_name)
    else:
        return do_get_certain(flower_name)


def do_post(flower_name):
    params = json.loads(request.data.decode('utf-8'))
    flowers_db[flower_name] = params
    result = {"status": "OK", "message": f"Add new user {params}"}
    return json.dumps(result)


def do_get_all():
    return render_template('test_methods.html', values=flowers_db)


def do_get_certain(flower_name):
    if not check_flowers(flower_name):
        result = {"status": "Fail", "message": "I dont know about such flower. Sorry"}
    else:
        certain_flower = flowers_db.get(flower_name)
        result = {"status": "OK", "message": f"We find your flower {certain_flower}"}
    return json.dumps(result)


def do_delete(flower_name):
    if not check_flowers(flower_name):
        result = {"status": "Fail", "message": "I dont know about such flower. Sorry"}
    else:
        del flowers_db[flower_name]
        result = {"status": "Ok", "message": f"Delete flower '{flower_name}'"}
    return json.dumps(result)


@app.route("/flower_error")
def test_redirect():
    abort(404, "Value error")


@app.errorhandler(404)
def error_404_handler(error):
    return render_template("error_404.html")


def check_user(user_name: str) -> bool:
    return user_name in user_db.keys()


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForms()
    if login_form.validate_on_submit():
        if login_form.username.data in user_db.keys():
            if login_form.password.data == str(user_db[login_form.username.data].get('password')):
                session['username'] = login_form.username.data
                return redirect(url_for('home_page'))
            else:
                pass
        else:
            result = 'This username not exists. Please registration <a href="/sign_in">Sign_in</a>'
            return result
    return render_template("login.html", title="Login", form=login_form)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    sign_in_form = Sign_inForm()
    if sign_in_form.validate_on_submit():

        if check_user(sign_in_form.s_username.data):
            result = 'User name already exists Please login: <a href="/login">Login</a>'
            return result
        else:
            new_user = {"name": sign_in_form.s_username.data, "age": sign_in_form.s_age.data,
                        "password": sign_in_form.s_password.data, "e-mail": sign_in_form.s_email.data}
            user_db[sign_in_form.s_username.data] = new_user
            result = 'New user {} successfully created. Please login: <a href="/login">Login</a>'.format(sign_in_form.s_username.data)
            return result

    return render_template("sign_in.html", title="Sign_in", form=sign_in_form)



