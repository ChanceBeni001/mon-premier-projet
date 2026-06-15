# --- Découverte des Listes en Python ---

# 1. On crée une liste avec 3 objets de départ
inventaire = ["Épée en fer", "Bouclier en bois", "Potion de soin"]

print("🎒 Voici ton inventaire de départ :")
print(inventaire)

print("-" * 30)

# 2. On accède à un élément précis grâce à son numéro (index)
# Rappel : 0 = premier objet
premier_objet = inventaire[0]
print(f"⚔️ Ton premier objet (index 0) est : {premier_objet}")

print("-" * 30)

# 3. On ajoute un nouvel objet à la fin de la liste avec .append()
print("🎁 Tu trouves un trésor !")
inventaire.append("Casque en or")

print("🎒 Ton inventaire mis à jour :")
print(inventaire)

# 4. On compte le nombre d'objets dans la liste avec len()
nombre_objets = len(inventaire)
print(f"📊 Tu as actuellement {nombre_objets} objets sur toi.")
