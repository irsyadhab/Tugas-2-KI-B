import socket
from itertools import cycle

# Import atau copy semua kode DES dari algoritma Anda di sini
# Sesuaikan fungsi encrypt dan text_to_bin, bin_to_text sesuai algoritma Anda

KEY = [0, 1, 1, 0, 1, 0, 1, 0] * 8  # Kunci DES yang disepakati antara server dan client

# Client configuration
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Input pesan
plaintext = input("Masukkan pesan yang akan dienkripsi dan dikirim: ")
binary_message = text_to_bin(plaintext)

# Membagi pesan menjadi blok-blok 64-bit (8 karakter)
blocks = [binary_message[i:i+64] for i in range(0, len(binary_message), 64)]

# Enkripsi setiap blok dan kirimkan ke server
for block in blocks:
    if len(block) < 64:
        block += [0] * (64 - len(block))  # Padding jika kurang dari 64 bit
    encrypted_block = encrypt(block, KEY)
    # Mengubah blok terenkripsi menjadi format byte stream
    encrypted_str = ''.join(str(bit) for bit in encrypted_block)
    client_socket.send(encrypted_str.encode('utf-8'))

client_socket.close()
