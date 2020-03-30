import sys 
sys.path.append('./src')
from automate import jeuDeLaVie

if __name__ == '__main__':
	while True:
		choice = input("0- Mode terminal, 1- Mode Graphique: ")
		if len(choice) == 1 and ord(choice) >= 48 and ord(choice) <= 49:
			jeuDeLaVie(int(choice))
		print("Mauvaise saisie")
