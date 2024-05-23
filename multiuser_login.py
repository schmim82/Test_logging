st.set_page_config(page_title="test")
st.title("test")

st.sidebar.title("test")

# Initialisiere den Zustand, falls er noch nicht existiert
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = '1'  # Setze die Standardauswahl auf '1'

# Button, der den Zustand ändert
if st.sidebar.button("drücken"):
    st.session_state.selected_option = '2'

# Optionen für das Radio-Button
liste = ["1", "2"]

# Erstelle das Radio-Button mit der ausgewählten Option aus st.session_state
selected = st.sidebar.radio("test", liste, index=liste.index(st.session_state.selected_option))

# Zeige die aktuelle Auswahl an
st.write(f"Ausgewählte Option: {selected}")
