from flask import Flask, render_template, request

from models.score_database_manager import DatabaseManager
from models.score import Score

app = Flask(__name__)

@app.route('/')
def homepage():
    manager = DatabaseManager()    # need to repeat it in each function bcuz flask can't work with sql query in global scope
    data = manager.get_all()
    manager.close()
    score_data = [score.to_dict() for score in data]
    return render_template("home.html", scores = score_data )

@app.route('/api/list')
def list_scores():
    manager = DatabaseManager()    # need to repeat it in each function bcuz flask can't work with sql query in global scope
    data = manager.get_all()
    manager.close()

    return {
        "scores": [score.to_dict() for score in data]
    }

if __name__ == "__main__":
    app.run(debug=True)