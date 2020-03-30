import sys 
sys.path.append('./src')
from automate import jeuDeLaVie

if __name__ == '__main__':

	print("\t\t-------------------------------------------------")
	print("\t\t|	Bonjour, voici mon jeu de la vie\t|", end = '\n\n')
	print("\t\t|0 - Mode terminal                   	\t|")
	print("\t\t|1 - Mode graphique avec Tkinter     	\t|")
	print("\t\t-------------------------------------------------")

	print(end ='\n\n')
	while True:
		choice = input("Votre choix: ")
		if len(choice) == 1 and ord(choice) >= 48 and ord(choice) <= 49:
			jeuDeLaVie(int(choice))
			break
		print("Mauvaise saisie")
