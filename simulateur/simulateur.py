import socket
import random
import time
from threading import Thread

# Fonction pour générer un tag RFID simulé
def generate_rfid_tag():
    return f"RFID_{random.randint(100000, 999999)}"

# Fonction pour gérer chaque connexion client
def handle_client(client_socket):
    try:
        # Attente de la connexion avec un client (simulateur d'un lecteur RFID)
        client_socket.send(b"login: ")
        client_socket.recv(1024)  # Attendre l'input de l'utilisateur (nom d'utilisateur)
        client_socket.send(b"Password: ")
        client_socket.recv(1024)  # Attendre le mot de passe
        
        while True:
            client_socket.send(b"Command: ")
            command = client_socket.recv(1024).decode('ascii').strip()
            
            if command == "READ_TAG":
                # Simuler la lecture d'un tag RFID
                rfid_tag = generate_rfid_tag()
                client_socket.send(f"RFID Tag Detected: {rfid_tag}\n".encode('ascii'))
                print(rfid_tag)
            else:
                client_socket.send(b"Unknown command\n")
            time.sleep(1)  # Attendre 1 seconde entre chaque réponse
    except Exception as e:
        print(f"Error in client handling: {e}")
    finally:
        client_socket.close()

# Fonction pour démarrer le serveur Telnet
def start_rfid_simulator(host='127.4.0.1', port=14150):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)


    while True:
        print(f"Simulateur RFID en écoute sur {host}:{port}...")
        # Accepter la connexion d'un client (comme le programme qui fait le telnet)
        client_socket, addr = server_socket.accept()
        print(f"Connexion acceptée de {addr}")
        
        # Lancer un thread pour gérer la connexion avec le client
        client_thread = Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    # Lancer le simulateur RFID sur 127.4.0.1, port 14150 (ou un autre port si nécessaire)
    start_rfid_simulator(host="127.4.0.1", port=14150)
