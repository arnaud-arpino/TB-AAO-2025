import pandas as pd
import matplotlib.pyplot as plt

# Lire les fichiers CSV
df1 = pd.read_csv("ech_1.csv", delimiter=";")
df2 = pd.read_csv("ech_2.csv", delimiter=";")

# Extraire les données
force1 = df1['C_1_Force[kN]']
deplacement1 = df1['C_1_Deplacement[mm]']

force2 = df2['C_1_Force[kN]']
deplacement2 = df2['C_1_Deplacement[mm]']

# Trouver les valeurs maximales de force
max_force1 = round(force1.max(),2)
max_force2 = round(force2.max(),2)

# Créer le graphe
plt.plot(deplacement1, force1, label='Echantillon 1')
plt.plot(deplacement2, force2, label='Echantillon 2')

# Ajouter les valeurs maximales de force au graphe
plt.text(deplacement1.iloc[force1.idxmax()], max_force1, f'Max: {max_force1} kN', horizontalalignment='left', verticalalignment='bottom')
plt.text(deplacement2.iloc[force2.idxmax()], max_force2, f'Max: {max_force2} kN', horizontalalignment='left', verticalalignment='bottom')

# Ajouter des titres et légendes
#plt.title('Courbes de traction')
plt.xlabel('Déplacement [mm]')
plt.ylabel('Force [kN]')
plt.legend()
plt.grid()

# Enregistrer le graphe en fichier PDF
plt.savefig('graphe.pdf')

# Afficher le graphe
plt.show()
