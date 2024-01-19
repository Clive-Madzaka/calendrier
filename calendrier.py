# --*-- Coding Utf-8 --*--
""" Ce programme permet d'afficher un calendrier annuel sur la base de l'année saisie par l'utilisateur """

from calendar import *
annee = int(input("Entrer l'année : "))
print(calendar(annee, 2, 1, 8, 3))

'''
    2: Largeur des colonnes dans le calendrier.
    1: Espacement entre les semaines dans le calendrier.
    8: Nombre de caractères de séparation entre les colonnes du calendrier.
    3: Nombre de mois à afficher à la fois.
'''
