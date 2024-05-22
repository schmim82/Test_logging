import pandas as pd



Rezepte_dataframe = pd.read_csv("test.csv", sep= ";")

st.markdown(Rezepte_dataframe)
