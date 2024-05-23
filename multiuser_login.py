import streamlit as st
import pandas as pd
from github_contents import GithubContents

st.set_page_config(page_title="test")

# Set constants
DATA_FILE = "test.csv"
DATA_COLUMNS = ['Name', 'Rezept', 'Anzahl']

def init_github():
    """Initialisiere das GithubContents-Objekt."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        print("GitHub initialisiert")

def init_credentials():
    """Initialisiere oder lade das DataFrame."""
    if 'df_users' not in st.session_state:
        if st.session_state.github.file_exists(DATA_FILE):
            st.session_state.df_users = st.session_state.github.read_df(DATA_FILE)
        else:
            st.session_state.df_users = pd.DataFrame(columns=DATA_COLUMNS)

def save_to_csv(dataframe):
    """Speichere das DataFrame in einer CSV-Datei."""
    st.session_state.github.write_df(DATA_FILE, dataframe, "updated CSV")

init_github() # Initialisiere das GithubContents-Objekt
init_credentials() # Lade die Anmeldeinformationen aus dem GitHub-Datenrepository
save_to_csv(st.session_state.df_users) # Speichere das DataFrame in der CSV-Datei
