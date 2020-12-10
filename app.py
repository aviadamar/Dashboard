import db
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config.from_pyfile('dconfig.py')


@app.route("/")
def index():
    user = False
    user_links = False
    if session.get('username'):
        user = session['username']
        user_links = db.get_user_links(user)
    return render_template("index.j2", user=user, user_links=user_links)


@app.route("/<int:link_id>")
def remove(link_id):
    user = session.get('username')
    if session.get('username'):
        db.remove_from_board(link_id, user)
    return redirect(url_for('index'))


@app.before_request
def _db_connect():
    db.database.connect()


@app.teardown_request
def _db_close(_):
    if not db.database.is_closed():
        db.database.close()


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    status = {
        'valid_username': True,
        'available_username': True,
        'valid_email': True,
        'valid_password': True,
        'password_validation': True,
    }
    valid = False

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_validation = request.form['password_validation']

        status = db.registration_validation(status, username, email,
                                            password, password_validation)

        if all(bool(value) for value in status.values()):
            valid = True
            db.create_user(username, email, password)

    return render_template("register.j2", status=status, valid=valid)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    error = False
    if request.method == 'GET':
        return render_template("login.j2", error=error)

    username = request.form['username']
    password = request.form['password']

    user = db.get_user(username)
    if user and db.verify_password(user, password):
        session['username'] = user.username
        return redirect(url_for('index'))

    error = True
    return render_template("login.j2", error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username') is None:
        return redirect(url_for('index'))

    session.clear()
    return redirect(url_for('index'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    username = session.get('username')
    if username is None:
        return redirect(url_for('index'))

    valid = False
    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        description = request.form['description']
        valid = db.create_link(name, url, description, username)
        return redirect(url_for('index'))
    return render_template("add.j2", valid=valid)


if __name__ == '__main__':
    app.run()
