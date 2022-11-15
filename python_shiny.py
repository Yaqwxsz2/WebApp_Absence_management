from shiny import *
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
    ui.output_table('result'),
)

def server(input, output, session):
    @output
    #Ajouter 
    @render.table
    def result():
        return penguins

app = App(app_ui, server)