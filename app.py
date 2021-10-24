from flask import Flask, render_template, request
from Fipe import Fipe

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        codigo = request.form.get('name')
        try:
            fipe = Fipe(codigo)
        except Exception as E:
            return f'<script>alert(`{E}`);</script>'
        else:
            values = [fipe.marca, fipe.modelo, fipe.valor]
            return pag2(values)

        
@app.route('/')
def pag2(values):
    return render_template('pag2.html', values=values)


@app.route('/<string:nome>')
def error(nome):
    mensagem = f'Página " {nome} " não existe'
    return render_template('error.html', mensagem= mensagem)

app.run(debug=True)