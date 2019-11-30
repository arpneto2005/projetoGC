from flask import Flask, redirect, url_for, request, abort, render_template
from json import dumps

app = Flask(__name__, static_folder='public', template_folder='templates')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dados', methods=['POST'])
def dados():
    resultados = dumps(request.form)    
    dados = sum([int(v) for v in request.form.to_dict().values()])

    return render_template('resultados.html', dados=dados, items = resultados)

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0', port=2020)