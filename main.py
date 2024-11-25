# -*- coding:utf-8 -*-

__projet__ = "Projet_Labo_3A"
__nom_fichier__ = "main"
__author__ = "Pierre Boutin"
__date__ = "octobre 2024"

import matplotlib.pyplot as plt
import mplstereonet as mpl
import numpy as np
import csv
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

couleurs_str = {
    '-1': 'gray',
    '0': 'red',         # Rouge
    '1': 'blue',        # Bleu
    '2': 'green',       # Vert
    '3': 'orange',      # Orange
    '4': 'purple',      # Violet
    '5': 'cyan',        # Cyan
    '6': 'magenta',     # Magenta
    '7': 'yellow',      # Jaune
    '8': 'black',       # Noir
}
couleurs = {
    -1: 'gray',
    0: 'red',         # Rouge
    1: 'blue',        # Bleu
    2: 'green',       # Vert
    3: 'orange',      # Orange
    4: 'purple',      # Violet
    5: 'cyan',        # Cyan
    6: 'magenta',     # Magenta
    7: 'yellow',      # Jaune
    8: 'black',       # Noir
}

# Ouvrir le fichier CSV en mode lecture
with open('Plans.csv', newline='') as fichier_csv:
    lecteur_csv = csv.reader(fichier_csv, delimiter=';')
    # Ignorer l'en-tête s'il existe
    next(lecteur_csv)
    # Parcourir les lignes et afficher la valeur de la n-ième colonne (par exemple, la 3ème colonne)
    azimut=[]
    pendage=[]
    for ligne in lecteur_csv:
        dip_orientation = float(ligne[10])
        dip= float(ligne[9])
        if (dip_orientation<=90):
            orientation=270+dip_orientation
        else:
            orientation=dip_orientation-90
        azimut.append(orientation)
        pendage.append(dip)

print(azimut)
print(pendage)
data = {
    'azimut': azimut,
    'pendage': pendage
}
df = pd.DataFrame(data)
print(df)
moyenne_azimut = df['azimut'].mean()
print(f"Moyenne des azimuts : {moyenne_azimut}")

scaler = StandardScaler()
data_scaled = scaler.fit_transform(df[['azimut', 'pendage']])

# DBSCAN clustering
db = DBSCAN(eps=0.2, min_samples=2)
#eps (epsilon) : C'est la distance maximale entre deux points pour qu'ils soient considérés comme dans le même voisinage.
#min_samples : C'est le nombre minimal de points requis pour former un cluster.
labels = db.fit_predict(data_scaled)

# Ajout des labels de cluster au DataFrame
df['famille'] = labels

print(df)

df_azimuts_par_famille = df.groupby('famille')['azimut'].apply(list).reset_index()
print(df_azimuts_par_famille)

familles_uniques = df['famille'].unique()

# Boucle pour afficher les azimuts selon chaque famille

fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

for famille in familles_uniques:
    azimuts = df[df['famille'] == famille]['azimut'].tolist()
    print(df[df['famille'] == famille]['azimut'].tolist())
    strikes= df[df['famille'] == famille]['azimut'].tolist()
    dips = df[df['famille'] == famille]['pendage'].tolist()
    ax.plane(strikes, dips, color = f"{couleurs[famille]}", linewidth=2)
    ax.pole(strikes, dips,'^',color='red', markersize=4)
ax.set_longitude_grid(10)
ax.set_longitude_grid_ends(75)
ax.grid(which='both', linestyle='dashed', color='gray', linewidth=0.5) # '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.show()