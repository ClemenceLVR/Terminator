# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:15:17 2018

@author: clemence
"""

#################### Writing the results in an excel file #####################

from xlwt import Workbook

def export(): 
    
    # creation
    book = Workbook()
    
    # creation of the first sheet
    sheet1 = book.add_sheet('Results')
    
    # adding the headers
    sheet1.write(0,0,'Organ')
    sheet1.write(0,1,'Property')
    sheet1.write(0,2,'Value')
    
    #filling the table
    # ??
    
    # material creation of the existing file
    book.save('FinalResults.xlsx')