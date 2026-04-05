from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", post=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = None
    for post in all_posts:
        if post["id"] == post_id:
            requested_post = post
            break
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
