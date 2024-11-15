from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    # return render_template("login.html", s=False, user="Vik")
    # data = request.form
    # print(data)
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p> Logout</p>"

@auth.route('/sign-up',methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
    return render_template("singup.html")
