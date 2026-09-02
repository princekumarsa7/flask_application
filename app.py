from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__, template_folder='Templates', static_folder='static')
app.secret_key = "change-this-secret"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user'):
            flash('Please log in to access the dashboard', 'warning')
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple demo authentication: accept any non-empty username/password
        if username and password:
            session['user'] = username
            flash('Logged in successfully', 'success')
            next_page = request.args.get('next') or url_for('dashboard')
            return redirect(next_page)
        flash('Invalid credentials', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    # Example data to show on dashboard
    stats = {
        'orders': 42,
        'products': 128,
        'users': 76,
        'revenue': '$5,420'
    }
    return render_template('dashboard.html', stats=stats, user=session.get('user'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)