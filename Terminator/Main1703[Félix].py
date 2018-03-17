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

source = "Measurements: Topotypes (10 females): L = 0.59-0.79 mm; a = 27-35; b = 5.8-6.9; b' = 4.4-5.9; c = 35-49; c' = 0.8-1.2; V = 60-65; spear = 25-28 µm; m = 46-50; O = 37-46. Female: Body usually in spiral shape. Lip region hemispherical, 4 or 5 often indistinct annules. Spear knobs with indented anterior surfaces. Excretory pore at level of anterior end of esophageal glands. Hemizonid just anterior to excretory pore. Hemizonion usually not visible. Spermatheca usually conspicuous, offset without sperm. Phasmids 5 to 11 annules anterior to level of anus. Tail more curved dorsally, usually with slight ventral projection, 6 to 12 annules."
#source = "Females (n = 6): L (including 'neck') = 336-515 (mean 447, standard error, 28.3); width = 149-272 (194.7, 19.7); neck length = 95-178 (128.7, 12.1); stylet length = 23.5- 24.4 (23.8, 0.2); DGO = 1.0-2.0 (1.6, 0.16); excretory pore from anterior end = 84-101 (92.6, 3.2); vulva-anus distance (lateral view) = 27.5-40.8 (36.9, 2.6); vulva length (n = 6 from cone mounts) = 10-12.7 (11.2, 0.5); thickness of cuticle --6.6-9.2 (8.2, 0.5); a = 1.9-3.4 (2.4, 0.23); O = 4.3-8.7 (6.8, 0.7). Body asymmetrical and dorsally curved with no cone in younger individuals, oval or nearly spherical with a minute posterior protuberance in large specimens (Figs. 1B,C;3B). Neck set off and usually reflexed ventrally. Young females pearly white, becoming increasingly opaque with age and following fixation. Cuticle with a pattern of deep zigzag folds; anterior to the excretory pore a gradual transition to wavy striations and finally a relatively smooth head region. Anterior to the excretory pore, a dense material covering the head and neck region. Excretory pore slightly posterior to level of median bulb and esophageal gland region elongate. Stylet slightly curved dorsally (Fig. 1A). Ovaries paired. Subcrystalline layer not observed."
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
    ordered_list = triBulle2(resFinal, pos)
    return(ordered_list)
#attention ici les organes sont affiches en fonction de leur ordre dans le dico et pas de leur ordre dans le texte
#la fonction gère directement la synonymie des organes
    

# A eviter d'utiliser, probleme de tri, le pb n'a pas été identifie
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
  

# --------------- PLUS EFFICACE QUE LA FONCTION ORDER -----------------------
    
def triBulle2(listOrgans, listPos):
    n = len(listPos)
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if listPos[j] < listPos[j-1]:
                listPos[j],listPos[j-1] = listPos[j-1],listPos[j]
                listOrgans[j],listOrgans[j-1] = listOrgans[j-1],listOrgans[j]
    return(listOrgans, listPos)
    
    
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
    list_prop_exp = order(resProp, posProp)
    list_val_qual = order(resVal, posVal)
    return(list_prop_exp, list_val_qual)
    #ici on recupere les valeurs qualitatives et les proprietes explicites sil y en a
    

#cette fonction permet de tenter une deduction de propriete
def property_deduction2(value, prop_dico):
    #from a value we can do a deduction of its possible property
    #found = False
    l_found = [] #liste des proprietes trouvees pour une valeur donnee
    if prop_dico!={}:
        for key in prop_dico: #parcours des cles du dico des proprietes
            l_aux = prop_dico[key]
            for i in range(len(l_aux)):
                if l_aux[i]==value: #si la valeur est trouvee dans le dictionnaire
                    l_found.append(key) #on recupere la propriete associee

    return(l_found)
    
    
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
    #triad = []
    #i = 0
    taillemax = max(len(listOrg),max(len(listProp),len(listVal)))
    for i in range(taillemax):
        
        if listOrg==[]:
            if listProp==[]:
                if listVal==[]:
                    createTriad("NA", "NA", "NA")
                else:
                    createTriad("NA", "NA", listVal[i])
            elif listVal==[]:
                createTriad("NA", listProp[i], "NA")
            else:
                createTriad("NA", listProp[i], listVal[i])
        elif listProp==[]:
            if listOrg==[]:
                createTriad("NA", "NA", listVal[i])
            elif listVal==[]:
                createTriad(listOrg[i], "NA", "NA") 
            else:
                createTriad(listOrg[i], "NA", listVal[i])
        elif listVal==[]:
            if listOrg==[]:
                createTriad("NA", listProp[i], "NA")
            elif listProp==[]:
                createTriad(listOrg[i], "NA", "NA")
        else:
            createTriad(listOrg[i], listProp[i], listVal[i])
        

# =============================================================================
# ATTENTION CETTE VERSION DE NEWTRIAD DATE DU 08/03 JE NE SAIS PAS QUEL EST LA BONNE
# =============================================================================
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
            
    
    
def detectionRelativeProp(source, dicoRelativeProp):
    listRelProp = []
    posRelProp = []
    if dicoRelativeProp!={}:
        for key in dicoRelativeProp:
            l_aux = dicoRelativeProp[key]
            for i in range(len(l_aux)):
                val_relative = source.find(l_aux[i])
                if val_relative != -1:
                    listRelProp.append(l_aux[i])
                    posRelProp.append(val_relative)
    return(order(listRelProp, posRelProp))
    #retourne les listes ordonnees des valeurs de propriétés relatives
    #il faut déduire la propriete

    
def addRelativeProp(listRelativeProp, posRelativeProp, listOrgans, posOrgans, dicoRelativeProp):
    #recuperer la position de la valeur dans le texte, mais concatener l'organe a la propriete et pas la valeur
    relativeProp = ''    

    if listRelativeProp!=[]: #si on a une valeur de prop relative trouvee dans le texte
        for i in listRelativeProp: 
            deduc = property_deduction2(i, dicoRelativeProp)  #on deduit la prop globale associee
            #deduc est une liste contenant les proprietes possibles pour cette valeur
            if deduc!=[]: #si on trouve la prop relative
                if listOrgans!=[]: #s'il y a des organes toruves dans la liste
                    for j in posRelativeProp: #positions des valeurs de prop relatives trouvees
                        ind_prop = posRelativeProp.index(j)
                        for k in posOrgans: #pour les organes trouves dans la phrase
                            ind_org = posOrgans.index(k) #on recupere l'indice de leur position dans la phrase
                            if j<k and relativeProp=='': #si la prop relative se trouve avant un organe
                                relativeProp = deduc[0] + ' ' + listOrgans[ind_org] #alors on les associe
                                #la prop est composee de la prop deduite a partir de la valeur + l'organe trouve apres
    if relativeProp!='':
        
        return(relativeProp) 
        #on recupere la PROPRIETE ET SON ORGANE RELATIF, par exemple 'position relative to anus'
        #la valeur correspond a ce qu'on a trouve initialement dans le texte, exemple 'anterior to'
        #il faut garder les deux pour les associer a l'organe correspondant
        
        
    
def modifiersDetect(source, listModifiers):
    # meme principe de detection de valeurs que d'habitude
    # stockage des modifiers trouves dans une liste et de leurs positions dans une autre
    modifiersFound = []
    pos = []
    source = source.lower()
    for i in listModifiers:
        modifiers = source.find(i)
        if modifiers!=-1:
            modifiersFound.append(i)
            pos.append(modifiers)
            
    return(order(modifiersFound, pos))
    
def addModifiers(listValue, posValue, listModifiers, posModifiers):
    newString = ''
    if listValue!=[]: #s'il y a des val qualitatives
        if listModifiers!=[]: #s'il y a des 'modifiers' dans la phrase
            for i in posValue: #pour chaque position de la liste des positions
                ind_val = posValue.index(i) #on recupere l'indice de cette valeur dans sa liste
                for j in posModifiers: #pour tout modifier trouve 
                    ind_mod = posModifiers.index(j) #on recupere son indice dans la liste
                    if j<i and newString=='': #si le modifier se situe avant la val
                        newString = listModifiers[ind_mod] + ' ' + listValue[ind_val] #on les associe
                        listValue[ind_val]=newString #on remplace la nouvelle valeur dans la liste des valeurs
    if newString!='':
        return(listValue)       
      
#creation d une triade a partir de trois arguments    
#def createTriad(org, prop, val):
#    triad = []
#    triad.append(org)
#    triad.append(prop)
#    triad.append(val)
#    return(triad) 


#Cette fonction permet de trouver les phrases avec des possibles measurement dedans
#En somme elle prend en parametre les phrases découpé et les résultats de regex
#On commence par détecter les "=" puis ce qui se trouve à la droite est surement la valeur et à gauche la propriété décrite
        #à partir de ça la fonction retourne 2 listes, une de propriétés et l'autre de valeurs
#ATTENTION j'ai voulu faire une double vérification pour savoir si cétait bien une phrase measurement 
        #à savoir est ce qu'il y a un "=" et surtout est ce qu'il y a une regex de trouvé à droite 
        #malheureusement ça ne fonctionne pas d'où le code en commentaire au milieu mais apparement c'est pas trop grave...
def findMeasurement(source, rgx):
    src = source.split(" ") #Split de la phrase en liste de mots
    resVal = "" 
    listProp = []
    posEqual = 0
    for i, word in enumerate(src): 
        if word == '=': #Si mon mot est un "="
            posEqual = i #je prends sa position
#            r = " ".join(rgx) #je refais une phrase de la liste regex
#            reg = source.find(r)            #après avoir regarder s'il y a un "=" je regarde s'il y a un regex
#            if reg != -1:                   # -> si oui c'est surement une phrase measurement
            for i, word in enumerate(src): #reparcours de la source
                if posEqual < i:# regarde les mots après le "="
                    resVal = resVal + src[i] + " " #j'en fais un string (plus commode qu'une liste à manipuler) -> les probables valeurs
                if posEqual > i: #Pour ce qu'il y a avant le "="
                    if src[i] != "":
                        listProp.append(src[i]) # = listProp + src[i] + " " .append(src[i]) #J'en fais un string -> les popriétés
    return(listProp, resVal)

#Cette fonction permet une première construction de triad avec les résultats de findMeasurement
#Elle est assez simple, elle prends en parametre les deux listes retourné par findMeasurement et retourne une triad
#Cette fonction est particulièrement efficace quand la phrase est du style "a = 0,4"
#Si les phrases contiennent une propriétés à une lettre je transforme ça en Ratio machinn ou équilant en fonction de ce qui est détecter
def createTriadMeasurement1(listProp, resVal):
    triad = []
    for i, word in enumerate(listProp):
        if word == "l" or word == "a" or word == "b" or word == "b'" or word == "v":
            triad.append("Body")
            if word == "l":
                triad.append("Length")
            else:
                triad.append("Ratio " + word)
            triad.append(resVal)
        if word == "c" or word  == "c'":
            triad.append("Tail")
            triad.append("Ratio " + word)
            triad.append(resVal)
        if  word == "spear" or word == "m":
            triad.append("Stylet")
            if word == "spear":
                triad.append("Length")
            else:
                triad.append("Ratio " + word)
            triad.append(resVal)
        if  word == "o":
            triad.append("Dorsal gland openning")
            triad.append("Ratio " + word)
            triad.append(resVal)
    return(triad)
    
#Deuxiéme fonction de création de Triad en fonction un seul résultat de findMeasurement qui est la liste des propriétés (N'est pas nécessairement utilisé!)
#Cette fonction prends en parametre 
    #La liste de valeur retourné par measurement (pas toujour utilisé)
    #la liste de résulat de findPropValNum qui donne ce qui se trouve avant les = (fonction d'Aurélia)
    #La liste des organes de findOrgan
    #la liste prop de findQualitativeValues
#à chaque fois j'ajoute ce qui se trouve à droite de = (trouvé dans findMeasurement)
def createTriadMeasurement2(resVal, propValNum, listOrg, listP):
    triad = []
    if propValNum != []:
        org = ""
        prop = ""
        if listOrg != []:
            org = " ".join(listOrg) #ça peut paraitre bizzare de rassembler tout les organes trouvé en 1 mais j'ai remarqué que cétait plus juste dans la réalité et si il y a vraiment un erreur alors elle sera modifiable. Ca permet surtout de contourner le pb des organes en 2 mots
            triad.append(org)
        else:
            org = ("Organ not found") # dans le cas ou findOrgan ne trouve rien
            triad.append(org)
        if listP != []:
            prop = " ".join(listP) #meme truc chelou si plusieurs organes sont trouvé j'en fait 1 ça évite le problèm des prop en 2 mots
            triad.append(prop)
        else:   
            prop = ("Property not found") #dans le cas ou findPropValNum ne retourne rien
            triad.append (prop)
        triad.append(resVal)
    return(triad)
    
#Cette fonction est vraiment con LOL. Parce que creatTriadMeasurement1 ne rentre jamais de "Organ not found, Prop not found..."
#Mais elle me permet quand même de sélectionner la meilleur version de triad des deux fonction, createTriadMeasurement 1 et 2
def scoreTriad(listTriad):
    score = 0
    if listTriad != []:
        for word in (listTriad):
            if word == "Organ not found":
                score = score + 1
            if word == "Property not found":
                score = score + 1
            if word == "Value not found":
                score = score + 1
    else:
        score = 100 #ça c'est dans le cas ou une des deux fonction createTriadMeasurement 1 ou 2 renvoie une liste vide, je met un score aberant pour qu'elle ne soit pas sélectionner pour le display
    return(score)

            
#----------------------------- Programme principal----------------------------
    
#----------------------------- Tests fonctionnels ----------------------------

listModifiers = ["usually", "often", "rarely", "almost"]

#dicoPropRelative = {'size relative to': ['much smaller', 'smaller', 'same size', 'larger', 'much larger'], 'position relative to': ['anterior to', 'at anterior end of', 'at level of', 'at middle of', 'at posterior end of', 'posterior to', 'lower', 'higher'], 'distance to': ['very close', 'close', 'far', 'very far'], 'angle with': ['very acute', 'acute', 'oblique', 'right angle', 'obtuse', 'very obtuse', 'parallel', 'open', 'very open']}


dicoOrgans = opening('organsList') # on charge le dictionnaire contenant les organes et leurs synonymes
valuesDico = opening('valuesDico') # on charge le dico contenant les valeurs et leurs synonymes
# =============================================================================
#       Mis en commentaire par Félix
# =============================================================================
#dicoRelativeProp = opening('relativeProp')

source = source.lower() #on repasse le texte en minuscules au cas ou

split = splitLine(source) #on coupe le texte en phrases

print(split) #liste de string correspondant aux phrases

for j in range(len(split)): 
#pour chaque phrase obtenue apres split du texte phrase par phrase
    
    print("Num de ligne")
    print(j) #affiche le numero de la ligne
    print("phrase : \n",split[j],"\n")
    
    org = findOrgans(split[j], dicoOrgans) 
    #trouve les organes de la ligne j et les stocke dans la variable org
    
    print("Liste d organes trouves et liste d indices de position correspondants")
    print(org) #remet les organes dans l ordre de la phrase
    #org_ord = order(org[0], org[1])
    
    valQual = findQualitativeValues(split[j], valuesDico) #trouve les val qualitatives par phrase
    #valQual retourne 4 valeurs : resProp, posProp, resVal et posVal
    #valQual[0] = resProp correspond aux proprietes
    #valQual[1] correspond aux positions des prop
    #valQual[2] correspond aux valeurs qualitatives trouvees
    #valQual[3] correspond aux positions des valeurs
    
    print("Proprietes explicites trouvees si existantes :")
    print(valQual[0][0], valQual[0][1]) #affiche les prop et leurs positions si trouves 
    print("Valeurs qualitatives trouvees si existantes :")
    print(valQual[1][0], valQual[1][1]) #affiche les prop et leurs positions si trouves
    #list_prop_exp = valQual[0], valQual[1])
    #list_val_qual = order(valQual[2], valQual[3])
    
    a = valQual[0]
    b = valQual[1]
    
    
    
    valNum = findRegex(split[j]) #trouve les valeurs numeriques par phrase
    print(valNum) 
    #if valNum!=[]:
    #    for i in range(len(valNum)):
            
    
    print("Triades numeriques de l en tete")

    propValNum = findPropValNum(split[j], r"(?<= )(.*)(?=\s=\s)")

    #fonction qui cherche a isoler les valeurs situees avant le signe egal
    #fonction sensee detecter les proprietes de l en tete
    print(propValNum)
    print("******************************************************")
    #Run des fonctions de détection de measurement
    m = findMeasurement(split[j], findRegex(split[j]))
    c = createTriadMeasurement1(m[0], m[1])
    c2 = createTriadMeasurement2(m[1], propValNum, org[0], valQual[0][0])
    scoreCreateTriad = scoreTriad(c)
    scoreCreateTriad2 = scoreTriad(c2)
    #Selon la fonction qui a le meilleur score (le plus proche de 0) / celle qui a trouvé le plus
    #C'est la que c'est un peu con(cf commentaire fonction score) parce que creatTriadMeasurement1 renvoit toujours 0 ou 100 (elle trouve tout ou rien)
    if scoreCreateTriad < scoreCreateTriad2:
        print(c)
    elif scoreCreateTriad > scoreCreateTriad2:
        print(c2)
    else:
        print("No measurement found") 
    print("******************************************************")
# =============================================================================
#     Mis en commentaire par Félix
# =============================================================================
#    if propValNum!=[]:
#        for i in range(len(propValNum)): #pour toute propriete trouvee avant le signe =
#            for j in range(len(valNum)): #pour toute valeur numerique de la phrase
#                print(createTriad('body', propValNum[i], valNum[j]))
                #association en triade descriptive du corps dans l en tete des mesures
    
    print("Triades crees a partir des organes/proprietes/valeurs trouvees :")
    #tri = newTriad(org_ord[0],prop_exp[0],val_qual[0])
    #print(tri)
    
    
    #gestion des cas particuliers
    print("Modifs des listes de propriétés et valeurs")
    
    theModifiers = modifiersDetect(split[j], listModifiers)
    print("Modifiers")
    print(theModifiers)
    print("Add modifiers")
    print(addModifiers(b[0], b[1], theModifiers[0], theModifiers[1]))
    #retourne la valeur modifiee
    #il faut recuperer cette valeur pour la remplacer dans la liste de val qual trouvees pour la phrase
    
# =============================================================================
#     Mis en commentaire par Félix
# =============================================================================
    #proprietes relatives
    #rel_values = detectionRelativeProp(split[j], dicoRelativeProp)
    #print("Valeurs des propriétés relatives :")
    #print(rel_values)
    #print("Concaténation avec l'organe :")
    #retourne la propriete relative deduite et l'organe associe suite a la valeur trouvee dans le texte
    #add_rel_prop = addRelativeProp(rel_values[0], rel_values[1], org[0], org[1], dicoRelativeProp)
    #print(add_rel_prop)
    
    
    print("***************************************")