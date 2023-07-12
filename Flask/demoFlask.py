from flask import Flask , url_for , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(r"index.html")

if __name__ == "main":
    app.run(debug=False,port=8080)