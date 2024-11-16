from flask import Flask, render_template,request, redirect, url_for, flash
import os
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/plant_model.h5"
# Load the pre-trained model
model = tf.keras.models.load_model("plantmodel.h5")

# loading the class names
class_indices = json.load(open(f"{working_dir}/class_indices.json"))



# Function to Load and Preprocess the Image using Pillow
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load the image
    img = Image.open(image_path)
    # Resize the image
    img = img.resize(target_size)
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Scale the image values to [0, 1]
    img_array = img_array.astype('float32') / 255.
    return img_array


# Function to Predict the Class of an Image
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name


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
        q2 = f"What is the market value of {query}"
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
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        print("File uploaded")
        uploaded_image = f"static/uploads/{os.listdir('static/uploads')[0]}"
        image = Image.open(uploaded_image)
        prediction = predict_image_class(model, uploaded_image, class_indices)
        return f"<h1>{prediction}</h1>"
    return render_template("ai.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)