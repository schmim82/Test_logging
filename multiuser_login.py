import streamlit as st

# Definiere die Optionen für die Selectbox
options = ['1', '2', '3']

# Initialisiere den Zustand der Selectbox in st.session_state
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = '1'

# Funktion zum Aktualisieren der Selectbox
def set_selectbox_to_three():
    st.session_state.selected_option = '3'
    st.experimental_rerun()

# Erstelle die Selectbox in der Sidebar mit dem initialen Wert aus st.session_state
selected = st.sidebar.selectbox("Wähle eine Option", options, index=options.index(st.session_state.selected_option), key='selectbox')

# Button, der beim Drücken die Selectbox auf '3' setzt
if st.sidebar.button("Setze auf 3"):
    set_selectbox_to_three()

# Zeige die aktuelle Auswahl an
st.write(f"Ausgewählte Option: {selected}")
