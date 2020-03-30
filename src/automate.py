#from graphicalInterface import Interface
from generation import generation
from graphicalInterface import Interface
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

	if tableau[(i+1) % width][j] == 1:
		nbVoisin += 1

	if tableau[(i+1) % width][(j-1) % height] == 1:
		nbVoisin += 1

	if tableau[(i+1) % width][(j+1) % height] == 1:
		nbVoisin += 1

	if tableau[(i-1) % width][j] == 1:
		nbVoisin += 1

	if tableau[(i-1) % width][(j-1) % height] == 1:
		nbVoisin += 1

	if tableau[(i-1) % width][(j+1) % height] == 1:
		nbVoisin += 1

	if tableau[i][(j+1) % height] == 1:
		nbVoisin += 1

	if tableau[i][(j-1) % height] == 1:
		nbVoisin += 1

	return nbVoisin

#Fonction d'affichage terminal && debuggage
def affichDebug(tableau, width, height, nbCellulesVivantes, nbTour):
	os.system('clear')
	for i in range(width):
		for j in range(height):
			if tableau[j][i]: print('$', end =' ')
			else: print('.', end =' ')
		print(end = '\n')
	print("Nombre de Cellules Vivantes: ",nbCellulesVivantes)
	print("Nombre de tours: ",nbTour)

	time.sleep(0.09)

#Fonction qui passe un tour
def passLap(tableau, width, height, nbCellulesVivantes, nbTour):
	tabCol = []
	cellule = 0 
	newCellule = 0
	nbCellulesVivantes = 0

	for i in range(width):
		tabRow = []
		for j in range(height):
			cellule = tableau[i][j]
			newCellule = regle(cellule, i, j, width, height, tableau)
			tabRow.append(newCellule)
			if newCellule: nbCellulesVivantes += 1
		tabCol.append(tabRow)
	tableau = tabCol
	del tabRow, tabCol, cellule, newCellule
	return tableau, nbCellulesVivantes, nbTour + 1

#Fonction principal
def jeuDeLaVie(mode):

	#Initialisation des valeurs
	width = 20
	height = 20
	nbCellulesVivantes = 0
	nbTour = 0

	#Initialisation du tableau
	tableau = [[0] * height for j in range(width)]
	
	#Remplissage du tableau aléatoire
	tableau = generation(tableau, 'Aleatoire', width, height)

	#Initialisation du mode graphique
	if mode:
		gui = Interface(tableau, width, height)
	else:
		while True:
			tableau, nbCellulesVivantes, nbTour = passLap(tableau, width, height, nbCellulesVivantes, nbTour)
			affichDebug(tableau, width, height, nbCellulesVivantes, nbTour)
