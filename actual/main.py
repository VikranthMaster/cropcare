from flask import Flask, render_template,request, redirect, url_for, flash
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired



def search(q):
    url = f'https://www.google.com/search?q={q}'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    mysearch = soup.find("div", class_="BNeawe").text
    return mysearch



app= Flask(__name__)
app.config['SECRET_KEY'] = 'asndjasnd'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        query = request.form.get('query')
        q1 = f"what is the best season to grow {query}"
        q2 = f"What is the market value of {query} in telangana for this month"
        q3 = f"give a brief description of {query}"
        q4 = f"What is the ideal temperature, rainfall and humidity to grow {query}"
        q5 = f"What is the best season to grow {query}"
        q6 = f"What are the best fertilizers and pesticides used to grow {query}"
        q7 = f"What are the different techniques used to grow {query} in india"
        q8 = f"What are the common diseases which occur to {query} and how to prevent them"
        q9 = f"What is the best time to harvest {query}"
        q10 = f"What is the average yield per acre output of {query}"
        q11 = f"What are the shelf life for {query}"
        q12 = f"What is the best soil to grow {query}"

        if query is not None:
            return render_template("main.html", name = query, q1=search(q1), q2=search(q2), q3=search(q3), q4=search(q4),
                                   q5 = search(q5), q6 = search(q6), q7 = search(q7), q8 = search(q8), q9 = search(q9), q10 = search(q10), q11 = search(q11), q12 = search(q12))
        else:
            return render_template("test.html")
    
    return render_template('test.html')

@app.route('/ai', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #         file.save(filepath)
    #         flash('File uploaded successfully!')
    #         return render_template('ai.html', uploaded_file=file.filename)
    # return render_template('ai.html')
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        return "File has been uploaded"
    return render_template("ai.html", form=form)

@app.route('/ai/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename=f'uploads/{filename}'))

if __name__ == '__main__':
    app.run(debug=True)