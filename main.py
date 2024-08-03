import pandas as pd
import matplotlib.pyplot as plt

#Étape 1 : Lire le fichier Excel dans un DataFrame pandas
chemin_fichier_excel = "calcul222.xlsx"
df = pd.read_excel(chemin_fichier_excel)

# Étape 2 : Préparer les données pour le graphique à barres empilées
# Nous voulons utiliser le nom comme index et les catégories comme colonnes
# Nous allons transposer le DataFrame pour avoir le bon format
df = df.set_index('nom')  # Assurez-vous de remplacer 'Nom' par le nom de votre colonne contenant les noms


# Étape 3 : Créer le graphique à barres empilées
plt.figure(figsize=(10, 6))

# Plot stacked bars
df.plot(kind='bar', stacked=True)

# Ajouter des labels et un titre
plt.xlabel('LLMs and KGs')
plt.ylabel('Number of appearance')

# Afficher le graphique
#plt.legend(title='LLMs and KGs', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.legend(title='Categories', loc='upper left', ncol=5, bbox_to_anchor=(0, -0.3), fontsize='small')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


