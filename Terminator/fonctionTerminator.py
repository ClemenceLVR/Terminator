#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:27:12 2018

@author: skaering
"""

import re 

units = ["µm","mm","cm","m","µg","g","mg"]

def testRegex(source,units):
    val = []
    pattern = re.compile(r"[^A-Za-z][0-9]*?[.,]\d?*") # regex (nombres entiers et décimaux)
    words = source.split() # split de la phrase en une liste de mots
    ##print(exemple)
    print(words)
    for i in words: # on parcours la liste de mots
        if pattern.match(i): # si on trouve un match dans la liste
            print(i, "it matches")
            num = words.index(i) # on relève la position du mot qui matche
            for u in units:
                if words[num+1] == u: # si le mot qui suit est une unité
                    val.append("".join(i + words[num+1])) # on l'ajoute en même temps que le mot dans la liste
## Le problème est avec ce else... Quand on le décommente le résultat n'est pas celui attendu
#                else: 
#                    val.append("".join(i)) # sinon on ajoute seulement le mot
        else: 
            print(i, "it does not match")
    print(val)
    

def testRegex_V2(source):
    pattern = re.compile(r"[-+]?\d*[.,]\d+|\d+")
    result = pattern.findall(source)
    print(result)

def testRegex_VPaul(source):
#    pattern = re.compile(r"(([1-9][0-9]*|0)([.,]\d+)?|[[]?([1-9][0-9]|0)([.,]\d+)?-([1-9][0-9]|0)([.,]\d+)?[]]?)([ ]*(µg|cm|g|mg|µm))?")           
    pattern=re.compile(r"""
                       (([[]?[0-9]+([.,]\d+)?-[0-9]+([.,]\d+)?[]]?)# intervalle
    |
    ([0-9]+([.,]\d+)?))
    ([ ]*(µg|cm|g|mg|µm|mm|cg|m))?
    """, re.VERBOSE)
    result = pattern.finditer(source)
    listofresult={}
    for m in result:
        print(m.group())
        listofresult.append(m.group());
    return listofresult
        
        
def inteligentOrgansResearch(source,sourcelist):
    listOfFoundedOrgans=[]
    source1= source 
    sourceSplited= list(source1.split());
    i=0
    while (i < len(sourceSplited)):
        if sourceSplited[i] in sourcelist:
            pos, x=i+1,sourceSplited[i]
            while ((pos< len(sourceSplited)) and (x+" "+sourceSplited[pos] in sourcelist)):
               x=x + ' ' + sourceSplited[pos]   
               print(x)
               pos+=1
            listOfFoundedOrgans.append(x)
            i=pos
        else:
            i+=1
    return listOfFoundedOrgans


def inteligentSplit (source, organs):
    source1=source.lower();
    sourceSplited=list(source1.split())
    i=0 
    while(i<len(sourceSplited)):
        if sourceSplited[i] in organs:
            sourceSplited[i]="@"
        i+=1    
    str="".join(sourceSplited)
    return (str.split("@"))

def createDict(organs):
    d = {}
    for i in organs:
        d[i]=[]
    return d

def findOccurences(source, d):
    oc=[]
    oc1={}

    for i in d.keys():

        for j in list(re.finditer(i, source)):
            oc1 = {'name': i, 'start':j.start(), 'end':j.end(),'av':True}

        if "start" in oc1:

            oc.append(oc1)

        oc1={}
    return oc




def findWordsInSource(oc,d):
    for w in d.keys():
        if oc.get(w) != None:
            d[w]=oc.get(w)
    return d

def deduction_Prop_implicite(source):
    org = [] #list organs, valeurs, prop
    val = []
    prop = []
    c = ""
    n = ""
    chint = ""
    u = 0
    Sentences_list = source.lower().split(".") #je coupe en phrase grâce au point et je majuscule->minuscule
    for i, sentence in enumerate(Sentences_list): #pour chaque phrases
        word_sent = Sentences_list[i].split(" ") #je coupe en mots
        for j, word in enumerate(word_sent): #pour chaque mot -> 2 tests
            u = len(word_sent) #Je reléve l'indice du dernier item de la liste word_sent (enfin ça me renvoie le dernier +1 je sais pas pourqoui)
            if j != u-1: # Si j n'est pas le dernier mot (item) de la liste alors
                chint = word + " " + word_sent[j+1] #la chaine intermediaire prends le mot plus celui après "lip" + "region"
            for o, key_organ in enumerate(dico_Organ_Prop.keys()): #test : est-ce un organe répertorié
                if chint == key_organ: #est ce que l'organe est un organe à deux mot "lip region"
                    org.append(key_organ) #si oui ajout à la liste
                    c = dico_Organ_Prop.get(key_organ) #Je stock la valeur de cette clé 
                    chint = "" #la chaine doit être vidé
                elif word == key_organ: #sinon est ce que le mot est un organe répertorié
                    org.append(word) #si oui ajout à la liste
                    c = dico_Organ_Prop.get(key_organ) #Je stock la valeur de cette clé         
            for key, value in dico_Prop_Value.items():#test : est-ce une valeur répertoriée 
                if word == value:
                    val.append(value) #si oui ajout à la liste
                    n = key #Je stock la clé de cette valeur
            if c == n and c != '' or n != '':                       #Test final: est ce que la valeur de dicoOrg,Prop (donc prop) 
                prop.append(c)                                      # est égale à la clé de dicoProp,Val (la clé est aussi prop)
                c = "" #reset des bouches trous
                n = ""
    for i, o, j in zip(org, val, prop):
        print("Organe : ", i, "       sa valeur est : ", o, "  Propriété associé : ", j)
        
        ## fonction permettant de rechercher une proprieté relative exlicite et les organes qui lui sont associé
def recherchePropRelative (source,listeRelativeProp,organs):
    ListFoundedProp= inteligentOrgansResearch(source,listeRelativeProp); #on recherche si on a des proprietés explicites
    print(ListFoundedProp);
    final=[] #création de la liste finale
    if len(ListFoundedProp) != 0:#si on a des prop relatives
       # ListFoundedOrgan = inteligentResearch(organs);
        source1= inteligentSplit(source,ListFoundedProp);#on split par les prop trouvés
       # l= [];#creation d'une liste tampon
        couple=[];# creation de la liste contenant les couples
        for i in len(source1): #pour chaque élément de la liste splité: 
            l= inteligentOrgansResearch(source1[i],organs);  #on regarde si on a des organes dedans et on les met dans l
            if len(l)>0: 
                couple.append(l[0]);#couple prend le premier et le derniers element de l
            if len(l)>1: #si il y a plus d'un element couple prend le  dernier de la liste l
                couple.append(l[len(l)]); 
        couple.remove(1); # on suprime le premier de couple qui fausse le resultat
        for  j in len(ListFoundedProp):  # pour chaque prop trouvé : final recoit le premier couple puis la prop puis le second couple 
            tampon={couple[0],ListFoundedProp[i],couple[1]}
            ##print(tampon);
            final.append(tampon)
            couple.remove(0); # ensuite supression des couples ajoutés
            couple.remove(1);
        return final; 
        
        
            
   
    
        