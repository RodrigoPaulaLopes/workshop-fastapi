
import bcrypt

# Função para criptografar a senha
def encrypt_password(password):
    # Gere um salt aleatório
    salt = bcrypt.gensalt()

    # Hash da senha usando o salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password