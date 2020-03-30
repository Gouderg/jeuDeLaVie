#from graphicalInterface import Interface
from generation import generation
from graphicalInterface import Interface
import constante
import os 
import time

#Règle du jeu de la vie
def regle(cellule, i, j, tableau):
	nbvoisine = checkNeighbours(tableau, i, j)

	if cellule == 0: #Cellule morte
		if nbvoisine == 3: return 1
		else: return 0

	else: #Cellule vivante
		if nbvoisine == 2 or nbvoisine == 3: return 1
		else: return 0

#Compare les voisins
def checkNeighbours(tableau, i, j):
	nbVoisin = 0

	if tableau[(i+1) % constante.HEIGHT][j] == 1:
		nbVoisin += 1

	if tableau[(i+1) % constante.HEIGHT][(j-1) % constante.WIDTH] == 1:
		nbVoisin += 1

	if tableau[(i+1) % constante.HEIGHT][(j+1) % constante.WIDTH] == 1:
		nbVoisin += 1

	if tableau[(i-1) % constante.HEIGHT][j] == 1:
		nbVoisin += 1

	if tableau[(i-1) % constante.HEIGHT][(j-1) % constante.WIDTH] == 1:
		nbVoisin += 1

	if tableau[(i-1) % constante.HEIGHT][(j+1) % constante.WIDTH] == 1:
		nbVoisin += 1

	if tableau[i][(j+1) % constante.WIDTH] == 1:
		nbVoisin += 1

	if tableau[i][(j-1) % constante.WIDTH] == 1:
		nbVoisin += 1

	return nbVoisin

#Fonction d'affichage terminal && debuggage
def affichDebug(tableau, nbCellulesVivantes = 0, nbTour = 0):
	os.system('clear')
	for i in range(constante.HEIGHT):
		for j in range(constante.WIDTH):
			if tableau[i][j]: print('$', end =' ')
			else: print('.', end =' ')
		print(end = '\n')
	print("Nombre de Cellules Vivantes: ",nbCellulesVivantes)
	print("Nombre de tours: ",nbTour)

	time.sleep(0.09)

#Fonction qui passe un tour
def passLap(tableau, nbCellulesVivantes, nbTour):
	tabCol = []
	cellule = 0 
	newCellule = 0
	nbCellulesVivantes = 0

	for i in range(constante.HEIGHT):
		tabRow = []
		for j in range(constante.WIDTH):
			cellule = tableau[i][j]
			newCellule = regle(cellule, i, j, tableau)
			tabRow.append(newCellule)
			if newCellule: nbCellulesVivantes += 1
		tabCol.append(tabRow)
	tableau = tabCol
	del tabRow, tabCol, cellule, newCellule
	return tableau, nbCellulesVivantes, nbTour + 1

#Fonction principal
def jeuDeLaVie(mode):

	#Initialisation des valeurs
	nbCellulesVivantes = 0
	nbTour = 0
	
	#Initialisation du tableau
	tableau = [[0] * constante.WIDTH for j in range(constante.HEIGHT)]
	
	#Remplissage du tableau aléatoire
	tableau = generation(tableau, 'Aleatoire')

	#Initialisation du mode graphique
	if mode:
		gui = Interface(tableau)
	else:
		while True:
			tableau, nbCellulesVivantes, nbTour = passLap(tableau, nbCellulesVivantes, nbTour)
			affichDebug(tableau, nbCellulesVivantes, nbTour)
