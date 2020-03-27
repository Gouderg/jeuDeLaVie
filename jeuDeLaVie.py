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

	

	


	#Reset le tableau
	def reset(self, nbGeneration, width, height):
		nbGeneration = 0
		self.can.after_cancel(self.id_can)
		self.id_can = None
		for i in range(tableau_width):
			for j in range(tableau_height): 
				self.tableau[i][j] = 0

		self.affichage()
		self.id_can = self.can.after(100, self.generation)

if __name__ == '__main__':
	app = JeudeLaVie()

