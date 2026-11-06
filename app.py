
from flask import Flask, render_template, request

from crypto.encryption import encrypt_text, decrypt_text, hash_md5,  verify_md5
from crypto.key_manager import KeyManager

app = Flask(__name__)

manager = KeyManager()

# Membuat kunci pertama saat aplikasi dijalankan
manager.create_key()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    key_id = None
    error = None

    if request.method == "POST":

        action = request.form.get("action")

        try:

            if action == "encrypt":

                plaintext = request.form.get("plaintext")

                key_id = manager.active_key_id
                key = manager.get_active_key()

                result = encrypt_text(plaintext, key)

            elif action == "decrypt":

                encrypted_text = request.form.get("encrypted_text")
                key_id = request.form.get("key_id")

                key = manager.get_key(key_id)

                result = decrypt_text(encrypted_text, key)

            elif action == "md5":
                plaintext = request.form.get("plaintext", "")
                print("TEKS YANG DITERIMA:", repr(plaintext))
                result = hash_md5(plaintext)

            elif action == "verify_md5":
                plaintext = request.form.get("plaintext", "")
                original_hash = request.form.get("original_hash", "")
                if verify_md5(plaintext, original_hash):
                    result = "Hash cocok! Teks sesuai."
                else:
                    result = "Hash tidak cocok!"

        except Exception:
            error = "Proses gagal. Periksa teks, Key ID, atau kunci yang digunakan."

    return render_template(
        "crypto.html",
        result=result,
        key_id=key_id,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)