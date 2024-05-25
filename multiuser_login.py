import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd
import os




def get_image_list():
    """
    Diese Funktion gibt eine Liste von Bilddateien aus dem lokalen 'images'-Ordner zurück.
    """
    image_dir = os.path.join(os.path.dirname(__file__), 'images')
    return [os.path.join(image_dir, img) for img in os.listdir(image_dir) if img.endswith(('png', 'jpg', 'jpeg', 'gif'))]



def bild_anzeigen(bild, bilder_liste):
# Bild, das angezeigt werden soll
    
# Liste der Bilder abrufen
    

# Überprüfen, ob das Bild in der Liste enthalten ist, und dann anzeigen
    if bild in [os.path.basename(img) for img in bilder_liste]:

        st.image(os.path.join('images', bild), use_column_width=True)
    else:
        st.error(f"Das Bild '{bild}' wurde nicht in der Bildliste gefunden.")



a = "pinkeblume.jpg"
b = get_image_list()

bild_anzeigen(a,b)



