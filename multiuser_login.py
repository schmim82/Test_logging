import streamlit as st
import pandas as pd
from github_contents import GithubContents

st.set_page_config(page_title="Test")

# Set constants
DATA_FILE = "other_data.csv"  # Dateiname für die andere Daten-CSV-Datei
DATA_COLUMNS = ['Column1', 'Column2', 'Column3']  # Spaltennamen für deine anderen Daten

def init_github():
    """Initialisiere das GithubContents-Objekt."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        print("GitHub initialisiert")

def init_data():
    """Initialisiere oder lade das DataFrame mit den anderen Daten."""
    if 'other_data_df' not in st.session_state:
        if st.session_state.github.file_exists(DATA_FILE):
            st.session_state.other_data_df = st.session_state.github.read_df(DATA_FILE)
        else:
            st.session_state.other_data_df = pd.DataFrame(columns=DATA_COLUMNS)

def main():
    init_github()
    init_data()

    if 'authentication' not in st.session_state:
        st.session_state['authentication'] = False

    if not st.session_state['authentication']:
        options = st.sidebar.selectbox("Select a page", ["Login", "Register"])
        if options == "Login":
            login_page()
        elif options == "Register":
            register_page()

    else:
        # Hier kannst du Code hinzufügen, der nach dem erfolgreichen Login ausgeführt wird
        st.markdown("Erfolgreich authentifiziert")

if __name__ == "__main__":
    main()
