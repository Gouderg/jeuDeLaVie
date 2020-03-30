from tkinter import *
from generation import generation
import automate
import constante

class Interface:
	
	nbTour = 0
	nbCellulesVivantes = 0

	def __init__(self, tableau):
		#Création de la fenêtre	
		self.root = Tk()
		self.root.title("Quadrillage")

		#Déclaration et Initialisation des valeurs du tableau
		self.tableau = tableau	 			    			#Tableau
		self.size = 6					  					#Taille d'une cellule
		self.can_width = constante.WIDTH * self.size		#Largeur du canva
		self.can_height = constante.HEIGHT * self.size 		#Hauteur du canva

		#Couleur pour la génération des cellules
		self.color = {0: "white", 1: "black"}
		self.id_can = 0

		#Création du cadre
		self.can = Canvas(self.root, width = self.can_width, height = self.can_height)
		self.can.pack()

		#Texte informatif
		self.textGeneration = Label(self.root)
		self.textGeneration.pack()
		self.textVivant = Label(self.root)
		self.textVivant.pack()

		#Création des différents modes
		self.state = StringVar()
		for item in ['Aleatoire', 'Stable', 'Oscillateur', 'Canon', 'Vaisseaux']:
			rb = Radiobutton(self.root, text = item, value = item, variable = self.state)
			rb.pack(side = LEFT)

		#Lancement du jeu avec une génération aléatoire
		Button(self.root, text = 'Lancer le jeu',
				command = self.passLapGui).pack(side = LEFT)

		#Quitte le jeu
		Button(self.root, text = 'Quitter',
               command =self.root.destroy).pack(side = RIGHT)

		#Recommence la partie avec une nouvelle génération
		Button(self.root, text = 'Reset',
				command = self.reset).pack(side = RIGHT)
		
		self.affichage()
		self.root.mainloop()

	#Reset la partie
	def reset(self):
		self.nbTour = 0
		self.can.after_cancel(self.id_can)
		self.id_can = None
		for i in range(constante.HEIGHT):
			for j in range(constante.WIDTH):
				self.tableau[i][j] = 0

		self.tableau = generation(self.tableau, self.state.get())
		self.affichage()
		self.id_can = self.can.after(100, self.passLapGui)

	#Affichage du tableau
	def affichage(self):
		self.can.delete('all')
		for i in range(constante.HEIGHT):
			for j in range(constante.WIDTH):
				self.can.create_rectangle(i * self.size,
										  j * self.size,
										  (i + 1) * self.size,
										  (j + 1) * self.size,
										  fill = self.color[self.tableau[j][i]],
										  width = 1)

		self.textGeneration.configure(text = 'Génération: ' + str(self.nbTour))
		self.textVivant.configure(text = 'Cellules vivantes: '+str(self.nbCellulesVivantes))

	#Passe un tour en mode graphique
	def passLapGui(self):
		tabCol = []
		cellule = 0 
		newCellule = 0
		self.nbCellulesVivantes = 0

		for i in range(constante.HEIGHT):
			tabRow = []
			for j in range(constante.WIDTH):
				cellule = self.tableau[i][j]
				newCellule = automate.regle(cellule, i, j, self.tableau)
				tabRow.append(newCellule)
				if newCellule: self.nbCellulesVivantes += 1
			tabCol.append(tabRow)
		self.tableau = tabCol
		self.nbTour += 1
		del tabRow, tabCol, cellule, newCellule
		self.affichage()
		self.id_can = self.can.after(10,self.passLapGui)
