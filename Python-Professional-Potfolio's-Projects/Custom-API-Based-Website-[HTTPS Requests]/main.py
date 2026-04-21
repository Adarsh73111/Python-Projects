from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = ""
    apod_data = None

    if request.method == 'POST':
        date = request.form.get('date')
        url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={date}"
        response = requests.get(url)
        if response.status_code == 200:
            apod_data = response.json()

    # Un-indented this else block so it aligns with the 'if' statement
    else:
        url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
        response = requests.get(url)
        if response.status_code == 200:
            apod_data = response.json()

    # Un-indented the return statement so it runs for BOTH GET and POST requests
    return render_template('index.html', apod_data=apod_data)


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request, request_started
# import requests
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
#
# def index ():
#     data = ""
#     apod_data = None
#
#     if request.method == 'POST':
#         date = request.form.get('date')
#         url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={date}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             apod_data = response.json()
#         else:
#             url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
#             response = requests.get(url)
#             if response.status_code == 200:
#                 apod_data = response.json()
#
#         return render_template('index.html', apod_data = apod_data)
#
# if __name__ == '__main__':
#     app.run(debug = True)
#
#
