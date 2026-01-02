from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

hasher = PasswordHash((
        Argon2Hasher(),
))
