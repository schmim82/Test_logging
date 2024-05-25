import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd
import os

def get_image_path(image_name):
    # Erstellen des Pfads zum Bilderverzeichnis
    image_dir = os.path.join(os.path.dirname(__file__), "test_2", "bilder")
    return os.path.join(image_dir, image_name)

def bild_anzeigen(bild):
    try:
        st.image(bild, use_column_width=True)
    except FileNotFoundError:
        st.error(f"Die Bilddatei '{bild}' wurde nicht gefunden.")
    except Exception as e:
        st.error(f"Fehler beim Laden des Bildes: {e}")

# Verwende get_image_path, um den Pfad zum Bild zu erhalten
bild_pfad = get_image_path("pinkebluem.jpg")

# Debug-Ausgabe des generierten Pfads
st.write(f"Generated image path: {bild_pfad}")

# Überprüfen, ob die Datei existiert
if os.path.exists(bild_pfad):
    bild_anzeigen(bild_pfad)
else:
    st.error(f"Die Bilddatei '{bild_pfad}' wurde nicht gefunden.")
