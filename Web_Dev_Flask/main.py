from flask import Flask
import functools
app = Flask(__name__)
def log_access(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--> [SERVER LOG]: The '{func.__name__}' endpoint was just accessed!")
        result = func(*args, **kwargs)
        return result
    return wrapper
@app.route('/')
def home():
    return "<h1>Hello! Welcome to your first web server.</h1> <a href='/dashboard'>Go to Dashboard</a>"
@app.route('/dashboard')
@log_access
def secret_dashboard():
    return "<h1>Dashboard</h1><p>Check your PyCharm console! You should see a log message.</p>"

if __name__ == "__main__":
    print("Starting the web server... Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)