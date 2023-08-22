import tkinter as tk
import time
import random

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

#Création de ma liste contenant les opérations
operations = [
    {"operation": "addition", "a": random.randint(1,1000), "b": random.randint(1,1000)},
    {"operation": "soustraction", "a": random.randint(1,1000), "b": random.randint(1,1000)},
    {"operation": "multiplication", "a": random.randint(1,1000), "b": random.randint(1,99)},
    {"operation": "division", "a": 2022, "b": 3}
]

#Création de mon interface appelée "fenetre" avec initialisation de la taille par defaut
fenetre = tk.Tk()
fenetre.geometry("1500x1500")
fenetre.title("EXPOSE GROUPE 14 ")

label=tk.Label(fenetre,text="Ce code est un calcul mental qui ne necessite aucune saise de la part de l'utilisateur",font=("Helvetica", 25) )
label.pack()
label=tk.Label(fenetre,text=" Are you ready ?",font=("Helvetica", 40) )
label.pack()

time.sleep(15)

#séquences de calcul 
for operation in operations:
    label = tk.Label(fenetre, text=f"Calculer {operation['operation']}({operation['a']}, {operation['b']})", font=("Helvetica", 40))
    label.pack()
    fenetre.update()
    time.sleep(10)
    label = tk.Label(fenetre,text="Fin du temps", font=("Helvetica", 16))
    label.pack()
    fenetre.update()
    resultat = eval(f"{operation['operation']}({operation['a']}, {operation['b']})")
    time.sleep(7)
    label = tk.Label(fenetre,text=f"le resultat est {resultat}", font=("Helvetica", 24))
    label.pack()
    fenetre.update()
    time.sleep(7)

label = tk.Label(fenetre, text="Terminé!", font=("Helvetica", 40) ,bg="orange")
label.pack()

fenetre.update()

fenetre.mainloop()
