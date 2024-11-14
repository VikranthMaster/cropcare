from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates')
app.secret_key = "himynameisvikranth"


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/detect")
def about():
    return render_template('detect.html')

if __name__ == '__main__':
    app.run(debug=True)