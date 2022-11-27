
from shiny import *
from shiny.ui import tags, h2
import numpy as np 
import matplotlib.pyplot as plt
import pathlib
import palmerpenguins
import pandas as pd
import re
import sqlite3

con = sqlite3.connect('C:/Users/WilliamNOBLET/Downloads/BD.db')

df_admin = pd.read_sql_query('SELECT * FROM Administrateur', con)

df_prof = pd.read_sql_query('SELECT * FROM Professeur', con)

df_etu = pd.read_sql_query('SELECT * FROM Etudiant', con)

df_classe = pd.read_sql_query('SELECT * FROM SalleDeClasse', con)



app_ui = ui.page_fluid(
      
    ui.navset_tab(


        ui.nav('Login', h2('Login'),
        ui.input_text('y', 'Email', placeholder="Entrer l'adresse mail"),
    ui.input_password('x', 'Matricule', placeholder='Entrer le matricule'),
        ),
                
                ui.nav("Professeur", h2("Classes"),
    ui.output_table('result'),
    ui.input_action_button('add', 'Créer une classe'),
    ui.input_action_button('delete', 'Supprimer la dernière classe créée')
    ),

                ui.nav('Profil', h2('Profil'),
                #Voir les informations personnelles + modifier ces informations.
                ui.output_text('nom'),
                ui.output_text('prenom'),
                ui.output_text('datenaissance'),
                ui.output_text('mail')
                ),
                id="inTabset",
            ),




)

def server(input, output, session):

    nom_classe = df_classe.Nom.unique()


    @output
    #Ajouter 
    
    @render.table
    def result():
        if re.match(r'^ADM', input.y()):
            if df_admin.index(input.x()) == df_admin.index(input.y()):
                pp = df_admin[df_admin['Matricule'] == input.x()]
                for i in range(len(nom_classe)):
                    classe = df_classe[df_classe['Nom'] == nom_classe[i]]
                    classe_etu = classe[['Matricule_etudiant']]
                    classe_prof = classe[['Matricule_prof']]
                    return df_etu[df_etu['Matricule_etudiant'] == classe_etu['Matricule_etudiant']], df_prof[df_prof['Matricule_prof'] == classe_prof['Matricule_prof']]



        elif re.match(r'^PRF', input.y()):
            if df_prof.index(input.x()) == df_prof.index(input.y()):
                pp = df_prof[df_prof['Matricule'] == input.x()]
                classe_prof = df_classe[df_classe['Matricule_prof'] == input.x()]
                classe_prof = classe_prof[['Matricule_s']]


                for i in range(len(nom_classe))

                



        elif re.match(r'^ETU', input.y()):
            if df_etu.index(input.x()) == df_etu.index(input.y()):
                pp = df_etu[df_etu['Matricule'] == input.x()]
                return df_etu
        else:
            return('Error')
        
            
    @reactive.Effect 
    @reactive.event(input.add())
    def _():
        nom_classe = input("Nom de la classe:")
        matricule_professeur = input('Matricule du professeur:')
        matricule_eleve = input('Matricule de élève:')
        req = '''INSERT INTO SalleDeClasse (Nom, Matricule_prof, Matricule_etudiant)  
            VALUES ({}, {}, {})'''.format(nom_classe, matricule_professeur, matricule_eleve)

        con.execute(req)

  
    @reactive.Effect
    @reactive.event(input.delete())
    def _():
        nom_classe_d = input('Nom de la classe a supprimer:')
        req_delete = '''DELETE from SalleDeClasse where Nom = {};'''.format(nom_classe_d)
        con.execute(req_delete)

    @output
    @render.text
    def nom():
        return f"Nom :{pp['Nom']}"

    @output
    @render.text
    def prenom():
        return f"Prénom :{pp['Prenom']}"

    @output
    @render.text
    def datenaissance():
        return f"Lieu de naissance :{pp['Date_de_naissance']}"

    @output
    @render.text
    def mail():
        return f"Adresse mail :{pp['email']}"

   


app = App(app_ui, server)
