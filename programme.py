import random

# L'ordinateur choisit un nombre secret entre 1 et 10
nombre_secret = random.randint(1, 10)
tentative = 0

print("🎯 BIENVENUE AU JEU DU NOMBRE SECRET ! 🎯")
print("Je viens de choisir un nombre entre 1 et 10. À toi de deviner !")

# La boucle : TANT QUE la tentative est différente du nombre secret
while tentative != nombre_secret:
    # On demande un nombre au joueur
    reponse = input("Propose un nombre : ")
    tentative = int(reponse)
    
    # On donne un indice
    if tentative < nombre_secret:
        print("C'est PLUS GRAND ! ⬆️")
    elif tentative > nombre_secret:
        print("C'est PLUS PETIT ! ⬇️")

# Si on sort de la boucle, c'est qu'on a trouvé !
print(f"🎉 BRAVO CHANCE ! Tu as trouvé, le nombre secret était bien {nombre_secret} !")
