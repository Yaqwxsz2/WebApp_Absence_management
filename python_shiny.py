from shiny import *
from shiny.ui import tags, h2
import numpy as np 
import matplotlib.pyplot as plt
import pathlib
import palmerpenguins
import pandas as pd
import re

penguins = palmerpenguins.load_penguins() #changer avec la base de données SQL

numerix_cols = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",]


app_ui = ui.page_fluid(
      
    ui.navset_tab(


        ui.nav('Login', h2('Login'),
        ui.input_text('y', 'Email', placeholder="Entrer l'adresse mail"),
    ui.input_password('x', 'Matricule', placeholder='Entrer le matricule'),
        ),
                
                ui.nav("Professeur", h2("Partie des professeurs"),
    ui.output_table('result'),
    ui.input_action_button('add', 'Créer une classe'),
    ui.input_action_button('delete', 'Supprimer la dernière classe créée')
    ),

                ui.nav('Profil', h2('Profil'),
                #Voir les informations personnelles + modifier ces informations.
                ui.output_text('nom'),
                ui.output_text('prenom'),
                ui.output_text('datenaissance'),
                ui.output_text('mail'),
                ui.output_text('ntel')
                ),
                id="inTabset",
            ),




)

def server(input, output, session):
    @output
    #Ajouter 
    
    @render.table
    def result():
        if re.match(r'^ad', input.y()):
            return penguins[(penguins['species'] == 'Adelie')] #utiliser start with
        elif re.match(r'^az', input.y()):
            return penguins[(penguins['species'] != 'Adelie')] 
        else :
            return penguins


            
    pp = penguins[(penguins['species'] == input.y())]

    @output
    @render.text
    def nom():
        return f"Nom : {pp[penguins['Nom']]}"

    @output
    @render.text
    def prenom():
        return f"Prénom : {pp[penguins['Prenom']]}"

    @output
    @render.text
    def datenaissance():
        return f"Date de naissance : {pp[penguins['Date_de_naissance']]}"

    @output
    @render.text
    def datenaissance():
        return f"Lieu de naissance : {pp[penguins['Lieu_de_naissance']]}"

    @output
    @render.text
    def mail():
        return f"Adresse mail : {pp[penguins['Email']]}"

    @output
    @render.text
    def ntel():
        return  f"Numéro de téléphone : {pp[penguins['Prenom']]}"


app = App(app_ui, server)
