import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_key():
    key = AESGCM.generate_key(bit_length=256)
    return base64.b64encode(key).decode("utf-8")


def encrypt_text(plaintext, key):
    key_bytes = base64.b64decode(key)

    aes = AESGCM(key_bytes)
    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None
    )

    result = nonce + ciphertext

    return base64.b64encode(result).decode("utf-8")


def decrypt_text(encrypted_text, key):
    key_bytes = base64.b64decode(key)
    data = base64.b64decode(encrypted_text)

    nonce = data[:12]
    ciphertext = data[12:]

    aes = AESGCM(key_bytes)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode("utf-8")