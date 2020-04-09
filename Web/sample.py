from flask import Flask, render_template, session, redirect, url_for, request, flash
from markupsafe import escape

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def main():
    if 'username' in session:
        return render_template('main.html', is_anonymous=0)
    return render_template('main.html', is_anonymous=1)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['userpassword'])
        session['username'] = request.form['username']
        return redirect(url_for('main'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['userpassword'])
        print(request.form['re_userpassword'])
        session['username'] = request.form['username']
        return redirect(url_for('main'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run()
