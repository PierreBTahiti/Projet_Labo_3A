# -*- coding:utf-8 -*-

__projet__ = "Projet_Labo_3A"
__nom_fichier__ = "test_clustering"
__author__ = "mon_Prénom mon_Nom"
__date__ = "octobre 2024"

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import mplstereonet as mpl

# Exemple de jeu de données avec des orientations d'azimut et de pendage
data = {
    'azimut': [10, 20, 190, 200, 30, 210, 350, 355],
    'pendage': [45, 40, 50, 47, 42, 53, 60, 58]
}
df = pd.DataFrame(data)

# Prétraitement : Normalisation des données pour DBSCAN
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df[['azimut', 'pendage']])

# DBSCAN clustering
db = DBSCAN(eps=0.5, min_samples=2)  # Ajuste eps et min_samples selon les besoins
labels = db.fit_predict(data_scaled)

# Ajout des labels de cluster au DataFrame
df['famille'] = labels

print(df)
print(df['famille'])
print(df.iloc[:, 0])
print(df[['azimut']])

df_azimuts_par_famille = df.groupby('famille')['azimut'].apply(list).reset_index()
print(df_azimuts_par_famille)

# Obtenir les familles uniques
familles_uniques = df['famille'].unique()

# Boucle pour afficher les azimuts selon chaque famille
for famille in familles_uniques:
    azimuts = df[df['famille'] == famille]['azimut'].tolist()
    # Affichage d'une manière spéciale
    print(f"Azimuts pour {famille} : {', '.join(map(str, azimuts))}")

strikes = df.iloc[:, 0]
dips = df.iloc[:, 1]


fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

ax.plane(strikes, dips, linewidth=2)
ax.pole(strikes, dips,'^',color='red', markersize=4)
ax.set_longitude_grid(10)
ax.set_longitude_grid_ends(75)
ax.grid(which='both', linestyle='dashed', color='gray', linewidth=0.5) # '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

plt.show()