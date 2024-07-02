from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumar', methods=['POST'])
def sumar():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    resultado = num1 + num2
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
