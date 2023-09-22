from comunidadeimpressionadora import app, bcrypt

# teste -  tirar daqui
from comunidadeimpressionadora.models import Usuario

from comunidadeimpressionadora import database
import os
# teste - tirar até aqui


if __name__ == '__main__':
    app.run(debug=True)

# teste para criar o database
# with app.app_context():
#     database.drop_all()
#     database.create_all()

# Comando para verificar os usuarios no Banco de Dados

# Teste --> apagar depois
#os.system('cls')
with app.app_context():
    meus_usuarios = Usuario.query.all()
    if meus_usuarios=="": 
            print('Nenhum usuário cadastrado')
    c = 1
    for usuario in meus_usuarios:
        print("--> ", c)
        print(usuario)
        print(usuario.username)
        print(usuario.email)
        print(usuario.senha)
        print('---' * 15)
        c += 1
        
        
    
    
# with app.app_context():
#     database.drop_all()
#     database.create_all()
#     print('Usuarios apagados do Banco de Dados...')
    
    