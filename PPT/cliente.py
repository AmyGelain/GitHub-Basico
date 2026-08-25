import socket

opciones = ["piedra", "papel", "tijera"]

def pedir_jugada():
    while True:
        jugada = input("Elegí piedra, papel o tijera: ").strip().lower()

        if jugada in opciones:
            return jugada

        print("Opción inválida. Escribí piedra, papel o tijera.")

cliente = socket.socket()

ip = ___ # Qué va acá?

cliente.connect((ip, ????)) # y acá?

mi_jugada = pedir_jugada()

jugada_rival = cliente.recv(1024).decode().strip().lower()

cliente.send(mi_jugada.encode())

if jugada_rival not in opciones:
    print("El servidor envió una jugada inválida:", jugada_rival)

else:
    print("Vos:", mi_jugada)
    print("Rival:", jugada_rival)

    if mi_jugada == jugada_rival:
        print("EMPATE")

    elif (mi_jugada == "piedra" and jugada_rival == "tijera") or \
         (mi_jugada == "papel" and jugada_rival == "piedra") or \
         (mi_jugada == "tijera" and jugada_rival == "papel"):
        print("GANASTE")

    else:
        print("PERDISTE")

cliente.close()