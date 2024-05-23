import streamlit as st
import pandas as pd
from github_contents import GithubContents

st.set_page_config(page_title="test")

# Set constants
DATA_FILE = "test.csv"
DATA_COLUMNS = ['Name', 'Rezept', 'Anzahl']

def init_github_rez():
    """Initialisiere das GithubContents-Objekt."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        print("GitHub initialisiert")

def init_rez():
    """Initialisiere oder lade das DataFrame."""
    if 'df_liste' not in st.session_state:
        if st.session_state.github.file_exists(DATA_FILE):
            st.session_state.df_liste = st.session_state.github.read_df(DATA_FILE)
        else:
            st.session_state.df_liste = pd.DataFrame(columns=DATA_COLUMNS)
   

def save_to_csv_rez(dataframe):
    """Speichere das DataFrame in einer CSV-Datei."""
    st.session_state.github.write_df(DATA_FILE, dataframe, "updated CSV")


def daten_hochladen(new_data_df):
    init_github_rez() # Initialisiere das GithubContents-Objekt
    init_rez() # Lade die informationen aus dem GitHub-Datenrepository
# DataFrame aktualisieren
    st.session_state.df_liste = pd.concat([st.session_state.df_liste, new_data_df], ignore_index=True)

# DataFrame in CSV-Datei speichern
    save_to_csv_rez(st.session_state.df_liste)



def show_dataframe():
    dataframe = st.session_state.df_liste
    dataframe_eink_liste = dataframe.iloc[:, 3:]
    return dataframe_eink_liste
    

    st.markdown("""
    <style>
        .button-container {
            position: fixed;
            top: 10px;
            right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Erstelle einen Container für den Button
button_container = st.container()

# Füge den Button zum Container hinzu
with button_container:
    st.button("Button in oberer rechter Ecke")

# Füge Platzhalterinhalt hinzu, um den Abstand für den Button zu schaffen
st.text("Hauptinhalt der App")





new_data = {'name': ['test'], 'rezept': ['Neues Rezept'], 'anzahl': [20]}
new_data_df = pd.DataFrame(new_data)



