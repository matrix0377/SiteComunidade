from comunidadeimpressionadora import app

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
os.system('cls')
with app.app_context():
    meus_usuarios = Usuario.query.all()
    for usuario in meus_usuarios:
        print(usuario)
        print(usuario.username)
        print(usuario.email)
        print(usuario.senha)
        print('---' * 9)
    
# with app.app_context():
#     database.drop_all()
#     database.create_all()
    