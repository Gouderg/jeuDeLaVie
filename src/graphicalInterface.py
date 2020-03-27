from tkinter import *

class Interface:

	nbGeneration = 0
	nbCelluleVivante = 0

	def __init__(self, tableau, width, height):
		#Création de la fenêtre	
		self.root = Tk()
		self.root.title("Quadrillage")

		#Déclaration et Initialisation des valeurs du tableau
		self.size = 6					  		#Taille d'une cellule
		self.can_width = width * self.size		#Largeur du tableau
		self.can_height = height * self.size 	#Hauteur du tableau

		#Couleur pour la génération des cellules
		self.color = {0: "white", 1: "black"}
		self.id_can = 0

		#Création du cadre
		self.can = Canvas(self.root, height = can_height, width = can_width)
		self.can.pack()

		#Texte informatif
		self.textGeneration = Label(self.root)
		self.textGeneration.pack()
		self.textVivant = Label(self.root)
		self.textVivant.pack()

		#Boutton pour lancer le jeu
		Button(self.root, text = "Lancer le jeu", command = )

		self.state = StringVar()
		for item in ['Aleatoire', 'Stable', 'Oscillateur', 'Canon', 'Vaisseaux']:
			rb = Radiobutton(self.root, text = item, value = item, variable = self.state)
			rb.pack(side = LEFT)

		Button(self.root, text = 'Quitter',
               command =self.root.quit).pack()

		Button(self.root, text = 'Reset',
				command = self.reset).pack(side = RIGHT)

		self.affichage()		
	
	#Affichage du tableau
	def affichage(self, tableau, width, height, nbGeneration, nbCelluleVivante):
		self.can.delete('all')
		for i in range(width):
			for j in range(height):
				self.can.create_rectangle(i * self.size,
										  j * self.size,
										  (i + 1) * self.size,
										  (j + 1) * self.size,
										  fill = self.color[tableau[i][j]],
										  width = 1)
		self.textGeneration.configure(text = 'Génération: ' + str(self.nbGeneration))
		self.textVivant.configure(text = 'Cellules vivantes: '+str(self.nbCelluleVivante))

	