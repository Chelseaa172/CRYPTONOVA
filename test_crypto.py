from crypto.encryption import generate_key, encrypt_text, decrypt_text

key = generate_key()

pesan = "Halo, ini pesan rahasia CRYPTONOVA!"

hasil_enkripsi = encrypt_text(pesan, key)
hasil_dekripsi = decrypt_text(hasil_enkripsi, key)

print("KUNCI:", key)
print("PESAN ASLI:", pesan)
print("HASIL ENKRIPSI:", hasil_enkripsi)
print("HASIL DEKRIPSI:", hasil_dekripsi)

print("\n=== UJI KEAMANAN ===")

wrong_key = generate_key()

try:
    decrypt_text(hasil_enkripsi, wrong_key)
    print("Peringatan: Dekripsi berhasil dengan kunci salah!")
except Exception:
    print("BERHASIL: Kunci salah ditolak!")