# Fait par Antoine Patino Conde
# Le 30 septembre 2022
# TP2 : le jeu de devinette
import random
# Le code choisit un chiffre a l'aleatoire
number = random.randint(1, 99)
print(number)
nb_essais = 0
# Fonction pour inscrire votre première estimation
guess = int(input(" Inscrit un nombre entre 1 et 99: "))




while True :
    while number != guess:
     if guess < number: # Si votre estimation est inferieur au chiffre choisi,
        nb_essais = nb_essais + 1
        print(" le chiffre rentré est plus petit que le chiffre choisi")
        guess = int(input("Inscrit un nombre entre 1 et 99: "))
     elif guess > number:
        nb_essais = nb_essais + 1
        print(" le chiffre rentré est plus grand que le chiffre choisi")
        guess = int(input("Inscrit un nombre entre 1 et 99: "))
     else:
         nb_essais = nb_essais + 1
         print("Tu l'as devine")
         print ( f" Ca a pris {nb_essais} essais")

         play_again = str(input("Voulez-vous jouer encore? y/n ;"))
         if play_again == ("y") :
             continue
         else:
             break