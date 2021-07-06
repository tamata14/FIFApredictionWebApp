# -*- coding: utf-8 -*-

import flask
import pickle
import pandas as pd

with open(f'model/fifaOverall.pkl', 'rb') as f:
    model = pickle.load(f)




app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
            height_cm = flask.request.form['height_cm']
            weight_kg = flask.request.form['weight_kg']
            age = flask.request.form['age']
            dribbling = flask.request.form['dribbling']
            pace = flask.request.form['pace']
            physic = flask.request.form['physic']
            defending = flask.request.form['defending']
            shooting = flask.request.form['shooting']
            passing = flask.request.form['passing']
            
            input_variables = pd.DataFrame([[ height_cm, weight_kg, age, dribbling, pace, physic, defending, shooting, passing]], columns=['height_cm', 'weight_kg', 'age', 'dribbling', 'pace', 'physic', 'defending', 'shooting', 'passing'], dtype=float)
            
            prediction = model.predict(input_variables) [0]
            
    return flask.render_template('main.html', original_input = {
        'Height':height_cm,
        'Weight':weight_kg,
        'Age':age,
        'Dribbling':dribbling,
        'Pace':pace,
        'Physical':physic,
        'Defending':defending,
        'Shooting':shooting,
        'Passing':passing
        
        },
        result=prediction
        )

if __name__ == '__main__':
    app.run()