from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

blog_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(blog_url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        user_message = request.form.get("message")

        OWN_EMAIL = "your_testing_email@gmail.com"
        OWN_PASSWORD = "your_app_password"

        email_message = f"Subject:New Message from {user_name}!\n\nName: {user_name}\nEmail: {user_email}\nMessage: {user_message}"

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
                connection.sendmail(
                    from_addr=OWN_EMAIL,
                    to_addrs=OWN_EMAIL,
                    msg=email_message
                )
            return render_template("contact.html", msg_sent=True)

        except Exception as e:
            print(f"Error sending email: {e}")
            return render_template("contact.html", msg_sent=False)

    return render_template("contact.html", msg_sent=False)


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