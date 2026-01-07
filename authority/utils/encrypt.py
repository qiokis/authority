from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

hasher = PasswordHash((
        Argon2Hasher(),
))

def get_password_hash(plain_password: str) -> str:
    return hasher.hash(plain_password)

def verify_password_hash(plain_password: str, password_hash: str) -> bool:
    return hasher.verify(plain_password, password_hash)
