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
        st.image(image_path, caption=os.path.basename(image_path), use_column_width=True)

# Hauptfunktion zur Ausführung des Skripts
st.title("Bilder aus lokalem Ordner anzeigen")
display_images()
