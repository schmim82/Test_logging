import pandas as pd

def csv_reader(csv):
    return pd.read_csv(csv, sep= ";")

Rezepte_dataframe = csv_reader("test")

st.markdown(Rezepte_dataframe)
