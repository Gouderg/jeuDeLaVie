from tkinter import *
from random import *


class JeudeLaVie:

	nbGeneration = 0
	nbCelluleVivante = 0

	def __init__(self):

		self.root = Tk()
		self.root.title("Quadrillage")

		#Déclaration et Initialisation des valeurs du tableau
		self.tableau_width = 60    #Largeur
		self.tableau_height = 60    #Hauteur
		self.size = 6               #Taille d'une cellule
		self.can_width = self.tableau_width * self.size   #Largeur du canvas
		self.can_height = self.tableau_height * self.size #Hauteur du canvas

		self.color = {0: "white", 1: "black"}
		self.tableau = [[0 for i in range(self.tableau_height)] for j in range(self.tableau_width)]
		self.id_can = 0

		self.can = Canvas(self.root, height = self.can_height, width = self.can_width)
		self.can.pack()

		self.textGeneration = Label(self.root)
		self.textGeneration.pack()
		self.textVivant = Label(self.root)
		self.textVivant.pack()
		
		Button(self.root, text = 'Lancer le jeu',
				command = self.generation).pack()
		
		self.state = StringVar()
		for item in ['Aleatoire', 'Stable', 'Oscillateur', 'Canon', 'Vaisseaux']:
			rb = Radiobutton(self.root, text = item, value = item, variable = self.state)
			rb.pack(side = LEFT)

		Button(self.root, text = 'Quitter',
               command =self.root.quit).pack()

		Button(self.root, text = 'Reset',
				command = self.reset).pack(side = RIGHT)

		self.affichage()		

		self.root.mainloop()


	def generation(self):


		etat = self.state.get()
		
		if etat == '' or etat == 'Aleatoire':
			for i in range(self.tableau_width):
				for j in range(self.tableau_height):
					self.tableau[i][j] = randint(0,1)

		elif etat == 'Oscillateur' and self.tableau_width > 20 and self.tableau_height > 20:
			#Galaxie de Kok
			self.tableau[20][20] = 1
			self.tableau[21][20] = 1
			self.tableau[22][20] = 1
			self.tableau[23][20] = 1
			self.tableau[24][20] = 1
			self.tableau[25][20] = 1
			self.tableau[20][21] = 1
			self.tableau[21][21] = 1
			self.tableau[22][21] = 1
			self.tableau[23][21] = 1
			self.tableau[24][21] = 1
			self.tableau[25][21] = 1

			self.tableau[27][20] = 1
			self.tableau[27][21] = 1
			self.tableau[27][22] = 1
			self.tableau[27][23] = 1
			self.tableau[27][24] = 1
			self.tableau[27][25] = 1
			self.tableau[28][20] = 1
			self.tableau[28][21] = 1
			self.tableau[28][22] = 1
			self.tableau[28][23] = 1
			self.tableau[28][24] = 1
			self.tableau[28][25] = 1

			self.tableau[23][27] = 1
			self.tableau[24][27] = 1
			self.tableau[25][27] = 1
			self.tableau[26][27] = 1
			self.tableau[27][27] = 1
			self.tableau[28][27] = 1
			self.tableau[23][28] = 1
			self.tableau[24][28] = 1
			self.tableau[25][28] = 1
			self.tableau[26][28] = 1
			self.tableau[27][28] = 1
			self.tableau[28][28] = 1

			self.tableau[20][23] = 1
			self.tableau[20][24] = 1
			self.tableau[20][25] = 1
			self.tableau[20][26] = 1
			self.tableau[20][27] = 1
			self.tableau[20][28] = 1
			self.tableau[21][23] = 1
			self.tableau[21][24] = 1
			self.tableau[21][25] = 1
			self.tableau[21][26] = 1
			self.tableau[21][27] = 1
			self.tableau[21][28] = 1

			#pentadecathlon, 15 périodes

			self.tableau[20][43] = 1
			self.tableau[21][43] = 1
			self.tableau[22][42] = 1
			self.tableau[22][44] = 1
			self.tableau[23][43] = 1
			self.tableau[24][43] = 1
			self.tableau[25][43] = 1
			self.tableau[26][43] = 1
			self.tableau[27][42] = 1
			self.tableau[27][44] = 1
			self.tableau[28][43] = 1
			self.tableau[29][43] = 1





		elif etat == 'Stable':
			#bloc
			self.tableau[26][26] = 1
			self.tableau[26][25] = 1
			self.tableau[25][26] = 1
			self.tableau[25][25] = 1

			#bateau
			self.tableau[16][16] = 1
			self.tableau[17][16] = 1
			self.tableau[16][17] = 1
			self.tableau[17][18] = 1
			self.tableau[18][17] = 1

			#ruche
			self.tableau[46][46] = 1
			self.tableau[45][47] = 1
			self.tableau[45][48] = 1
			self.tableau[46][49] = 1
			self.tableau[47][48] = 1
			self.tableau[47][47] = 1

			#Une structure de quarante cellules asymétriques
			self.tableau[16][46] = 1
			self.tableau[16][47] = 1
			self.tableau[17][47] = 1
			self.tableau[18][46] = 1
			self.tableau[19][46] = 1
			self.tableau[19][47] = 1
			self.tableau[20][45] = 1
			self.tableau[20][44] = 1
			self.tableau[21][46] = 1
			self.tableau[21][47] = 1

			self.tableau[21][48] = 1
			self.tableau[21][49] = 1
			self.tableau[23][49] = 1
			self.tableau[22][50] = 1
			self.tableau[23][50] = 1
			self.tableau[22][45] = 1
			self.tableau[23][45] = 1
			self.tableau[23][46] = 1
			self.tableau[25][46] = 1
			self.tableau[26][46] = 1

			self.tableau[25][45] = 1
			self.tableau[26][45] = 1
			self.tableau[21][43] = 1
			self.tableau[22][43] = 1
			self.tableau[23][43] = 1
			self.tableau[23][42] = 1
			self.tableau[23][41] = 1
			self.tableau[24][40] = 1
			self.tableau[25][40] = 1
			self.tableau[25][41] = 1

			self.tableau[25][42] = 1
			self.tableau[25][43] = 1
			self.tableau[26][43] = 1
			self.tableau[25][37] = 1
			self.tableau[26][37] = 1
			self.tableau[26][38] = 1
			self.tableau[26][39] = 1
			self.tableau[27][40] = 1
			self.tableau[28][40] = 1
			self.tableau[28][39] = 1

		elif etat == 'Canon':

			self.tableau[26][2] = 1
			self.tableau[24][3] = 1
			self.tableau[26][3] = 1
			self.tableau[14][4] = 1
			self.tableau[15][4] = 1
			self.tableau[22][4] = 1
			self.tableau[23][4] = 1
			self.tableau[36][4] = 1
			self.tableau[37][4] = 1
			self.tableau[13][5] = 1
			self.tableau[17][5] = 1
			self.tableau[22][5] = 1
			self.tableau[23][5] = 1
			self.tableau[36][5] = 1
			self.tableau[37][5] = 1
			self.tableau[2][6] = 1
			self.tableau[3][6] = 1
			self.tableau[12][6] = 1
			self.tableau[18][6] = 1
			self.tableau[22][6] = 1
			self.tableau[23][6] = 1
			self.tableau[2][7] = 1
			self.tableau[3][7] = 1
			self.tableau[12][7] = 1
			self.tableau[16][7] = 1
			self.tableau[18][7] = 1
			self.tableau[19][7] = 1
			self.tableau[24][7] = 1
			self.tableau[26][7] = 1
			self.tableau[12][8] = 1
			self.tableau[18][8] = 1
			self.tableau[26][8] = 1
			self.tableau[13][9] = 1
			self.tableau[17][9] = 1
			self.tableau[14][10] = 1
			self.tableau[15][10] = 1

		if etat == 'Vaisseaux':

			#1er vaisseau
			self.tableau[2][51] = 1
			self.tableau[3][51] = 1
			self.tableau[4][51] = 1
			self.tableau[4][52] = 1
			self.tableau[3][53] = 1

			#2eme vaisseau
			self.tableau[2][23] = 1
			self.tableau[2][25] = 1
			self.tableau[3][26] = 1
			self.tableau[4][26] = 1
			self.tableau[5][26] = 1
			self.tableau[6][26] = 1
			self.tableau[6][25] = 1
			self.tableau[6][24] = 1
			self.tableau[5][23] = 1

			#3eme vaisseau
			self.tableau[2][13] = 1
			self.tableau[2][15] = 1
			self.tableau[3][16] = 1
			self.tableau[4][16] = 1
			self.tableau[5][16] = 1
			self.tableau[6][16] = 1
			self.tableau[7][16] = 1
			self.tableau[8][16] = 1
			self.tableau[8][15] = 1
			self.tableau[8][14] = 1
			self.tableau[7][13] = 1
			self.tableau[5][12] = 1
			self.tableau[4][12] = 1


		self.affichage()
		self.id_can = self.can.after(100,self.passLap)
	

	def passLap(self):

		tabTemp = []
		cellule = 0
		self.nbCelluleVivante = 0

		for i in range(self.tableau_width):
			tabTempRow = []
			for j in range(self.tableau_height):
				cellule = self.tableau[i][j]
				if self.tableau[i][j] == 1: self.nbCelluleVivante += 1
				tabTempRow.append(self.regle(cellule, i, j,))
			tabTemp.append(tabTempRow)

		self.nbGeneration += 1

		self.tableau = tabTemp
		del tabTemp
		del tabTempRow
		self.affichage()
		self.id_can = self.can.after(10,self.passLap)


	def affichage(self):
		
		self.can.delete('all')
		for i in range(self.tableau_width):
			for j in range(self.tableau_height):
				self.can.create_rectangle(i * self.size,
										 j * self.size, 
										 (i + 1) * self.size, 
									 	 (j + 1) * self.size,
										 fill = self.color[self.tableau[i][j]],
										 width = 1)
		self.textGeneration.configure(text='Génération: ' + str(self.nbGeneration))
		self.textVivant.configure(text='Cellules vivantes: ' + str(self.nbCelluleVivante))

	def checkNeighbours(self,i,j):

		nbVoisin = 0

		if (i + 1 < self.tableau_width) and self.tableau[i+1][j] == 1:
			nbVoisin += 1

		if ((i + 1 < self.tableau_width) and (j - 1 > -1)) and self.tableau[i+1][j-1] == 1:
			nbVoisin += 1

		if ((i + 1 < self.tableau_width) and (j + 1 < self.tableau_height)) and (self.tableau[i+1][j+1] == 1):
			nbVoisin += 1

		if (i - 1 > -1) and self.tableau[i-1][j] == 1:
			nbVoisin += 1

		if (i - 1 > -1) and (j - 1 > -1) and self.tableau[i-1][j-1] == 1:
			nbVoisin += 1

		if (i - 1 > -1) and (j + 1 < self.tableau_height) and self.tableau[i-1][j+1] == 1:
			nbVoisin += 1

		if (j + 1 < self.tableau_height) and self.tableau[i][j+1] == 1:
			nbVoisin += 1

		if (j - 1 > -1) and self.tableau[i][j-1] == 1:
			nbVoisin += 1

		return nbVoisin

	def regle(self,cellule, i, j):

		nbvoisine = self.checkNeighbours(i,j)

		if cellule == 0: #Cellule morte

			if nbvoisine == 3: return 1
			else: return 0

		else: #Cellule vivante

			if nbvoisine == 2 or nbvoisine == 3: return 1
			else: return 0


	def reset(self):

		self.nbGeneration = 0
		self.can.after_cancel(self.id_can)
		self.id_can = None
		for i in range(self.tableau_width):
			for j in range(self.tableau_height): 
				self.tableau[i][j] = 0

		self.affichage()
		self.id_can = self.can.after(100, self.generation)



if __name__ == '__main__':
	app = JeudeLaVie()

