import socket

opciones = ["piedra", "papel", "tijera"]

def pedir_jugada():
    while True:
        jugada = input("Elegí piedra, papel o tijera: ").strip().lower()

        if jugada in opciones:
            return jugada

        print("Opción inválida. Escribí piedra, papel o tijera.")

servidor = socket.socket()

servidor.bind(("0.0.0.0", ?????)) #qué va acá?
servidor.listen(1)

print("Esperando rival...")

conexion, direccion = servidor.accept()

print("Se conectó:", direccion)

mi_jugada = pedir_jugada()

conexion.send(mi_jugada.encode())

jugada_rival = conexion.recv(1024).decode().strip().lower()

if jugada_rival not in opciones:
    print("El rival envió una jugada inválida:", jugada_rival)

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

conexion.close()
servidor.close()