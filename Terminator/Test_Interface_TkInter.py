## -*- coding: utf-8 -*-
#"""
#Created on Mon Feb  5 14:18:04 2018
#@author: Felix
#"""
#
#from tkinter import *
#from tkinter.filedialog import *
#import tkinter as tk
#from tkinter import TclError
##from tkinter import Tk, BOTH
##from tkinter.ttk import Frame
#
#class Interface(Frame):
#    def __init__(self):
#        super().__init__() #Méthode qui appel le constructeur de la classe inhérité
#        self.initUI() #Creation de l'interface avec la méthode initUI()
#    
#    def initUI(self):
#        self.master.title("Terminator")
#        self.pack(fill=BOTH, expand=1)
#        
#def download():
#    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
#    fichier = open(filename, "r")
#    content = fichier.read()
##    text_input.insert(Tk,"mes couilles{}".format(content))
#    text_input.insert("self.first", content)#, *args)
#    fichier.close()
##    add_text(content)
##    try:
##        start = text_input.index("self.first")
##        end = text_input.index("self.last")
##        text_input.delete(start, end)
##    except TclError:
##    text_input.insert("self.first", str)#, *args)
##    return text_input.get(content) 
#    
##def add_text(str):
##    try:
##        start = text_input.index("self.first")
##        end = text_input.index("self.last")
##        text_input.delete(start, end)
##    except TclError:
##        text_input.insert("self.first", str)#, *args)
#
#    
##def main(): #à garder
#root = Tk()
#root.geometry("750x500+850+850")
#root['bg']='white'
#boolTest = False
#champ_label = Label(root, text="Coller le texte à analyser ici.")
#champ_label.pack(side=TOP)
#            #Frame 1 : là ou doit apparaître le texte importé ou collé
#Cadre_Input = Frame(root)
#Cadre_Input.pack()
#            #Caractérise la Frame 1
#text_input = Text(Cadre_Input)
#text_input.pack(side="top", fill="both", expand=True)  


#root.mainloop() 
#    
#    
##if __name__ == '__main__':
##    main() 





import tkinter as tk
from tkinter import TclError
from tkinter import *
from tkinter.filedialog import *
from win32api import GetSystemMetrics
#from tkinter import Tk, BOTH
#from tkinter.ttk import Frame

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs): #master à rajouter
        tk.Tk.__init__(self, *args, **kwargs) #master=None
#        self.master.title("Terminator")
        width = GetSystemMetrics(0) #trouve les dimensions de l'écran en largeur
        height = GetSystemMetrics(1) #trouve les dimensions de l'écran en longueur
        self.text = tk.Text(self, width=100, height=10)
        self.text.pack(side="bottom", fill="both", expand=True)
        Button_dll = tk.Button(self, text = "Importation", command = self.doit)
        Button_dll.pack()
        
        #Button de lancement d'algorithme
        Button_algo = tk.Button(self, text = "Traitement", command = self.traitement)
        Button_algo.pack()
        
        #Là ou les résultats seront affiché
#        self.frame = tk.Frame(self)
#        self.frame.pack()#, width=width, height=height)
#        Label(Cadre_Sortie, text="cadre output",bg="white").pack(padx=10, pady=10)
    
    def traitement(self, *args):
#        ent1=Entry(root)
        start = self.text.index("sel.first") 
        end = self.text.index("sel.last")
        entry = self.text.get(start, end)
        equals_search(entry)
#        print(entry)
        
    def doit(self, *args):
        filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt', ),('all files','.*')])
        fichier = open(filename, "r")
        content = fichier.read()
        fichier.close()
        try:
            start = self.text.index("sel.first")
            end = self.text.index("sel.last")
            self.text.delete(start, end) # delete the selected text, if any -> Ne fonctionne pas
            self.text.insert("insert", content)
        except TclError: # nothing was selected, so paste doesn't need to delete anything
            self.text.insert("insert", content)
            pass

if __name__ == "__main__": #"Terminator"
    app = SampleApp()
    app.mainloop()  
    
def equals_search(source):
    ch = source #je passe la source dans une variable string
    ch2 ='' #variable string final après detection préalable des "=" afin de voir si il y a une faute de frappe 
    chint = '' #variable string intermediaire
    i = 0 #variable compteur (j'arrive pas à faire sans)
    for c in ch: #Pour chaque caracters dans le string
        ch2 = ch2 + c #à chaque tour de boucle (par caracters) j'avoute le caractère à la chaine
        if c == "=": #si le caractére est un "="
            if ch[i+1] != " ": #Je regarde si le caractére suivant est bien un espace " "
                ch2 = ch2 + ' ' #sinon j'ajoute cette espace
            if ch[i-1] != " ": #Je regarde si le caractère d'avant est lui aussii bien un espace
                chint = ch2 #si c'est pas un, espace je passe ma chaine de caractère dans une chaine intermédiaire
                ch2 ='' #je vide la chaine ch2
                ch2 = chint[:i-1] + " =" #finalement je reconstruis la chaine jusqu'au cractére avant le "=" est j'ajoute un espace puis le "="
        i +=1  #j'increment
    r = ch2.replace(';','') #je vire tout les ; et les remplace par rien
    Word_list = r.split(" ") #je coupe ma chaine en une liste de mot en fonction de l'espace " " (les espacent disparaissent après)
    prop = []  # list of properties
    val = []  # list of value
    unit = [] # list of the unit 'nm', 'µm' ...
    c = 0 # just a integer
    b = False # a boolean
    for i, word in enumerate(Word_list): 
        if word == "Measurements:": # if the word Measurements appears
            c = i # the integer take the position of "Measuremts:" in the list
            b = True #True there's a word "Measurements:"
        if word == '=': # we search for the "="
            if i > c and b == True: # if the "=" word doesn't concern the desciption tag (REF_NO, SPECIES_NO...)
                prop.append(Word_list[i-1]) # the word at the right of "=" is supposed to be the property
                val.append(Word_list[i+1]) # the word at the left of "=" is supposed to be the value
                UnitWord = Word_list[i+2]
                if UnitWord == 'µm'or UnitWord == 'mm' or UnitWord == 'nm':
                    unit.append(Word_list[i+2])
                else:
                    unit.append('') 
    for i, o, j in zip(prop, val, unit): # browse two list at the same time with zip
        print(i, " = ", o, j) # easy display
        