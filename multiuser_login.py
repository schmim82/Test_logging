import streamlit as st
import pandas as pd
import requests
from base64 import b64encode, b64decode

class GithubContents:
    def __init__(self, owner, repo, token):
        self.owner = owner
        self.repo = repo
        self.token = token

    def get_file_content(self, path):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{path}"
        response = requests.get(url, headers={'Authorization': f'token {self.token}'})
        if response.status_code == 200:
            file_content = response.json()
            decoded_content = b64decode(file_content['content']).decode('utf-8')
            return decoded_content, file_content['sha']
        else:
            return None, None

    def update_file_content(self, path, content, sha, message="Update file"):
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/contents/{path}"
        encoded_content = b64encode(content.encode()).decode()
        payload = {
            "message": message,
            "content": encoded_content,
            "sha": sha,
            "branch": "main"
        }
        response = requests.put(url, json=payload, headers={'Authorization': f'token {self.token}'})
        return response.status_code in [200, 201]

def init_github():
    """Initialize the GithubContents object."""
    if 'github' not in st.session_state:
        st.session_state.github = GithubContents(
            st.secrets["github"]["owner"],
            st.secrets["github"]["repo"],
            st.secrets["github"]["token"])
        st.success("GitHub initialized")

def create_csv():
    # Beispiel-Datenframe erstellen
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = pd.DataFrame(data)
    return df.to_csv(index=False)

def upload_to_github(content):
    path = st.secrets["github"]["path"]
    github = st.session_state.github
    existing_content, sha = github.get_file_content(path)
    if existing_content is not None:
        updated_content = existing_content + '\n' + content
        success = github.update_file_content(path, updated_content, sha)
    else:
        updated_content = content
        success = github.update_file_content(path, updated_content, sha)

    if success:
        st.success("CSV-Datei wurde erfolgreich zu GitHub hochgeladen!")
    else:
        st.error("Fehler beim Hochladen der CSV-Datei zu GitHub")

st.title("Daten in bestehende CSV-Datei hochladen")

if st.button('Daten in CSV-Datei speichern'):
    init_github()
    csv_data = create_csv()
