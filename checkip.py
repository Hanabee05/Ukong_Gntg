import socket

# Input dari pengguna
hostname = input('Enter a domain name: ')
# Mendapatkan alamat IP dari hostname
ip_address = socket.gethostbyname(hostname)

# Menampilkan hasil
print(f'Domain Name: {hostname}')
print(f'IP Address: {ip_address}')