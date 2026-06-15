# --- Parcourir une liste avec une boucle FOR ---

# Notre inventaire complet
inventaire = ["Épée en fer", "Bouclier en bois", "Potion de soin", "Casque en or"]

print("⚔️ --- MODE COMBAT REQUIS --- ⚔️")
print("Tu ouvres ton sac pour inspecter ton équipement :")
print("-" * 40)

# La boucle FOR : 'objet' est une variable temporaire qui va recevoir
# le nom de chaque équipement, l'un après l'autre.
for objet in inventaire:
    print(f" 👉 [ÉQUIPÉ] : {objet}")

print("-" * 40)
print("Tout est prêt, tu peux aller affronter les monstres ! 🐉")
