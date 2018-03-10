# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:26:44 2018

@author: Aurelia
"""

#Terminator 08_03 apres reunion avec Renaud
#objectif : repartir sur un decoupage par lignes car une ligne = une triade.


import re 
import string

#from StructureDeDonnée import organsDicoSynonyms #dictionnaire organe:synonyme
#from StructureDeDonnée import valuesDico #dictionnaire propriete:values
#from StructureDeDonnée import organs
#from StructureDeDonnée import properties
from Import_script import opening 
from homonymie import property_deduction

source = "Measurements: Topotypes (10 females): L = 0.59-0.79 mm; a = 27-35; b = 5.8-6.9; b' = 4.4-5.9; c = 35-49; c' = 0.8-1.2; V = 60-65; spear = 25-28 µm; m = 46-50; O = 37-46.  Female: Body usually in spiral shape. Lip region hemispherical, 4 or 5 often indistinct annules. Spear knobs with indented anterior surfaces. Excretory pore at level of anterior end of esophageal glands. Hemizonid just anterior to excretory pore. Hemizonion usually not visible. Spermatheca usually conspicuous, offset without sperm. Phasmids 5 to 11 annules anterior to level of anus. Tail more curved dorsally, usually with slight ventral projection, 6 to 12 annules."
source2 = "Females (n = 6): L (including 'neck') = 336-515 (mean 447, standard error, 28.3); width = 149-272 (194.7, 19.7); neck length = 95-178 (128.7, 12.1); stylet length = 23.5- 24.4 (23.8, 0.2); DGO = 1.0-2.0 (1.6, 0.16); excretory pore from anterior end = 84-101 (92.6, 3.2); vulva-anus distance (lateral view) = 27.5-40.8 (36.9, 2.6); vulva length (n = 6 from cone mounts) = 10-12.7 (11.2, 0.5); thickness of cuticle --6.6-9.2 (8.2, 0.5); a = 1.9-3.4 (2.4, 0.23); O = 4.3-8.7 (6.8, 0.7).  Body asymmetrical and dorsally curved with no cone in younger individuals, oval or nearly spherical with a minute posterior protuberance in large specimens (Figs. 1B,C;3B). Neck set off and usually reflexed ventrally. Young females pearly white, becoming increasingly opaque with age and following fixation. Cuticle with a pattern of deep zigzag folds; anterior to the excretory pore a gradual transition to wavy striations and finally a relatively smooth head region. Anterior to the excretory pore, a dense material covering the head and neck region. Excretory pore slightly posterior to level of median bulb and esophageal gland region elongate. Stylet slightly curved dorsally (Fig. 1A). Ovaries paired. Subcrystalline layer not observed."
############################################################################

# This function allow to detect some nemerical value and it units , range

#regex de clemence
def findRegex(source):
# search numerical values in the text using a regex    
    pattern=re.compile(r"""
                       (([[]?[0-9]+(\s?[.,]\s?\d+)?\s?(-|to|or)\s?[0-9]+(\s?[.,]\s?\d+)?[]]?)# intervalle
    |
    ([0-9]+(\s?[.,]\s?\d+)?))
    ([ ]*(µg|cm|g|mg|µm|mm|cg|m))?
    """, re.VERBOSE)
    result = pattern.finditer(source)
    listofresult=[] #record the result in a dictionnary
    for m in result:
        listofresult.append(m.group());
    return listofresult


#fonction permettant de splitter par ligne en coupant au niveau d'un point ou point virgule
def splitLine(source):
    result = re.split('(?<!\d)[;.]|[;.](?!\d)', source)

    return(result)


#fonction de recherche d organe
#on cherche dans le dico d organes contenant le nom principal en cle et les synonymes en valeur
def findOrgans(source, dicoOrgans):
    resFinal = [] #organes trouves
    pos = [] #liste des positions des organes trouves
    source = source.lower()
    if dicoOrgans!={}:
        for key in dicoOrgans: # parcours des cles du dico
            org = source.find(key) 
            
#.find est une fct qui retourne la position d un string si on le trouve dans un autre string
#.find retourne -1 comme valeur sentinelle s il n y a pas match entre les string
            if org!=-1: #si on a trouve un match et que la position est differente de la valeur sentinelle
                resFinal.append(key) #on recupere la cle
                pos.append(org) #on recupere sa position
            else : #si la cle n existe pas dans le texte
                l_aux = dicoOrgans[key] 
                # creation d'une liste auxiliaire pour chaque cle, constituee des valeurs
                for i in range(len(l_aux)):
                    syn = source.find(l_aux[i]) #on refait la recherche avec les valeurs synonymes
                    if syn!=-1: # si la valeur i de la liste de valeurs de la cle correspond à l'organe
                        resFinal.append(key) #on remplace le synonyme par le nom de l'organe general
                        pos.append(syn)
    return(resFinal, pos)
#attention ici les organes sont affiches en fonction de leur ordre dans le dico et pas de leur ordre dans le texte
#la fonction gère directement la synonymie des organes
    

#la fonction order a pour but de remettre les organes trouves dans l ordre ou ils sont dans la phrase
#car findOrgans recupere les organes en fonction de leur position dans le dico
def order(listOrgans, listPos):
    #methode de tri par insertion
    l = len(listPos)
    for i in range(1,l):
        j=i-1
        while j>=0 and listPos[j]>listPos[j+1]:
            #si la valeur en j+1 est sup a celle en j
            listOrgans[i], listOrgans[j] = listOrgans[j], listOrgans[i]
            #on echange les valeurs en position i et j dans la liste des organes
            listPos[i], listPos[j] = listPos[j], listPos[i]
            j = j-1 #parcours de liste jusqu'à la fin
    return(listOrgans, listPos) #on recupere les listes des organes et de leurs positions triees
  
    
    
#cette fonction cherche les valeurs qualitatives exactement pareil que findOrgans
#on cherche dans le dico des proprietes et de leurs valeurs    
def findQualitativeValues(source, dicoProp):
    source = source.lower()
    resProp, resVal = [], []
    posProp, posVal = [], []
    if dicoProp!={}:
        for key in dicoProp:
            prop = source.find(key) #si on trouve une propriete explicite
            if prop != -1:
                resProp.append(key) #on recupere la propriete
                posProp.append(prop)
            else:
                l_aux = dicoProp[key]
                for i in range(len(l_aux)):
                    val = source.find(l_aux[i])
                    if val!=-1: # si la valeur i de la liste de valeurs de la cle correspond à l'organe
                        resVal.append(l_aux[i]) #on recupere la valeur associee a une propriete
                        posVal.append(val)
    return(resProp, posProp, resVal, posVal)
    #ici on recupere les valeurs qualitatives et les proprietes explicites sil y en a
    

#cette fonction permet de tenter une deduction de propriete
def property_deduction(value, prop_dico):
    #from a value we can do a deduction of its possible property
    #found = False
    l_found = [] #liste des proprietes trouvees pour une valeur donnee
    if prop_dico!={}:
        for key in prop_dico: #parcours des cles du dico des proprietes
            l_aux = prop_dico[key]
            for i in range(len(l_aux)):
                if l_aux[i]==value: #si la valeur est trouvee dans le dictionnaire
                    l_found.append(l_aux[i]) #on recupere la propriete associee

    return(l_found)
 

    
#creation d une triade a partir de trois arguments    
def createTriad(org, prop, val):
    triad = []
    triad.append(org)
    triad.append(prop)
    triad.append(val)
    return(triad)
    
    
#recherche de valeurs numeriques dans un texte 
def findPropValNum(source, regle):
    #result = []
    pattern=re.compile(regle)
    #m=re.findall(pattern, source) #recherche du motif de la regle 
        #if m:
        #    result.append(m.group())
    #return(m)
    result = pattern.finditer(source)
    listofresult=[] #record the result in a dictionnary
    for m in result:
        listofresult.append(m.group());
    return listofresult

# creation d'une triade à partir de ce qui a été trouvé dans la phrase
def newTriad(listOrg,listProp,listVal):
    triad = []
   # i = 0
   # taillemax = max(len(listOrg),len(listProp),len(listVal))
    if listVal!=[]:
        if len(listOrg)< len(listVal):
            while len(listOrg)<len(listVal):
                listOrg.append(listOrg[-1])
        if len(listProp)<len(listVal):    
            while len(listProp)<len(listVal):
                listProp.append("NA")
        if len(listVal)<len(listProp):
            while len(listVal)<len(listProp):
                listVal.append("NA")
        for i in range(len(listVal)):
            triad.append(createTriad(listOrg[i],listProp[i],listVal[i]))
        

        # triad.append(listOrg[i])
            #triad.append(listProp[i])
            #triad.append(listVal[i])
    #i += 1
    return(triad)
#fonction qui nous calculerais le pourcentage de reussite de terminator et affiche
#les triades non trouvés 
#def percentSucess(listTriades,source): 
    
    
#----------------------------- Programme principal----------------------------
    
#----------------------------- Tests fonctionnels ----------------------------

dicoOrgans = opening('organsList') # on charge le dictionnaire contenant les organes et leurs synonymes
valuesDico = opening('valuesDico') # on charge le dico contenant les valeurs et leurs synonymes

source = source.lower() #on repasse le texte en minuscules au cas ou

split = splitLine(source) #on coupe le texte en phrases
listOrgan=[]
print(split) #liste de string correspondant aux phrases

for j in range(len(split)): 
#pour chaque phrase obtenue apres split du texte phrase par phrase
    
    print("Num de ligne")
    print(j) #affiche le numero de la ligne
    print("phrase : \n",split[j],"\n")
    if (findOrgans(split[j], dicoOrgans)!= [],[]):
        org = findOrgans(split[j], dicoOrgans) 
    print (org)
    #trouve les organes de la ligne j et les stocke dans la variable org
    listOrgan.append(org)
    print("Liste d organes trouves et liste d indices de position correspondants")
    print(order(org[0], org[1])) #remet les organes dans l ordre de la phrase

    
    valQual = findQualitativeValues(split[j], valuesDico) #trouve les val qualitatives par phrase
    #valQual retourne 4 valeurs : resProp, posProp, resVal et posVal
    #valQual[0] = resProp correspond aux proprietes
    #valQual[1] correspond aux positions des prop
    #valQual[2] correspond aux valeurs qualitatives trouvees
    #valQual[3] correspond aux positions des valeurs
    
    print("Proprietes explicites trouvees si existantes :")
    print(order(valQual[0], valQual[1])) #affiche les prop et leurs positions si trouves 
    print("Valeurs qualitatives trouvees si existantes :")
    print(order(valQual[2], valQual[3])) #affiche les prop et leurs positions si trouves
    
    
    valNum = findRegex(split[j]) #trouve les valeurs numeriques par phrase
    print(valNum) 
    print("Triades numeriques de l en tete")

    propValNum = findPropValNum(split[j], r"(?<= )(.*)(?=\s=\s)")

    #fonction qui cherche a isoler les valeurs situees avant le signe egal
    #fonction sensee detecter les proprietes de l en tete
    print(propValNum)
    
    if propValNum!=[]:
        for i in range(len(propValNum)): #pour toute propriete trouvee avant le signe =
            for j in range(len(valNum)): #pour toute valeur numerique de la phrase
                print(createTriad('body', propValNum[i], valNum[j]))
                #association en triade descriptive du corps dans l en tete des mesures
    
    print("Triades crees a partir des organes/proprietes/valeurs trouvees :")
    tri = newTriad(org[0],valQual[0],valQual[2])
    
    print(tri)
    #print("test  de paul")
   # print(org[0])
    #print(valQual[0])
    #print(valQual[2])
   # print (listOrgan)
    print("***************************************")