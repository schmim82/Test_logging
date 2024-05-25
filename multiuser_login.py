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

def display_images():
    """
    Diese Funktion zeigt die Bilder in Streamlit an.
    """
    image_list = get_image_list()
    for image_path in image_list:
        st.image(image_path, caption = os.basename(image_path), use_column_width=True, output_format='PNG')

# Bild, das angezeigt werden soll
bild = "pinkeblume.jpg"
# Liste der Bilder abrufen
bilder_liste = get_image_list()

# Überprüfen, ob das Bild in der Liste enthalten ist, und dann anzeigen
if bild in [os.path.basename(img) for img in bilder_liste]:
    st.title("Bild aus lokalem Ordner anzeigen")
    st.image(os.path.join('images', bild), caption=bild, use_column_width=True, output_format='PNG')
else:
    st.error(f"Das Bild '{bild}' wurde nicht in der Bildliste gefunden.")
