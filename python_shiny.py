from shiny import *
from shiny.ui import tags, h2
import numpy as np 
import matplotlib.pyplot as plt
import pathlib
import palmerpenguins
import pandas as pd

penguins = palmerpenguins.load_penguins() #changer avec la base de données SQL

numerix_cols = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",]


app_ui = ui.page_fluid(
    ui.navset_tab(
        ui.nav('Login', h2('Login'),
        ui.input_text('y', 'Numero', placeholder='Entrer le numero'),
    ui.input_password('x', 'Password input', placeholder='Entrer les mots de passes'),
        ),
                
                ui.nav("Professeur", h2("Partie des professeurs"),
    ui.output_table('result'),
    ),

                ui.nav("Classe", h2("Partie des classes")),
                ui.nav("Elève", h2("Partie des élèves")),
                ui.nav('Profil', h2('Profil'),
                #Voir les informations personnelles + modifier ces informations.
                ),
                id="inTabset",
            ),




)

def server(input, output, session):
    @output
    #Ajouter 
    
    @render.table
    def result():
        return penguins

app = App(app_ui, server)
