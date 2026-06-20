from flask import Flask, render_template, request
from resume_parser import extract_text, analyze_resume


app = Flask(__name__)



@app.route("/")
def home():

    return render_template("index.html")




@app.route("/analyze", methods=["POST"])
def analyze():


    file = request.files["resume"]


    text = extract_text(file)


    result = analyze_resume(text)


    return render_template(
        "index.html",
        result=result
    )




if __name__ == "__main__":

    app.run(debug=True)