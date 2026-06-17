import socket

SRV_ADDR = '0.0.0.0'
SRV_PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1) # cosa fa l'uno?

# print('Socket in ascolto alla porta ' + str(SRV_PORT))
print(f'Socket in ascolto alla porta {SRV_PORT}')

# result = s.accept()
# print(result)

connection, address = s.accept()

# risultato = ('ciao', 'pausaaaaaaa')
# connection = risultato[0]    # 'ciao'
# address = risultato[1]       # 'pausaaaaaaa'

print(f'Sei stato contattato da {address}')

while True:
    data = connection.recv(20)
    if data == b'\n': break
    print(data.decode('utf-8'))
    connection.sendall(b'Bucket ricevuto: ' + data)

connection.close()
s.close()
