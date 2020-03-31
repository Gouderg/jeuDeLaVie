from random import randint
import constante 

#Fonction générant des cas spécifiques
def generation(tableau, etat):
	if constante.WIDTH > 55 and constante.HEIGHT > 55 and etat != '' and etat != "Aleatoire":
		if etat == 'Oscillateur':
			#Galaxie de Kok
			tableau[20][20] = 1
			tableau[21][20] = 1
			tableau[22][20] = 1
			tableau[23][20] = 1
			tableau[24][20] = 1
			tableau[25][20] = 1
			tableau[20][21] = 1
			tableau[21][21] = 1
			tableau[22][21] = 1
			tableau[23][21] = 1
			tableau[24][21] = 1
			tableau[25][21] = 1

			tableau[27][20] = 1
			tableau[27][21] = 1
			tableau[27][22] = 1
			tableau[27][23] = 1
			tableau[27][24] = 1
			tableau[27][25] = 1
			tableau[28][20] = 1
			tableau[28][21] = 1
			tableau[28][22] = 1
			tableau[28][23] = 1
			tableau[28][24] = 1
			tableau[28][25] = 1

			tableau[23][27] = 1
			tableau[24][27] = 1
			tableau[25][27] = 1
			tableau[26][27] = 1
			tableau[27][27] = 1
			tableau[28][27] = 1
			tableau[23][28] = 1
			tableau[24][28] = 1
			tableau[25][28] = 1
			tableau[26][28] = 1
			tableau[27][28] = 1
			tableau[28][28] = 1

			tableau[20][23] = 1
			tableau[20][24] = 1
			tableau[20][25] = 1
			tableau[20][26] = 1
			tableau[20][27] = 1
			tableau[20][28] = 1
			tableau[21][23] = 1
			tableau[21][24] = 1
			tableau[21][25] = 1
			tableau[21][26] = 1
			tableau[21][27] = 1
			tableau[21][28] = 1

			#pentadecathlon, 15 périodes

			tableau[20][43] = 1
			tableau[21][43] = 1
			tableau[22][42] = 1
			tableau[22][44] = 1
			tableau[23][43] = 1
			tableau[24][43] = 1
			tableau[25][43] = 1
			tableau[26][43] = 1
			tableau[27][42] = 1
			tableau[27][44] = 1
			tableau[28][43] = 1
			tableau[29][43] = 1

		elif etat == 'Stable':
			#bloc
			tableau[26][26] = 1
			tableau[26][25] = 1
			tableau[25][26] = 1
			tableau[25][25] = 1
			#bateau
			tableau[16][16] = 1
			tableau[17][16] = 1
			tableau[16][17] = 1
			tableau[17][18] = 1
			tableau[18][17] = 1

			#ruche
			tableau[46][46] = 1
			tableau[45][47] = 1
			tableau[45][48] = 1
			tableau[46][49] = 1
			tableau[47][48] = 1
			tableau[47][47] = 1

			#Une structure de quarante cellules asymétriques
			tableau[16][46] = 1
			tableau[16][47] = 1
			tableau[17][47] = 1
			tableau[18][46] = 1
			tableau[19][46] = 1
			tableau[19][47] = 1
			tableau[20][45] = 1
			tableau[20][44] = 1
			tableau[21][46] = 1
			tableau[21][47] = 1

			tableau[21][48] = 1
			tableau[21][49] = 1
			tableau[23][49] = 1
			tableau[22][50] = 1
			tableau[23][50] = 1
			tableau[22][45] = 1
			tableau[23][45] = 1
			tableau[23][46] = 1
			tableau[25][46] = 1
			tableau[26][46] = 1

			tableau[25][45] = 1
			tableau[26][45] = 1
			tableau[21][43] = 1
			tableau[22][43] = 1
			tableau[23][43] = 1
			tableau[23][42] = 1
			tableau[23][41] = 1
			tableau[24][40] = 1
			tableau[25][40] = 1
			tableau[25][41] = 1

			tableau[25][42] = 1
			tableau[25][43] = 1
			tableau[26][43] = 1
			tableau[25][37] = 1
			tableau[26][37] = 1
			tableau[26][38] = 1
			tableau[26][39] = 1
			tableau[27][40] = 1
			tableau[28][40] = 1
			tableau[28][39] = 1

		elif etat == 'Canon':
			tableau[26][2] = 1
			tableau[24][3] = 1
			tableau[26][3] = 1
			tableau[14][4] = 1
			tableau[15][4] = 1
			tableau[22][4] = 1
			tableau[23][4] = 1
			tableau[36][4] = 1
			tableau[37][4] = 1
			tableau[13][5] = 1
			tableau[17][5] = 1
			tableau[22][5] = 1
			tableau[23][5] = 1
			tableau[36][5] = 1
			tableau[37][5] = 1
			tableau[2][6] = 1
			tableau[3][6] = 1
			tableau[12][6] = 1
			tableau[18][6] = 1
			tableau[22][6] = 1
			tableau[23][6] = 1
			tableau[2][7] = 1
			tableau[3][7] = 1
			tableau[12][7] = 1
			tableau[16][7] = 1
			tableau[18][7] = 1
			tableau[19][7] = 1
			tableau[24][7] = 1
			tableau[26][7] = 1
			tableau[12][8] = 1
			tableau[18][8] = 1
			tableau[26][8] = 1
			tableau[13][9] = 1
			tableau[17][9] = 1
			tableau[14][10] = 1
			tableau[15][10] = 1

		if etat == 'Vaisseaux':
			#1er vaisseau
			tableau[2][51] = 1
			tableau[3][51] = 1
			tableau[4][51] = 1
			tableau[4][52] = 1
			tableau[3][53] = 1

			#2eme vaisseau
			tableau[2][23] = 1
			tableau[2][25] = 1
			tableau[3][26] = 1
			tableau[4][26] = 1
			tableau[5][26] = 1
			tableau[6][26] = 1
			tableau[6][25] = 1
			tableau[6][24] = 1
			tableau[5][23] = 1

			#3eme vaisseau
			tableau[2][13] = 1
			tableau[2][15] = 1
			tableau[3][16] = 1
			tableau[4][16] = 1
			tableau[5][16] = 1
			tableau[6][16] = 1
			tableau[7][16] = 1
			tableau[8][16] = 1
			tableau[8][15] = 1
			tableau[8][14] = 1
			tableau[7][13] = 1
			tableau[5][12] = 1
			tableau[4][12] = 1
	#Génération aléatoire
	else:
		for i in range(constante.HEIGHT):
			for j in range(constante.WIDTH):
				tableau[i][j] = randint(0,1)

	return tableau
