#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:22:57 2018

@author: skaering
"""
from StructureDeDonnée import properties
from StructureDeDonnée import organs
from StructureDeDonnée import source
from StructureDeDonnée import relativeProperties
#from StructureDeDonnée.py  import organs 
from fonctionTerminator import inteligentOrgansResearch

#from fonctionTerminator import testRegex_VPaul
#from fonctionTerminator import inteligentSplit
#from fonctionTerminator import inteligentOrgansResearch
from fonctionTerminator import recherchePropRelative

#def main ():
    #OrganFounded= inteligentOrgansResearch(source,organs);
  #  SourceSplited= inteligentSplit(source,OrganFounded);
  #  unitsfounded= testRegex_VPaul(source);
print(inteligentOrgansResearch(source,organs))
print(inteligentOrgansResearch(source,properties))
#final= recherchePropRelative(source,relativeProperties,organs);
#print(final);
    
    
    