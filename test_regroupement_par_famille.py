# -*- coding:utf-8 -*-

__projet__ = "Projet_Labo_3A"
__nom_fichier__ = "test_regroupement_par_famille"
__author__ = "mon_Prénom mon_Nom"
__date__ = "octobre 2024"

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import mplstereonet as mpl

couleurs = {
    0: 'red',         # Rouge
    1: 'blue',        # Bleu
    2: 'green',       # Vert
    3: 'orange',      # Orange
    4: 'purple',      # Violet
    5: 'cyan',        # Cyan
    6: 'magenta',     # Magenta
    7: 'yellow',      # Jaune
    8: 'black',       # Noir
    9: 'gray'         # Gris
}
couleurs_str = {
    '0': 'red',         # Rouge
    '1': 'blue',        # Bleu
    '2': 'green',       # Vert
    '3': 'orange',      # Orange
    '4': 'purple',      # Violet
    '5': 'cyan',        # Cyan
    '6': 'magenta',     # Magenta
    '7': 'yellow',      # Jaune
    '8': 'black',       # Noir
    '9': 'gray'         # Gris
}

data = {
    'azimut': [10, 20, 190, 200, 30, 210, 350, 355],
    'pendage': [45, 40, 50, 47, 42, 53, 60, 58],
    'famille': ['1', '1', '2', '2', '1', '2', '3', '3']
}
df = pd.DataFrame(data)

# Obtenir les familles uniques
familles_uniques = df['famille'].unique()

# Boucle pour afficher les azimuts selon chaque famille

fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

for famille in familles_uniques:
    azimuts = df[df['famille'] == famille]['azimut'].tolist()
    print(df[df['famille'] == famille]['azimut'].tolist())
    strikes= df[df['famille'] == famille]['azimut'].tolist()
    dips = df[df['famille'] == famille]['pendage'].tolist()
    ax.plane(strikes, dips, color = f"{couleurs_str[famille]}", linewidth=2)
    ax.pole(strikes, dips,'^',color='red', markersize=4)
ax.set_longitude_grid(10)
ax.set_longitude_grid_ends(75)
ax.grid(which='both', linestyle='dashed', color='gray', linewidth=0.5) # '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.show()