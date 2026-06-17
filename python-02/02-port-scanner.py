import socket

target = input("Inserisci l'ip: ")
port_range = input("Range di porte per lo scan [70-200]: ")

port_low = int(port_range.split('-')[0])
port_high = int(port_range.split('-')[1])

print(f'Scansionando {target} da porta {port_low} a {port_high}')

for port in range(port_low, port_high + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if status == 0:
        print(f'{port} - OPEN')
    else:
        print(f'{port} - CLOSED')
    s.close()
