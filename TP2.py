# Fait par Antoine Patino Conde
# Le 30 septembre 2022
# TP2 : le jeu de devinette
import random
# Le code choisit un chiffre a l'aleatoire
number = random.randint(1, 99)
# Fonction pour inscrire votre première estimation
guess = int(input(" Inscrit un nombre entre 1 et 99: "))

while number != guess:
     if guess < number: # Si votre estimation est inferieur au chiffre choisi,
        print(" le chiffre rentré est plus petit que le chiffre choisi")
        guess = int(input("Inscrit un nombre entre 1 et 99: "))
    elif guess > number:
        print(" le chiffre rentré est plus grand que le chiffre choisi")
        guess = int(input("Inscrit un nombre entre 1 et 99: "))

print("Tu l'as devine")