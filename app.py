from flask import Flask, render_template, request
import marks

app = Flask(__name__)

@app.route("/")
def hello():
   

    return render_template("index.html")

@app.route('/sub', methods = ['POST'])
def submit():
    if request.method == "POST":
        area = request.form['area']
        dist_praia = request.form['dist_praia']
        marks_pred = marks.marks_prediction(area, dist_praia)
        print("teste: ",marks_pred)

    return render_template("index.html", my_marks = marks_pred)

if __name__ == "__main__":
    app.run(debug=True)