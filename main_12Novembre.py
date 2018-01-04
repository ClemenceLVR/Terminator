# -*- coding: utf-8 -*-

organs = ["sheath", "cast cuticle", "cuticle", "exocuticle", "layers", "cuticle layers",
          "v-shaped mark", "annuli", "striae", "cuticular annulations", "annules",
          "posterior edge ornementations", "head annuli", "anterior end annuli",
          "cephalic region annuli", "labial region annuli", "lip annuli",
          "longitudinal striae", "longitudinal striae on head annuli",
          "horizntal lines on the annuli of the anterior end", "longitudinal grooves",
          "longitudinal grooves on head area", "radial grooves", "head basal annulus",
          "longitudinal striae on basal anulus", "labial disc", "oral disc",
          "circumoral ridge", "head disc", "first annulus", "sectors", "collar",
          "head annuli", "labial pattern", "lip pattern", "labial disc", "oral disc",
          "circumoral ridge", "head disc", "first labial annulus", "first lip annulus",
          "first cephalic annulus", "lips", "sectors", "labial annulus sectors",
          "first annulus sectors", "sub-median sectors", "sub-median pseudolips",
          "sub-median liplets", "sub-median lobes", "neck annuli", "tail annuli",
          "fused portion", "tail end annuli", "striae at terminus", "lateral field",
          "lateral alae", "wings", "lines", "lateral field lines", "incisures", "involutions",
          "section with", "junction", "section with x lines", "section with y lines",
          "bands", "lateral field bands", "areolations", "cross striations",
          "body annuli extending in lateral field", "lateral field crossed by body annuli",
          "annulation continues across the lateral field", "lateral field", "anastomoses",
          "subcuticular markings", "punctations", "hypodermis", "thorneian cells",
          "stomodeum", "stoma", "buccal cavity", "oral opening", "prostoma", "mouth opening",
          "vestibule", "guiding apparatus", "stylet guide", "spear guiding", "apparatus",
          "anterior part", "anterior part of the vestibule", "skeletal tube", "posterior part",
          "posterior part of the vestibule", "stylet", "spear", "stomatostyle", "base",
          "stylet base", "stylet lumen", "cone", "conus", "apex", "prorhabdions",
          "metenchium", "conical part of stylet", "tapering fore part", "stylet cone",
          "anterior part of stylet", "shaft", "cylindrus", "cylindrical part of the stylet",
          "telenchium", "knobs", "stylet knobs", "anterior face of knobs",
          "anterior part of knobs", "teeth", "anterior", "projections", "stylet knob teeth",
          "posterior face of knobs", "posterior part of knobs", "muscles", "stylet muscles",
          "protractors", "stylet protractors", "head musculature", "end", "end of stomodeum",
          "end of vestibule", "oesophagus", "pharynx", "lumen", "oesophageal lumen", "corpus",
          "procorpus", "precorpus", "junction procorpus median bulb",
          "junction between medial bulb et procorpus", "junction between procorpus and median bulb",
          "median bulb", "metacorpus", "metacorpal bulb", "post corpus", "valve",
          "median bulb valve", "pump", "valvular apparatus", "vesicles", "vesicles in median bulb",
          "grouping median bulb and isthmus", "junction median bulb and isthmus",
          "end of median bulb", "isthmus", "stem", "oesophageal glands", "oesophageal lobes",
          "glandular bulb", "gland bulb", "dorsal oesophageal gland", "dorsal gland opening",
          "nucleus", "dorsal gland nucleus", "subventral oesophageal glands",
          "subventral glands openings", "subventral gland nuclei",
          "oesophageal glands end", "gland overlap end", "cardia", "oesophago-intestinal junction",
          "oesophago-intestinal valve", "intestine", "mesenteron", "midgut", "lumen",
          "intestinal lumen", "fasciculi", "lateral canals", "serpentine", "origin",
          "origin of fasciculi", "fasciculi end", "proctodeum", "posterior gut",
          "hind gut", "sphincter muscle", "rectum", "wall", "rectum wall", "rectum glands",
          "rectal glands", "anus", "cloaca", "anal opening"]

properties = ["presence", "kind", "number", "thickness","number = R", "visibility", "size",
              "orientation", "shape", "width", "aspect", "arrangement", "number per number",
              "symmetry", "position relative to", "height", "diameter", "length",
              "size relative to", "appearance", "ratio", "distance to",
              "type", "location relative to", "texture", "Shape (type of stylet)",
              "posture", "angle to", "orientaion relative to", "position within",
              "angle with", "position", "habitus = posture = attitude", "angle",
              "color = colour", "diameter = width", "depth", "length relative to",
              "physiology", "position on", "Length (width)", "Width (=height)"]

source = "Female: Body usually in spiral shape.Lip region hemispherical, 4 or 5 often indistinct annules.Spear knobs with indented anterior surfaces. Excretory pore at level of anterior end of oesophageal glands. Hemizonid just anterior to excretory pore. Hemizonion usually not visible. Spermatheca usually conspicuous,offset without sperm. Phasmids 5 to 11 annules anterior to level of anus. Tail more curved dorsally, usually with slight ventral projection, 6 to 12 annules."
import re
import string

def createDict(organs):
    d = {}
    for i in organs:
        d[i]=[]
    return d

# def createlistProp(d):
#     dispo={}
#     dispo['name']
#     dispo
#     n={}
#
#     for i in d.keys():
#         for j in tuple():
#             n=( d.keys,d.tuple(j),0)
#             if n !=[]:
#                 print(n)
#                 dispo[i+j] = n
#     return dispo

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

def Association(treated_organ,treated_properties):
    oc = [] #creation liste finale
    oc1 = {} # creation liste bouche trou
    d1min = 999999 # D1 min et D2 min sont les valeurs pivots de la recherche on les affecte
    d2min = 999999
    organLeft="" # se sont les deux valeurs des organes les plus proches qui seronts ensuites compares
    organRight=""
    for i in treated_properties: # pour chaque organe on regarde sa distance par rapport a la propriete et si elle est inferieure a D1 ou D2 min ils prennent sa valeur.
         for j in treated_organ:

                d1= i.get("start")-j.get("end")
                d2= j.get("start")-i.get("end")
                if d1<d1min and j.get("av")== True: # av est un boolean de test permetant de s'assurer que l'organe/ la propriete n'est pas deja utlise
                  d1min=d1
                  organLeft=j.get("name")
                if d2min<d2 and j.get("av")== True:
                  d2min=d2
                  organRight=j.get("name")
         if d1min < d2min: # on regarde lequel des deux (le plus proche a gauche ou le plus proche a droite)
             oc1 = {'Propertie':i.get("name"),'Associated to':organLeft, 'value':"XX"}
             i["av"]= False #  la propriete devient indisponible
         else:
             oc1 = {'Propertie':i.get("name"),'Associated to':organRight, 'value':"XX"}
             i["av"] = False
         organRight=None # on reset les valeur de Dmin et les valeurs d'organes
         organLeft=None
         d1min = 999999
         d2min = 999999
         oc.append(oc1) # on ajoute l'element recupere a la liste finale
         oc1={}
    return oc
# commente avec amour par Paul 

#treated_organ = findOccurences(source, createDict(organs))
#print(treated_organ)
#treated_properties = findOccurences(source, createDict(properties))
#print(treated_properties)
#result=Association(treated_organ,treated_properties)
#print(result)

measures = ["0","1","2","3","4","5","6","7","8","9","(",")","+","-","±",",","."]
units = ["µm","mm","cm","m","µg","g","mg"]

###### TEST RECHERCHE DE VALEURS NUMERIQUES DANS UNE LISTE DE MOTS - Clémence ######

def findNumbers2(source,measures,units):
    liste = []
    si = ""
    words = source.split()
    print(words)
    for i in range(len(words)):
        mot = words[i]
        for j in range(len(measures)):
            for k in range(len(mot)):
                lettre = mot[k]
            if lettre == measures[j]:
                si += words[i]
                liste.append("".join(si))
                si = ""
    print(liste)

###### TEST RECHERCHE DE VALEURS NUMERIQUES DANS UN TEXTE N°1 - Clémence ######

#def findNumbers(source,measures,units): 
## fonction qui trouve les chiffres dans le texte et retourne une liste avec les valeurs 
## associées avec leur unité (si elles en ont une)
#    lf=[] #liste finale
#    si="" #string intermédiaire
#    size=len(source)
#    for i in range (size-1): #parcours du paragraphe
#        for j in range (len(measures)): #parcours de la liste measures
#            numb = measures[j] #numb prend la valeur du caractère 
#            if source[i] == numb: #si le caractère du texte = valeur dans measure
#                si += source[i]
##repérer les unités 
##quand on a un espace entre deux lettres il faut changer de string car pas la même valeur
#    lf.append("".join(si))    
#    print(exemple)    
#    print(lf)   
#    
## TEST AVEC RE.FINDALL
#    si = re.findall('\d',source)
#    print(si)

exemple="le vers mesure 2,5 cm de long et 5 de large"

findNumbers2(exemple,measures,units)   