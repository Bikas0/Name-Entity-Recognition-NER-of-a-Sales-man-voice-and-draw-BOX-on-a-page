from flask import Flask, render_template, request
from nameEntity import Name_Entity

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=["GET","POST"])
def ner():
    if request.method == "POST":
        name = Name_Entity()
        return render_template('results.html', result= name)
        

if __name__ == '__main__':
    app.run(debug=True)