class Joueur:
  
    # La fonction get_colonne demande au joueur de saisir un nombre entre 0 et 6,
    # et réitère la demande tant que la valeur saisie n'est pas un entier dans cet intervale
    def get_colonne(self,joueur_courant):
        if joueur_courant==1:
            joueur='Kevin'
        else:
            joueur='Xavier'
        saisie_correct=False
        # gestion des erreurs et filtrage des entrées : demande une saisie jusqu'à ce que la valeur entrée soit un chiffre entre 0 et 6
        # Les messages d'erreurs orientant l'utilisateur sont affichés sur la sortie standard (sans provoquer d'erreur)
        while not saisie_correct:
            s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)
            # teste si la chaine saise est un entier :
            if not s_colonne.isdigit():
                print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
            # teste si la valeur numérique est comprise entre 0 et 6 :
            elif int(s_colonne)<0 or int(s_colonne)>6:
                print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
            else:
                saisie_correct=True
        # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
        return int(s_colonne)
           
    # La fonction jouer() demande au joueur courant dans quelle colonne (de 0 à 6) il veut jouer
    def jouer(self,joueur_courant, get_colonne,tab_colonne,grille):
        
        if joueur_courant==1:
            joueur='Kevin'
        else:
            joueur='Xavier'
        # La fonction get_colonne renvoie forcément un chiffre entre 0 et 6 :
        colonne=self.get_colonne(joueur_courant)
        while tab_colonne[colonne]==6:
            print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur))
            colonne=self.get_colonne(joueur_courant)
        grille[5-tab_colonne[colonne]][colonne]=joueur_courant
        tab_colonne[colonne]+=1
        print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur,colonne)) 
       

class JoueurIA(Joueur):
    def __init__(self, nom, jeton):
        super().__init__(nom, jeton)

    def jouer(self,grille):
        print("Joueur IA")     

class Grille:

   
    
    #permet d'initialiser la grille avec la valeur 0 dans chaque cellule.
    def init(self):
        #ligne = 6
        colonne = 7
        grille=[colonne*[0],colonne*[0], colonne*[0],colonne*[0], colonne*[0],colonne*[0]]
        return grille


    #permet d'afficher la grille avec le choix de chaque joueur
    # La fonction afficher() affiche la grille sur la sortie standard
    def afficher(self,grille):
        ligne = 6
        for i in range(ligne):
           # print("afficher grille")
            print(grille[i])

    # affiche le repère des colonnes sous la grille :
    print('\n 0  1  2  3  4  5  6')


    # La fonction grille_pleine() teste si la grille est pleine (aucun 0 dans la liste grille)
    def grille_pleine(self,grille):
        b_plein=True
        for i in range(6):
            for j in range(7):
                if grille[i][j]==0:
                    b_plein=False
        return b_plein


    # La fonction test_gagner() teste si 4 pions de même couleur sont alignés dans la grille
    def test_gagner(self,grille):
        trouve=0
        # teste 4 pions alignés horizontalement en analysant chacune des 6 lignes :
        for i in range(6):
            rouge=0
            bleu=0
            for j in range(7):
                if grille[i][j]==1:
                    rouge+=1
                    bleu=0
                    if rouge>=4:
                        trouve=1
                        return trouve
                elif grille[i][j]==2:
                    rouge=0
                    bleu+=1
                    if bleu>=4:
                        trouve=2
                        return trouve
                else:
                    rouge=0
                    bleu=0          
        # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
        for j in range(7):
            rouge=0
            bleu=0
            for i in range(6):
                if grille[i][j]==1:
                    rouge+=1
                    bleu=0
                    if rouge>=4:
                        trouve=1
                        return trouve
                elif grille[i][j]==2:
                    rouge=0
                    bleu+=1
                    if bleu>=4:
                        trouve=2
                        return trouve
                else:
                    rouge=0
                    bleu=0
        
        # test des 2 diagonales croissantes à 4 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(4):
            i=3-j
            k=i+2
            l=j+3
            # teste la première diagonale [i][j] :
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            # teste la seconde diagonale [k][l] :
            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # test des 2 diagonales croissantes à 5 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(5):
            i=4-j
            k=i+1
            l=j+2
            # teste la première diagonale [i][j] :
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            # teste la seconde diagonale [k][l] :
            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # test des 2 diagonales croissantes à 6 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(6):
            i=5-j
            k=i
            l=j+1
            # teste la première diagonale [i][j] :
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            # teste la seconde diagonale [k][l] :
            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # test des 2 diagonales décroissantes à 4 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(3,7):
            i=j-3
            k=j-1
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # test des 2 diagonales décroissantes à 5 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(2,7):
            i=j-2
            k=j-1
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # test des 2 diagonales décroissantes à 6 cases :
        rouge=[0,0]
        bleu=[0,0]

        for j in range(1,7):
            i=j-1
            k=i
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                bleu[0]=0
                if rouge[0]>=4:
                    trouve=1
                    return trouve
            elif grille[i][j]==2:
                rouge[0]=0
                bleu[0]+=1
                if bleu[0]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[0]=0
                bleu[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                bleu[1]=0
                if rouge[1]>=4:
                    trouve=1
                    return trouve
            elif grille[k][l]==2:
                rouge[1]=0
                bleu[1]+=1
                if bleu[1]>=4:
                    trouve=2
                    return trouve
            else:
                rouge[1]=0
                bleu[1]=0

        # si on n'a rien trouvé on retourne 0 :
        return trouve
 


    #permet de trouver la ligne disponible à partir d'une colonne. positionner(ligne, colonne, jeton):
    #permet de positionner un jeton dans la grille suivant la ligne et la colonne.
    def get_ligne(self,colonne):
        #si la colonne est pleine
         return -1

    def positionner(self,ligne,colonne,jeton):
        self.grille[ligne][colonne] = jeton                         




class Puissance4:

    def demmarer(self):
        print("Bienvenue dans le jeu Puissance4")
        
        joueur = Joueur()
        init_grille = Grille()
        # joueur_courant indique le prochain joueur qui doit jouer : 1 pour Kevin et 2 pour Xavier
        joueur_courant=1
        get_colonne = joueur.get_colonne(joueur_courant)
        colonne = 7
        # tab_colonne mémorise le nombre de pions dans chacune des colonnes
        tab_colonne = colonne*[0]
        grille = init_grille.init()


        # ############################################################################
        #    P R O G R A M M E      P R I N C I P A L
        # ############################################################################

        print('Le nom des joueurs sera ici Kevin et Xavier. Le joueur Kevin commence.')
        print('Début de la partie (la grille est vide) :')
        gagnant=0
        while not init_grille.grille_pleine(grille) and gagnant==0:
            init_grille.afficher(grille)
            joueur.jouer(joueur_courant,get_colonne,tab_colonne,grille)
            joueur_courant=3-joueur_courant
            gagnant = init_grille.test_gagner(grille)
            if gagnant==1:
                print('Bravo ! Le joueur Kevin a gagné !')
            elif gagnant==2:
                print('Bravo ! Le joueur Xavier a gagné !')


        init_grille.afficher(grille)
        if gagnant==0:
            print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
        elif init_grille.grille_pleine(grille):
            print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
        else:
            print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")

        # ############################################################################
        #    F I N     D U     P R O G R A M M E
        # ############################################################################


puissance4 = Puissance4()

puissance4.demmarer()