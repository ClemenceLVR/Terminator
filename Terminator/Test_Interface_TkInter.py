# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:18:04 2018
@author: Felix
"""

from tkinter import *
from tkinter.filedialog import *
from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Interface(Frame):
    def __init__(self):
        super().__init__() #Méthode qui appel le constructeur de la classe inhérité
        self.initUI() #Creation de l'interface avec la méthode initUI()
        
    def initUI(self):
        self.master.title("Terminator")
        self.pack(fill=BOTH, expand=1)
        
    def download():
        filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
        fichier = open(filename, "r")
        content = fichier.read()
        fichier.close()
        return text_input.get(content)
        boolTest = True

def main():
    root = Tk()
    root.geometry("750x500+850+850")
    root['bg']='white'
    #app = Terminator()
    boolTest = False
    
    champ_label = Label(root, text="Coller le texte à analyser ici.")
    champ_label.pack(side=TOP)
    #Frame 1 : là ou doit apparaître le texte importé ou collé
    Cadre_Input = Frame(root)
    Cadre_Input.pack(side=TOP, padx=30, pady=30)
    
    #Caractérise la Frame 1
    var_texte = StringVar()
    text_input = Text(Cadre_Input)#, textvariable=StringVar, width=80)
    text_input.pack(side=TOP)#, fill=X)
#    if boolTest == False:
#        text_input = Text(Cadre_Input)#, textvariable=StringVar, width=80)
#        text_input.pack(side=TOP)#, fill=X)
#    if boolTest == True:
#        text_input.get(content)
    
    #Bouton d'importation
#        Button_dll_text_file=Button(root, text="Importation", command = download())
#        Button_dll_text_file.pack()
    
    #Là ou les résultats seront affiché
#    Cadre_Sortie = Frame(root)#, width=root.winfo_width)#, height=576, borderwidth=1)
#    Cadre_Sortie.pack(side=BOTTOM, padx=10, pady=10)
#    Label(Cadre_Sortie, text="cadre output",bg="white").pack(padx=10, pady=10)
    
    
    root.mainloop()  
if __name__ == '__main__':
    main() 
    
    