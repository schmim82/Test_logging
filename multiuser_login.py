import streamlit as st
import pandas as pd
from github_contents import GithubContents
import Zutaten_daten as zd

def einkaufsliste_erstellen(einkaufsliste, Kochbuch):
    leere_dic = {}
    leere_dic_2 = {}

    

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
        if isinstance(leere_dic[key], int) or isinstance(leere_dic[key], float):
            leere_dic_2[key] = leere_dic[key]

        else:
            words_2 = key.split()
            if words_2[0]  not in leere_dic_2:

                leere_dic_2[words_2[0] = ""



                
    for key in leere_dic_2:
        st.markdown(f"{key} -- {leere_dic_2[key]}")


liste = {"Goma Ae": 2,
        "Knoblauchbrot": 2,
        "Parmigiana": 2,
        "Gefüllte Tomaten mit Feta": 2,
        "Kichererbsenbällchen mit Aprikosen": 2}

einkaufsliste_erstellen(liste, zd.Kochbuch)




