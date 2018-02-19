#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:22:57 2018

@author: skaering
"""
#from StructureDeDonnée import properties
#from StructureDeDonnée import organs
#from StructureDeDonnée import source
#from StructureDeDonnée import relativeProperties
##from StructureDeDonnée.py  import organs 
#from fonctionTerminator import intelligentOrgansResearch
#
##from fonctionTerminator import testRegex_VPaul
##from fonctionTerminator import inteligentSplit
##from fonctionTerminator import inteligentOrgansResearch
#from fonctionTerminator import recherchePropRelative
#
##def main ():
#    #OrganFounded= inteligentOrgansResearch(source,organs);
#  #  SourceSplited= inteligentSplit(source,OrganFounded);
#  #  unitsfounded= testRegex_VPaul(source);
#print(intelligentOrgansResearch(source,organs))
#print(intelligentOrgansResearch(source,properties))
##final= recherchePropRelative(source,relativeProperties,organs);
##print(final);
#    
    
###############################################################################

from fonctionTerminator import * 
from Import_script import opening
from StructureDeDonnée import source
from StructureDeDonnée import relativeProperties

###############################################################################

organ_syno = opening('OrgansSynonyms') # organs and their synonyms
values_syno = opening('Values_Synonyms') # values and their synonymps
standard_values = opening('Standards_vals') # properties and their standard values
list_organs = opening('organsList')

###############################################################################

def main(): 
    implicit_prop = deduction_Prop_implicite(source,???,standard_values)
    relative_prop = recherchePropRelative(source,relativeProperties,list_organs)
    organs_founded = intelligentOrgansResearch(source,list_organs)
    print("implicit properties",implicit_prop)
    print("relative properties",relative_prop)
    print("recherche organes",organs_founded)
    
main()
