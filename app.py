from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == 'main':
	app.run(debug=True)
