# Étape 1 : créer la grille de jeu sur laquelle nous allons jouer
from tkinter import Tk, Canvas
import random

Taille = 300
jeu = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def affichegrille(c="black"):
    canvas.create_line((100, 0), (100, 300), width=3, fill=c)
    canvas.create_line((200, 0), (200, 300), width=3, fill=c)
    canvas.create_line((0, 100), (300, 100), width=3, fill=c)
    canvas.create_line((0, 200), (300, 200), width=3, fill=c)

def affichepions():
    for x in range(3):
        for y in range(3):
            xx = x * 100
            yy = y * 100
            A = (xx + 20, yy + 20)
            B = (xx + 80, yy + 80)
            C = (xx + 20, yy + 80)
            D = (xx + 80, yy + 20)
            if jeu[x][y] == 1:
                canvas.create_oval(A, B, fill='blue')
            if jeu[x][y] == 2:
                canvas.create_line(A, B, fill='red', width=10)
                canvas.create_line(C, D, fill='red', width=10)

def Detectegagne():
    for j in [1,2]:
        for x in range(3):
            if jeu[x][0] == jeu[x][1] == jeu[x][2] == j : return j
        for y in range(3):
            if jeu[0][y] == jeu[1][y] == jeu [2][y] == j : return j
        if jeu[0][0] == jeu[1][1] == jeu[2][2] == j : return j
        if jeu[0][2] == jeu[1][1] == jeu[2][0] == j : return j
    return 0

def Cherchecasevide() :
    L = []
    for x in range(3):
        for y in range(3):
            if jeu[x][y] == 0:
                L.append((x,y))
    if len(L) == 0 : return False
    else :
        i = random.randint(0, len(L)-1)
        return L[i]
def Prog():
    affichegrille()

def Affiche() :
    canvas.delete('all')
    affichegrille()
    affichepions()

def click(event):
    global jeu
    Affiche()
    x = event.x // 100
    y = event.y // 100

    if Detectegagne() != 0 :  # sa relance une partie
        jeu = [[0,0,0], [0,0,0], [0,0,0]]
        Affiche()
        return
    if jeu[x][y] != 0 : return #clique sur une zone déja jouée
    # joueur humain
    jeu [x][y] = 1
    affichepions()
    if Detectegagne() == 1:
        affichegrille('blue')
        return

    # joueur ordinateur
    clalcul = Cherchecasevide()
    if clalcul != False :
        x,y = clalcul
        jeu[x][y] = 2
        affichepions()
        if Detectegagne() == 2:
            affichegrille('red')
            return



# créer la fenêtre de dessin
Mafenetre = Tk()
Mafenetre.geometry(str(Taille) + 'x' + str(Taille))
canvas = Canvas(Mafenetre, width=Taille, height=Taille, borderwidth=0, highlightthickness=0, bg="lightgray")
canvas.pack()
Mafenetre.after(100, Prog)
Mafenetre.bind("<Button-1>", click)
Mafenetre.mainloop()

