from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return ('August 17, 1987')

@app.route('/greeting/<name>')
def greeting(name):
	return ('Hello ' + name)

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
	int_num1 = int(num1)
	int_num2 = int(num2)
	total = int_num1 + int_num2
	new_total = str(total)
	return new_total

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
	int_num1 = int(num1)
	int_num2 = int(num2)
	total = int_num1 * int_num2
	new_total = str(total)
	return new_total

@app.route('/subtract/<num1>/<num2>')
def subtract(num1, num2):
	int_num1 = int(num1)
	int_num2 = int(num2)
	total = int_num1 - int_num2
	new_total = str(total)
	return new_total

@app.route('/favoritefoods')
def favoritefoods():
	foods = ['steak', 'shrimp', 'ribs']
	str1 = ', '.join(foods)
	return jsonify(str1)
