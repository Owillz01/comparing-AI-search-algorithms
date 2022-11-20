from flask import Flask, render_template, request

from SolvePuzzle import SolvePuzzle

# init flask 
app = Flask(__name__)

# define routes

@app.route("/")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/puzzle", methods=['POST', 'GET'])
def puzzle():
    output = request.form.to_dict()
    puzIndex = output["puzIndex"]
    puz = SolvePuzzle(int(puzIndex))
    solution = puz.solvePuzzle()
    return render_template("index.html", solution=solution)



if __name__ == '__main__':
    app.run(debug=True, port=1000)