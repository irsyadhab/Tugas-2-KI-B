import socket
from itertools import cycle

# Import atau copy semua kode DES dari algoritma Anda di sini
# Sesuaikan fungsi decrypt dan text_to_bin, bin_to_text sesuai algoritma Anda

KEY = [0, 1, 1, 0, 1, 0, 1, 0] * 8  # Kunci DES yang disepakati antara server dan client

# Server configuration
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("Server is listening on port 8080...")

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established.")

# Menerima data terenkripsi dalam blok dan mendekripsi
received_data = []
while True:
    encrypted_block = client_socket.recv(64)  # Terima blok 64-bit (8 karakter terenkripsi)
    if not encrypted_block:
        break
    # Konversi dari byte stream ke format biner
    encrypted_block = [int(bit) for bit in encrypted_block.decode('utf-8')]
    decrypted_block = decrypt(encrypted_block, KEY)
    received_data.extend(decrypted_block)

# Mengubah data biner ke string
decrypted_message = bin_to_text(received_data)
print("Pesan yang diterima dan didekripsi:", decrypted_message)

client_socket.close()
server_socket.close()
