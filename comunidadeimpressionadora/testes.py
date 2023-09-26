from comunidadeimpressionadora import app
from comunidadeimpressionadora.models import Usuario
from comunidadeimpressionadora import database
from comunidadeimpressionadora.models import Usuario, Post 
import os


os.system('cls')

# with app.app_context():
#     #database.drop_all()
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email="lira@gmail.com", senha="123456")
#     usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="123456")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     print('-------------------------')
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print('-------------------------')
#     segundo_usuario = meus_usuarios[1]
#     print('id: ', segundo_usuario.id)
#     print('username: ', segundo_usuario.username)
#     print('e-mail: ', segundo_usuario.email)
#     print()
#     print('....fim.......')
#     print()
    
    
# outra forma de pegar as informações
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(email='lira@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)
    
# outra forma
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post do Lira", corpo="Lira voando")
#     database.session.add(meu_post)
#     database.session.commit()
    
# with app.app_context():
#     post = Post.query.all()
#     print(post) 
    
# pegando o primeiro Post
# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)


# Deletando e criando o banco de dados novamente
# with app.app_context():
#     database.drop_all()
#     database.create_all()





os.system('cls')
with app.app_context():
    meus_usuarios = Usuario.query.all()
    for usuario in meus_usuarios:
        print(usuario)
        print(usuario.username)
        print(usuario.email)
        print(usuario.senha)
        print('---' * 9)
        
# -----------------------------------------

# Comandos para deletar e recriar o Banco de Dados
# with app.app_context():
#     database.drop_all()
#     database.create_all()

# # Comando para verificar os usuarios no Banco de Dados
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)


# ---------------------------------------
# Teste de usuários que deu certo no main.py
