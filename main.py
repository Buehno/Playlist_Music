from flask import Flask, render_template , redirect , request , session, flash, url_for

class Musica:
        def __init__(self,  nome , cantorGrupoBanda, genero):
                self.nome = nome
                self.cantorBanda = cantorGrupoBanda
                self.genero = genero

Musica01  = Musica("Temporal", "Hungria" , "RAP")
Musica02  = Musica("Papai Banca", "MC Ryan sp" , "Funk")
Musica03 = Musica("Camisa 10", "Turma do Pagode" , "RAP")
        
lista = [Musica01 ,Musica02, Musica03]

class Usuario:
        def __init__(self, nome, login, senha):
                self.nome  =  nome
                self.login = login
                self.senha = senha
Usuario01 = Usuario("Bueno", 'Buenozim_', 'admin')
Usuario02 = Usuario('joão', 'JoãoPaulo', '123456')
Usuario02 = Usuario('Vilma Nuner', 'VilmaNunes123', 'V4545')


app = Flask(__name__)

app.secret_key = 'primeiroprojetoflask'

@app.route("/")
def listarMusicas():

        if  'usuario_logado' not in session or  session['usuario_logado'] == None:
                return redirect(url_for('logar'))
        return render_template("index.html", titulo = "Lista de musicas" , 
                               musicas = lista)

@app.route("/cadastrar")
def cadastrar_musica():
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
                return redirect(url_for('logar'))
        
        return render_template('cadastra_musica.html',
                                titulo = "Cadastrar Musicas")
                
@app.route('/adicionar', methods = ['POST' , ])
def adicionar_muscia():
        nome = request.form['txtNome']
        cantorBanda = request.form['txtCantor']
        genero  = request.form['txtGenero']

        novamusica = Musica(nome, cantorBanda , genero)

        lista.append(novamusica)

        return redirect(url_for('listarMusicas'))

@app.route('/login')
def logar():
        return render_template('login.html')


@app.route('/autenticar',  methods=['POST' , ])
def  autenticar():
        if request.form['txtSenha'] == 'admin':
                session['usuario_logado'] = request.form['txtLogin']
                flash("Olá, " +  session['usuario_logado'])

                return redirect(url_for("listarMusicas"))
        else:
                flash("Usuario ou Senha Invalida!")
                return redirect(url_for('logar'))

@app.route('/sair')
def sair():
        session['usuario_logado'] = None
        return redirect('/login')
app.run(debug=True)
