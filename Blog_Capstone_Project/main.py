from flask import Flask, render_template
import requests

app = Flask(__name__)

api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)
all_posts = response.json()  # Converts the JSON response into a Python List of Dictionaries


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == post_id:
            requested_post = blog_post

    # Pass just that single post to the post.html template
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)