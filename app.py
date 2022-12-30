from flask import Flask, render_template, request

from SolvePuzzle import SolvePuzzle
import State as pz

# init flask 
app = Flask(__name__)

# define routes

@app.route("/")

@app.route("/home")
def home():
    states = pz.getAllInstance()
    return render_template("index.html", states=enumerate(states))


@app.route("/puzzle", methods=['POST', 'GET'])
def puzzle():
    output = request.form.to_dict()
    puzIndex = output["puzIndex"]
    puz = SolvePuzzle(int(puzIndex))
    a_Start = puz.solvePuzzleA_star()
    greedy_best = puz.solvePuzzleGreedy()
    states = pz.getAllInstance()
    return render_template("index.html", a_Start=a_Start, greedy_best=greedy_best, states=enumerate(states))



if __name__ == '__main__':
    app.run(debug=True, port=1000)