from flask import Flask, render_template,request, redirect, url_for
import requests
from bs4 import BeautifulSoup



def search(q):
    url = f'https://www.google.com/search?q={q}'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    mysearch = soup.find("div", class_="BNeawe").text
    return mysearch



app= Flask(__name__)
app.config['SECRET_KEY'] = 'asndjasnd'

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

if __name__ == '__main__':
    app.run(debug=True)