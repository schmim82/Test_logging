
import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd
import os

def get_image_path(image_name):
  image_dir = os.path.join(os.path.dirname(__file__), "../images")
  return os.path.join(image_dir, image_name)

                      
def bild_anzeigen(bild):

  try:
    st.image(bild, use_column_width = True)

  except FileNotFoundError:
    st.error(f"Die Bilddatei {bild} wurde nicht gefunden.")

  except Exception as e:
    st.error(f"Fehler beim Laden des Bildes: {e}")


bild_pfad = get_image_path("pinkebluem.jpg")

bild_anzeigen(bild_pfad)

