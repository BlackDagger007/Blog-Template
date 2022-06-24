from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = blog_response.json()


@app.route("/")
def home():
    return render_template("index.html", blogs=blog_data)


@app.route("/blog/<int:post_id>")
def goto_post(post_id):
    return render_template("post.html", blogs=blog_data, post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
