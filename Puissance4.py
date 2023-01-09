
from turtle import *
import os,random

# Dans le cadre du jeux enttre deux humains 
# Dans le cadre du jeux avec la machine le joueur BLEU est joué automatiquement par l'ordinateur : 
# le seul joueur humain est le joueur ROUGE 
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
    def jouer(self,joueur_courant,tab_colonne,grille):
        
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
       

class JoueurIA:
   
    
    #test_saisie  == get_colonne
    def get_colonne_Machine(self,grille,joueur_courant,tab_colonne,afficher_grille):
        #global grille,joueur_courant,tab_colonne
        if joueur_courant==1:
            joueur='ROUGE'
        else:
            joueur='BLEU'
            # le joueur 2 est remplacé par l'ordinateur qui renvoie ici un numéro de colonne entre 0 et 6

            # NIVEAU 1 : l'ordinateur recherche des pions rouges déjà alignés dans la grille

            # teste si 3 pions rouges sont alignés :
            prochain=self.jetons_rouges_alignes(grille,3)
            if prochain!=-1:
                if prochain<7:
                    if tab_colonne[prochain]<6:
                        return prochain
                else:
                    if tab_colonne[3]<6:
                        return 3

            # teste si 2 pions rouges sont alignés :
            if prochain!=-1:
                if prochain<7:
                    if tab_colonne[prochain]<6:
                        return prochain
                else:
                    if tab_colonne[4]<6:
                        return 4

            # NIVEAU 0 : l'ordinateur renvoie un numéro au hasard entre 0 et 6 en recherchant une colonne non pleine :
            n=random.randint(0,6)
            while tab_colonne[n]>=6:
                n=random.randint(0,6)
            return n

        saisie_correct=False
        # gestion des erreur et filtrage des entrées : demande une saisie jusqu'à ce que la valeur entrée soit un chiffre entre 0 et 6
        # Les messages d'erreurs orientant l'utilisateur sont affichés sur la sortie standard (sans provoquer d'erreur)
        while not saisie_correct:
            s_colonne=input("%s : entrez la colonne où jouer (de 0 à 6) :" % joueur)

            # commence par tester la saisie des commandes spéciales (f, s ou r) :
            if s_colonne.upper()=='F':
                # quitte le programme et ferme la fenêtre de la tortue si l'utilisateur saise f (comme fin)
                print("Fin du programme car l'utilisateur a saisie F")
                bye()
                exit()
            elif s_colonne.upper()=='S':
                # sauvegarde la sérialisation de la grille dans un fichier texte :
                fic=open('grille.txt','w')
                # convertit l'objet liste grile en chaine de caractères (sérialistation) :
                serialisation=str(grille)
                # enregistre la grille sur la première ligne du fichier grille.txt :
                fic.write(serialisation)
                fic.write('\n')
                # enregistre le joueur courant sur la deuxième ligne du fichier grille.txt :
                fic.write(str(joueur_courant))
                fic.close()
                print("\nL'état de la partie vient d'être enregistré dans le fichier grille.txt mais la partie continue.")
                print("C'est encore au joueur %s à jouer." % joueur)
            elif s_colonne.upper()=='R':
                if os.path.exists('grille.txt'):
                    # restaure la grille et le joueur courant à partir du fichier texte grille.txt :
                    fic=open('grille.txt','r')
                    # fic est un itérateur pointant sur les lignes du fichier : on le convertit en liste
                    ligne=list(fic)
                    fic.close()
                    # première ligne sans le \n : c'est la grille
                    s_grille=ligne[0].strip()
                    # deuxième ligne sans le \n : c'est le joueur courant
                    s_joueur_courant=ligne[1].strip()
                    # désérialisation des objets enregistrés en chaine de caractères :
                    grille=eval(s_grille)
                    joueur_courant=eval(s_joueur_courant)
                    # ré-initialise la grille graphique dans la fenêtre de la tortue :
                    reset()
                    speed(0)
                    hideturtle()
                    self.dessiner_grille()
                    # compte le nombre de pions dans chaque colonne et complète la grille graphique :
                    tab_colonne=7*[0]
                    for i in range(6):
                        for j in range(7):
                            if grille[i][j]!=0:
                                tab_colonne[j]+=1
                                self.dessiner_pion(j,5-i,grille[i][j])

                    print('\n\n\n\n\n\n=============================================')
                    print(' PUISSANCE 4 : FINIR UNE PARTIE')
                    print('=============================================')
                    if joueur_courant==1:
                        joueur='ROUGE'
                    else:
                        joueur='BLEU'
                    print("\nL'état de la partie vient d'être restaurée à partir du fichier grille.txt.")
                    print("C'est au joueur %s à jouer." % joueur)
                    afficher_grille()
                else:
                    print("\nLe fichier grille.txt n'existe pas.")
                    print("Avant de vouloir restaurer une partie avec la commande R il faut en sauvegarder une avec la commande S.")

            # teste si la chaine saise est un entier :
            elif not s_colonne.isdigit():
                print("Erreur de saise : la valeur entrée par le joueur %s n'est pas un nombre entier. Recommencez." % joueur)
            # teste si la valeur numérique est comprise entre 0 et 6 :
            elif int(s_colonne)<0 or int(s_colonne)>6:
                print("Erreur de saise : la valeur numérique entrée par le joueur %s n'est pas comprise entre 0 et 6. Recommencez." % joueur)
            else:
                saisie_correct=True
        # la chaine s_colonne est un chiffre entre 0 et 6 : on la convertit en entier et on la renvoie
        return int(s_colonne)    


   # La fonction jouer() demande au joueur courant dans quelle colonne (de 0 à 6) il veut jouer
    def jouer(self,grille,joueur_courant,tab_colonne,afficher_grille):
       # global joueur_courant
        joueur=["ROUGE","BLEU"]
        # La fonction tester_saisie renvoie forcément un chiffre entre 0 et 6 :
        colonne=self.get_colonne_Machine(grille,joueur_courant,tab_colonne,afficher_grille)
        while tab_colonne[colonne]==6:
            print('La colonne %d est pleine ! %s jouez dans une colonne non pleine' % (colonne,joueur[joueur_courant-1]))
            colonne=self.get_colonne_Machine(grille,joueur_courant,tab_colonne,afficher_grille)
        grille[5-tab_colonne[colonne]][colonne]=joueur_courant
        # dessine le pion sur la grille graphique :
        self.dessiner_pion(colonne,tab_colonne[colonne],joueur_courant)
        tab_colonne[colonne]+=1
        print('\nLe joueur %s vient de jouer dans la colonne %d :' % (joueur[joueur_courant-1],colonne))

    def dessiner_pion(self,x,y,couleur):
        # x de 0 à 6 et y de 0 à 5
        largeur=60
        x_base=-220
        y_base=-150
        up()
        goto(x_base+(x+1)*largeur-largeur//8,y_base+(y+1)*largeur-largeur//2)
        down()
        if couleur==1:
            # pion ROUGE si couleur=1 :
            color('red')
        else:
            # pion BLEU si couleur=2 :
            color('blue')
        begin_fill()
        circle(largeur/2.5)
        end_fill() 

    def jetons_rouges_alignes(self,grille,n):
        trouve=-1

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # teste 4 pions alignés horizontalement en alanysant chacune des 6 lignes :
        for i in range(6):
            rouge=0
            for j in range(7):
                if grille[i][j]==1:
                    rouge+=1
                    if rouge==n:
                        if i==5: # cas particulier de la première ligne
                            if j!=6 and grille[i][j+1]==0:
                                trouve=j+1
                                return trouve
                            elif j==6 and grille[i][j-n]==0:
                                trouve=j-n
                                return trouve
                        else: # une ligne haute
                            if j!=6 and grille[i][j+1]==0 and grille[i+1][j+1]!=0:
                                trouve=j+1
                                return trouve
                            elif j==6 and grille[i][j-n]==0 and grille[i+1][j-n]!=0:
                                trouve=j-n
                                return trouve

                else:
                    rouge=0

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # teste 4 pions alignés verticalement en alanysant chacune des 7 colonnes :
        for j in range(7):
            rouge=0
            for i in range(6):
                if grille[5-i][j]==1:
                    rouge+=1
                    if rouge==n and grille[4-i][j]==0:
                        trouve=j
                        return trouve
                else:
                    rouge=0

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # teste les 6 diagonales croissantes :

        # test des 2 diagonales croissantes à 4 cases :
        rouge=[0,0]

        for j in range(4):
            i=3-j
            k=i+2
            l=j+3
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # test des 2 diagonales croissantes à 5 cases :
        rouge=[0,0]

        for j in range(5):
            i=4-j
            k=i+1
            l=j+2
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # test des 2 diagonales croissantes à 6 cases :
        rouge=[0,0]

        for j in range(6):
            i=5-j
            k=i
            l=j+1
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i!=0 and grille[i-1][j+1]==0 and grille[i][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k!=0 and l!=6 and grille[k-1][l+1]==0 and grille[k][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # teste les 6 diagonales décroissantes :

        # test des 2 diagonales décroissantes à 4 cases :
        rouge=[0,0]

        for j in range(3,7):
            i=j-3
            k=j-1
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # test des 2 diagonales décroissantes à 5 cases :
        rouge=[0,0]

        for j in range(2,7):
            i=j-2
            k=j-1
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # test des 2 diagonales décroissantes à 6 cases :
        rouge=[0,0]

        for j in range(1,7):
            i=j-1
            k=i
            l=i
            if grille[i][j]==1:
                rouge[0]+=1
                if rouge[0]==n and i<=3 and j!=6 and grille[i+1][j+1]==0 and grille[i+2][j+1]!=0:
                    trouve=j+1
                    return trouve
            else:
                rouge[0]=0

            if grille[k][l]==1:
                rouge[1]+=1
                if rouge[1]==n and k<=3 and l!=6 and grille[k+1][l+1]==0 and grille[k+2][l+1]!=0:
                    trouve=l+1
                    return trouve
            else:
                rouge[1]=0

        # si on n'a rien trouvé on retourne -1 :
        return trouve      
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
        #ligne = 6
        #for i in range(ligne):
           # print("afficher grille")
           # print(grille[i])
        for row in grille:
            print("+---+---+---+---+---+---+---+") 

            line = []
            for item in row:
                if item == 1:
                    line.append("\u001B[31m" + "X" + "\u001B[0m")   
                elif item == 2:
                    line.append("\u001B[34m" + "O" + "\u001B[0m")
                else: 
                    line.append(" ")
            print("| " + " | ".join(line)+ " | ")
        print("+---+---+---+---+---+---+---+") 
        print()                  

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
 

    def positionner(self,ligne,colonne,jeton):
        self.grille[ligne][colonne] = jeton                         
    
    def dessiner_grille(self,x_base,y_base,largeur):
        up()
        goto(x_base,y_base)
        down()
        # traits horizontaux :
        for i in range(8):
            forward(7*largeur)
            up()
            goto(x_base,y_base+i*largeur)
            down()
        # traits verticaux :
        up()
        goto(x_base,y_base)
        setheading(90)
        down()
        for i in range(9):
            forward(6*largeur)
            up()
            goto(x_base+i*largeur,y_base)
            down()
        # affiche le numéro des colonnes sous la grille :
        for i in range(7):
            up()
            goto(x_base+i*largeur+largeur//2,y_base-largeur//2)
            down()
            write(str(i))

    # La fonction dessiner_pion(x,y,couleur) ajoute un pion dans la case (x,y)
    

class Puissance4:

    def jouer_avec_humain_ou_machine(self):
        str = ""
        print(" Bienvenue dans le jeu Puissance4 ")
        str = input("Desirez-vous jouer avec un humain(entrer humain) ou avec une machine(entrer machine) : ")
        if str == "humain":
           self. jeux_Humain_Humain()
        elif str == "machine": 
           self.jeux_humain_machine()   


    # La fonction qui_commence_entre_hummain_et_machine() demande à l'utilisateur le joueur qui commence (ROUGE ou BLEU)
    def qui_commence_entre_hummain_et_machine(self):
        global joueur_courant
        s=""
        while not s in ["1","2"]:
            s=input("Quel joueur commence ? Entrez 1 pour ROUGE ou 2 pour BLEU :")
        joueur_courant=int(s)  
        return joueur_courant

    def jeux_humain_machine(self):
              
        joueurIA = JoueurIA()
        init_grille = Grille()
        colonne = 7
        # tab_colonne mémorise le nombre de pions dans chacune des colonnes
        tab_colonne = colonne*[0]
        grille = init_grille.init()
        n = 3
        # initialise l'affichage graphique de la grille :
        largeur=60
        x_base=-220
        y_base=-150
        setup(7*largeur+30, 430, 0, 0)
        speed(0)
        hideturtle()
        init_grille.dessiner_grille(x_base,y_base,largeur)

        print('\n\n\n\n\n\n=============================================')
        print(' DEBUT DU JEUX [HUMAIN - MACHINE]')
        print('=============================================\n\n')
        print("Avant de lancer le programme réduisez la fenêtre de Python sur la moitié droite de l'écran.")
        print("La fenêtre de la tortue sera affichée dans le coin supérieur gauche de l'écran.\n\n")
        print("Dans cette version le joueur BLEU est l'ordinateur. Vous êtes le joueur ROUGE.\n\n")
        joueur_courant = self.qui_commence_entre_hummain_et_machine()
        print('Caractères particuliers à saisir à la place du numéro de la colonne à jouer :')
        print('S : Sauvegarde la partie dans le fichier grille.txt')
        print('R : Restaure la partie à partir du fichier grille.txt')
        print('F : Fin du jeu (pour quitter le programme)')
        print('\nLe nom des joueurs sera ici ROUGE et BLEU.')
        if joueur_courant==1:
            print('Le joueur ROUGE commence.')
        else:
            print('Le joueur BLEU commence.')
        print('\nDébut de la partie (la grille est vide) :')
        gagnant=0
        while not init_grille.grille_pleine(grille) and gagnant==0:
           # init_grille.afficher(grille)
            joueurIA.jouer(grille,joueur_courant,tab_colonne,init_grille.afficher(grille))
            joueur_courant=3-joueur_courant
            gagnant=init_grille.test_gagner(grille)
            if gagnant==1:
                print('Bravo ! Le joueur ROUGE a gagné !')
            elif gagnant==2:
                print('Bravo ! Le joueur BLEU a gagné !')


        init_grille.afficher(grille)
        if gagnant==0:
            print("Fin de la partie : la grille est pleine et il n'y a pas 4 pions alignés")
        elif init_grille.grille_pleine(grille):
            print("Fin de la partie : 4 pions sont alignés et la grille est pleine")
        else:
            print("Fin de la partie : 4 pions sont alignés et la grille n'est pas pleine")

        done()



    def jeux_Humain_Humain(self):
        print("Bienvenue dans le jeu Puissance4 Humain - Humain")
        joueurIA = JoueurIA()
        joueur = Joueur()
        init_grille = Grille()
        # joueur_courant indique le prochain joueur qui doit jouer : 1 pour Kevin et 2 pour Xavier
        joueur_courant=1
        #get_colonne = joueur.get_colonne(joueur_courant)
        colonne = 7
        # tab_colonne mémorise le nombre de pions dans chacune des colonnes
        tab_colonne = colonne*[0]

        grille = init_grille.init()

        #   JEUX [Humain - Humain]

        print('Le nom des joueurs sera ici Kevin et Xavier. Le joueur Kevin commence.')
        print('Début de la partie (la grille est vide) :')
        gagnant=0
        while not init_grille.grille_pleine(grille) and gagnant==0:
            init_grille.afficher(grille)
            joueur.jouer(joueur_courant,tab_colonne,grille)
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

        #    F I N     D U     JEUX [Humain - Humain]


puissance4 = Puissance4()

puissance4.jouer_avec_humain_ou_machine()