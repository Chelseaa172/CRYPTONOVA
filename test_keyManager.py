from crypto.key_manager import KeyManager
from crypto.encryption import encrypt_text, decrypt_text

manager = KeyManager()

# Membuat kunci pertama
key1_id = manager.create_key()
old_key = manager.get_active_key()

# Mengenkripsi pesan menggunakan KEY-1
pesan = "Dokumen rahasia CRYPTONOVA"
ciphertext = encrypt_text(pesan, old_key)

print("Pesan berhasil dienkripsi dengan KEY-1")

# Melakukan rotasi kunci
old_id, new_id = manager.rotate_key()

print("Kunci lama:", old_id)
print("Kunci baru:", new_id)

old_key_from_manager = manager.get_key(old_id)
hasil = decrypt_text(ciphertext, old_key_from_manager)

print("Hasil dekripsi:", hasil)

# Memeriksa hasil
if hasil == pesan:
    print("BERHASIL: Data lama tetap bisa dibuka!")
else:
    print("GAGAL: Data tidak cocok!")