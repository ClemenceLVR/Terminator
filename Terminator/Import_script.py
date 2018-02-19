# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:35:11 2018

@author: clemence
"""

import xlrd
import pickle

########## Import de fichiers excel sous forme de dictionnaires ###########

# Attention la fonction est faite de façon à ce que les données qui doivent 
# être extraîtes des documents excels soient sous forme de deux colonnes,
# sans titre, avec le premier mot en A1. 
# Pour fonctionner le script python doit être dans le même dossier que le 
# fichier excel que l'on souhaite utiliser.

def import_dico(nomDoc,nomSheet):
    # Attention à écrire le nom du doc entre simple '' + .xlsx
    # Attention, pour le nomSheet écrire sous la forme u'nomSheet' !!

    
    # Loading of the Excel sheets
    wb = xlrd.open_workbook(nomDoc)
    # Reading sheets of the doc
    sh = wb.sheet_by_name(nomSheet)
    
    synonyms = []
    dico = {}
    
    for rownum in range (0,sh.nrows): 
    # on parcours les lignes une par une à partir de la ligne 0
        synonyms.append(sh.row_values(rownum))    
        # on ajoute les mots du document dans une liste : une liste créée par ligne
        
        for key, value in synonyms: # on parcourt la liste
            if key not in dico:
                dico[key] = [value]
            # si la clé n'existe pas encore dans le dico on la créée, avec sa valeur associée 
            else:
                if not value in dico[key]: # si la valeur ne fait pas déjà partie des valeurs associées à la clé (évite la redondance)
                    dico[key].append(value)
                    # sinon on ajoute la valeur à la liste de valeurs de la clé
    
    return(dico)
    
def list_organs(nomDoc,nomSheet):
        # Loading of the Excel sheets
    wb = xlrd.open_workbook(nomDoc)
    # Reading sheets of the doc
    sh = wb.sheet_by_name(nomSheet)
    
    synonyms = []
    
    for rownum in range (0,sh.nrows): 
    # on parcours les lignes une par une à partir de la ligne 0
        synonyms.append(sh.row_values(rownum))    
        # on ajoute les mots du document dans une liste : une liste créée par ligne
    return(synonyms)
    
########## Enregistrement et lecture du fichier contenant le dico ###########
    
def register(dico,fileName):
    # record the dictionnary in a file
    with open(fileName,'wb') as theFile: 
        myPickler = pickle.Pickler(theFile) # indicate in which file we will work 
        myPickler.dump(dico) # write in the dictionnary
        
def opening(fileName):
    # open the file and read it
    with open(fileName,'rb') as theFile:
        myDepickler = pickle.Unpickler(theFile)
        dictionnary = myDepickler.load()
    return(dictionnary)

########## Enregistrement et lecture du fichier contenant le dico ###########

def add_Organ(word,dico):
    for key, value in dico: 
        if word not in dico: 
            dico[key] = word
            

##############################################################################################
            
dico = list_organs('Fichier_Dictionnaire.xlsx',u'Organes')
register(dico,'organsList')
test = opening('organsList')
print(test)