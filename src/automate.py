#from graphicalInterface import Interface
from generation import generation
import os 
import time

#Règle du jeu de la vie
def regle(cellule, i, j, width, height, tableau):
	nbvoisine = checkNeighbours(tableau, i, j, width, height)

	if cellule == 0: #Cellule morte
		if nbvoisine == 3: return 1
		else: return 0

	else: #Cellule vivante
		if nbvoisine == 2 or nbvoisine == 3: return 1
		else: return 0

#Compare les voisins
def checkNeighbours(tableau, i, j, width, height):
	nbVoisin = 0

	if (i + 1 < width) and tableau[i+1][j] == 1:
		nbVoisin += 1

	if ((i + 1 < width) and (j - 1 > -1)) and tableau[i+1][j-1] == 1:
		nbVoisin += 1

	if ((i + 1 < width) and (j + 1 <height)) and (tableau[i+1][j+1] == 1):
		nbVoisin += 1

	if (i - 1 > -1) and tableau[i-1][j] == 1:
		nbVoisin += 1

	if (i - 1 > -1) and (j - 1 > -1) and tableau[i-1][j-1] == 1:
		nbVoisin += 1

	if (i - 1 > -1) and (j + 1 < height) and tableau[i-1][j+1] == 1:
		nbVoisin += 1

	if (j + 1 < height) and tableau[i][j+1] == 1:
		nbVoisin += 1

	if (j - 1 > -1) and tableau[i][j-1] == 1:
		nbVoisin += 1

	return nbVoisin

#Fonction d'affichage terminal && debuggage
def affichDebug(tableau, width, height):
	os.system('clear')
	for i in range(width):
		for j in range(height):
			print(tableau[j][i], end = ' ')
		print(end = '\n')
	time.sleep(0.2)

#Fonction qui passe un tour
def passLap(tableau, width, height):
	tabCol = []
	cellule = 0
	for i in range(width):
		tabRow = []
		for j in range(height):
			cellule = tableau[i][j]
			tabRow.append(regle(cellule, i, j, width, height, tableau))
		tabCol.append(tabRow)
	tableau = tabCol
	del tabRow, tabCol
	return tableau

#Fonction principal
def jeuDeLaVie(mode):

	#Initialisation des valeurs
	width = 20
	height = 20

	#Initialisation du tableau
	tableau = [[0] * height for j in range(width)]
	
	#Remplissage du tableau aléatoire
	tableau = generation(tableau, 'Aleatoire', width, height)

	
	while True:
		affichDebug(tableau, width, height)
		tableau = passLap(tableau, width, height)
		
	