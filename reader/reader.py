import telnetlib

try:
    # Informations de connexion Telnet
    host = "127.4.0.1"  # Remplacez par l'IP de votre capteur
    port = 14150  # Port Telnet (par défaut 14150)
    username = "user"  # Nom d'utilisateur pour la connexion Telnet
    password = "password"  # Mot de passe pour la connexion Telnet

    # Commande pour lire les tags RFID
    command = "READ_TAG"

    # Connexion Telnet
    tn = telnetlib.Telnet(host, port)

    # Se connecter au capteur avec un nom d'utilisateur et un mot de passe
    tn.read_until(b"login: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    while True:
        # Exécuter la commande pour lire les tags RFID
        tn.read_until(b"Command: ")
        tn.write(command.encode('ascii') + b"\n")

        # Lire la sortie du capteur (les données des tags RFID)
        #output = tn.read_all().decode('ascii')
        output = tn.read_until(b"\n").decode('ascii')

        # Afficher la sortie (les tags RFID détectés)
        print("Data from RFID reader:")
        print(output)

    # Fermer la connexion Telnet
    tn.close()
    
except Exception as e:
    print(f"Erreur lors de la connexion ou de l'exécution de la commande : {e}")