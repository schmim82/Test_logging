import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd

def einkaufsliste_erstellen(einkaufsliste, Kochbuch):
    leere_dic = {}

    

    for key in einkaufsliste:
        dictionary = Kochbuch[key]

        anzahl = einkaufsliste[key]

        for key in dictionary:

            words = key.split()
        

            if words[0] != "Zubereitung":

                if key not in leere_dic:

                    if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):
                        leere_dic[key] = dictionary[key] * anzahl

                    else:
                        leere_dic[key] = dictionary[key]

                else:

                    if isinstance(dictionary[key], int) or isinstance(dictionary[key], float):
                        leere_dic[key] = leere_dic[key] + (dictionary[key] * anzahl)

    for key in leere_dic:
        st.markdown(f"{key} -- {leere_dic[key]}")

liste = {"Goma Ae: 2,
        "Knoblauchbrot": 2,
        "Parmigiana": 2,
        "Gefüllte Tomaten mit Feta": 2,
        "Kichererbsenbällchen mit Aprikosen": 2}

einkaufsliste_erstellen(liste, zd.Kochbuch)




