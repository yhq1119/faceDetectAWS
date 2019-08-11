from flask import Flask, redirect, url_for

app = Flask(__name__)

date = "11/11/2011"


@app.route('/admin')
def hello_admin():
    return 'hello, admin!'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'hello, %s as a guest!' % guest


@app.route('/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# app.add_url_rule('/','fff',hello_world)

if __name__ == '__main__':
    app.run(debug=True)
