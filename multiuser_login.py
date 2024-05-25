
import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd
import os



def bild_anzeigen(bild):

  try:
    st.image(bild, use_column_width = True)

  except FileNotFoundError:
    st.error(f"Die Bilddatei {bild} wurde nicht gefunden.")

  except Exception as e:
    st.error(f"Fehler beim Laden des Bildes: {e}")


bild = pinkeblume.pinkeblume.jpg

bild_anzeigen(bild)

