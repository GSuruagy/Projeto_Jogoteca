SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'JiraiaDBA',
        senha = '123456',
        servidor = 'localhost',
        database = 'jogoteca'
    )