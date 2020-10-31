from flask import Flask , render_template , request
import pickle
import numpy as np

# Loading the pickle file of the model

filename = 'ipl_score_innings_prediction_model.pkl'

regressor = pickle.load(open(filename , 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)


