# --- Mon programme qui prend des décisions ---

nom = input("Comment t'appelles-tu ? ")
print(f"Salut {nom} !")

# On demande l'année de naissance
annee_texte = input("En quelle année es-tu né(e) ? (ex: 1980) : ")

# On transforme le texte en vrai nombre pour faire un calcul mathématique
annee_naissance = int(annee_texte)
age = 2026 - annee_naissance

print(f"Tu as donc {age} ans.")

# --- LE CERVEAU DU PROGRAMME (La condition) ---
if age >= 40:
    print("La quarantaine passée... C'est l'âge de la sagesse et de l'expertise ! 🧠")
else:
    print("La jeunesse est avec toi ! Prêt à conquérir le monde du code ? 🚀")

print("Fin du programme, merci d'avoir joué !")
