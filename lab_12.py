# ==========================================
# Lab 12 - Statistiques rapides et analyse d'un mini-dataset
# Auteur : Imane Bounouala
# ==========================================
import numpy as np

# ==========================================
# Étape 1 - Mise en place du dataset
# ==========================================
noms = np.array(["Alice", "Bob", "Chloé", "David"])
notes = np.array([
    [14.5, 16.0, 13.0],   # Alice
    [11.0, 10.5, 12.5],   # Bob
    [17.0, 18.5, 16.5],   # Chloé
    [9.0, 11.0, 10.0]     # David
])

print("Étudiants :", noms)
print("Notes :\n", notes)
print("Shape notes :", notes.shape)   # (4, 3)

# ==========================================
# Étape 2 - Statistiques globales
# ==========================================
moyenne_globale = np.mean(notes)
min_global = np.min(notes)
max_global = np.max(notes)
somme_globale = np.sum(notes)
ecart_type_global = np.std(notes)

print(f"Moyenne générale : {moyenne_globale:.2f}")
print(f"Minimum global : {min_global}")
print(f"Maximum global : {max_global}")
print(f"Somme globale : {somme_globale}")
print(f"Écart-type global : {ecart_type_global:.2f}")

# ====
