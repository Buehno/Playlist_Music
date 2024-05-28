from flask import render_template , redirect , request , session, flash, url_for
from models import Musica, Usuario
from main import db, app

@app.route("/")
def listarMusicas():

        if  'usuario_logado' not in session or  session['usuario_logado'] == None:
                return redirect(url_for('logar'))
        
        lista = Musica.query.order_by(Musica.id_musica)

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

        musica = Musica.query.filter_by(nome_musica = nome).first()

        if musica:
                flash('Musica ja Cadastrada')
                return redirect(url_for('listarMusicas'))
        nova_musica = Musica(nome_musica =  nome, cantor_banda = cantorBanda, genero_musica =  genero)
        db.session.add(nova_musica)
        db.session.commit()
        return redirect(url_for('listarMusicas'))


@app.route("/editar")
def editar():
        if 'usuario_logado' not in session or session['usuari_logado'] == None:
                 return redirect(url_for('logar'))
        
        return  render_template("editar_musica.html", titulo = "Editar Musica")


@app.route("/atualizar")
def atualizar():
        pass
@app.route('/login')
def logar():
        return render_template('login.html')


@app.route('/autenticar',  methods=['POST' , ])
def  autenticar():
        usuario = Usuario.query.filter_by(login_usuario = request.form['txtLogin']).first()
        if usuario:
                if request.form['txtSenha'] == usuario.senha_usuario:
                        session['usuario_logado'] = request.form['txtLogin']
                        flash("Olá, " +  session['usuario_logado'])

                        return redirect(url_for("listarMusicas"))
                else:
                        flash('Senha invalida!')
                        return redirect(url_for('logar'))
        else:
                flash("Usuario ou Senha Invalida!")
                return redirect(url_for('logar'))

@app.route('/sair')
def sair():
        session['usuario_logado'] = None
        return redirect('/login')