from flask import Flask
from flask import render_template
from flask import request
import numpy as np
import pickle

app = Flask(__name__)

def setMethodValues(value):
	if value == 'sync':
		return 1, 0, 0
	elif value == 'async':
		return 0, 1, 0
	else:
		return 0, 0, 1

def setMechanimsValues(value):
	if value == 'theoric':
		return 1
	else:
		return 0

def setExamInteractionContact(value):
	if value == 'yes':
		return 1
	else:
		return 0

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
	methodSync, methodAsync, methodBoth = setMethodValues(request.form.get('method'))
	mechanism = setMechanimsValues(request.form.get('mechanism'))
	exam = setExamInteractionContact(request.form.get('exam'))
	interaction = setExamInteractionContact(request.form.get('interaction'))
	contact = setExamInteractionContact(request.form.get('contact'))

	resultValues = np.array([[methodSync, methodAsync, methodBoth, mechanism, exam, interaction, contact]])
	model = pickle.load(open('model.pkl', 'rb'))
	predictionValue = model.predict(resultValues)

	return render_template('index.html', prediction_text=predictionValue)

if __name__ == 'main':
	app.run(debug=True)
