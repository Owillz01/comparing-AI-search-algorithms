from flask import Flask, render_template, request

from SolvePuzzle import SolvePuzzle
import State as pz
import threading
import time

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
    # return render_template("index.html", greedy_best=greedy_best, states=enumerate(states))
    return render_template("index.html", a_Start=a_Start, greedy_best=greedy_best, states=enumerate(states), puzIndex=puzIndex)

def web():
    app.run(debug=True, use_reloader=False, port=1000)

if __name__ == '__main__':
    threading.Thread(target=puzzle, daemon=True).start()
    threading.Thread(target=web, daemon=True).start()
    while True:
        time.sleep(1)
    # app.run(debug=True, port=1000) 