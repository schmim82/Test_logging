import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd
import os




DATA_FILE_1 = "Favoriten.csv"
DATA_COLUMNS_1 = ['name', 'rezept']


def init_github_rez():
    """Initialisiere das GithubContents-Objekt."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        print("GitHub initialisiert")


def init_rez_f():
    """Initialisiere oder lade das DataFrame."""
    if 'df_favoriten' not in st.session_state:
        if st.session_state.github.file_exists(DATA_FILE_1):
            st.session_state.df_favoriten = st.session_state.github.read_df(DATA_FILE_1)
        else:
            st.session_state.df_favoriten = pd.DataFrame(columns=DATA_COLUMNS_1)

def save_to_csv_rez_f(dataframe):

    st.session_state.github.write_df(DATA_FILE_1, dataframe, "updated CSV")

def daten_hochladen_f(new_data_df):
    init_github_rez() # Initialisiere das GithubContents-Objekt
    init_rez_f() # Lade die informationen aus dem GitHub-Datenrepository

# DataFrame aktualisieren
    st.session_state.df_favoriten = pd.concat([st.session_state.df_favoriten, new_data_df], ignore_index=True)

# DataFrame in CSV-Datei speichern
    save_to_csv_rez_f(st.session_state.df_favoriten)


def show_dataframe_f():
    dataframe = st.session_state.df_favoriten
    
    return dataframe









def rezepte_hinzufügen_f(name, rezept):

    
    df = show_dataframe_f()
    df_kriterien = df[df["name"] == name]
   

    if rezept in df_kriterien["rezept"].values:
        st.markdown("schon vorhanden")

    else:
        new_data = {'name': [name], 'rezept': [rezept]}
        new_data_df = pd.DataFrame(new_data)

        daten_hochladen_f(new_data_df)


name = "test_3"
rezept = "test_3"

init_rez_f()

rezepte_hinzufügen_f(name, rezept)


