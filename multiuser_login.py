import streamlit as st
import pandas as pd
import requests
from base64 import b64encode

# GitHub Zugangsdaten
GITHUB_TOKEN = "your_github_token"
GITHUB_REPO = "username/reponame"
GITHUB_PATH = "path/to/your/file.csv"

def create_csv():
    # Beispiel-Datenframe erstellen
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    
    # CSV-Datei lokal speichern
    csv_data = df.to_csv(index=False)
    return csv_data

def upload_to_github(file_content):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{GITHUB_PATH}"
    
    # Base64-Kodierung der Datei
    encoded_content = b64encode(file_content.encode()).decode()
    
    # Überprüfen, ob die Datei bereits existiert
    response = requests.get(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    if response.status_code == 200:
        sha = response.json()['sha']
    else:
        sha = None
    
    # Datei hochladen
    payload = {
        "message": "Add CSV file",
        "content": encoded_content,
        "branch": "main"
    }
    if sha:
        payload["sha"] = sha
    
    response = requests.put(url, json=payload, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    
    if response.status_code == 201 or response.status_code == 200:
        st.success("CSV-Datei wurde erfolgreich zu GitHub hochgeladen!")
    else:
        st.error("Fehler beim Hochladen der CSV-Datei zu GitHub")

st.title("CSV-Datei zu GitHub hochladen")

if st.button('CSV-Datei erstellen und hochladen'):
    csv_data = create_csv()
    upload_to_github(csv_data)
