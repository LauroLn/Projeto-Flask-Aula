from flask import render_template, request
from datetime import date

Top100=[]
Jogadores= [{
    'nome': 'Lauro',
    'posicao': 50,
    'categoria': 'x2'
}]
def init_app(app):
    @app.route("/")  
    def home():  
        return render_template('index.html')

    @app.route("/jogadores", methods=['GET', 'POST'])
    def jogadores():
        if request.method =='POST':
            if request.form.get('nome') and request.form.get('posicao') and request.form.get('categoria'):
                Jogadores.append({'nome' : request.form.get('nome'), 'posicao' : request.form.get('posicao'), 'categoria' : request.form.get('categoria')})
                
        return render_template('jogadores.html', Jogadores = Jogadores)
    
    @app.route("/top", methods=['GET', 'POST'])
    def top():
        if request.method == 'POST':
            if request.form.get('jogador'):
              Top100.append(request.form.get('jogador'))
          

        return render_template('lista.html', Top100 = Top100)