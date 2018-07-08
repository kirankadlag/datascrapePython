# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 17:54:35 2018

@author: Kiran
"""

#Program to read footnotes from summary compensation table
import os #os module imported here
import csv
#location = os.getcwd() 

cik = list()
date = list()
table_data = list()

#print(location)
#Update a data folder path here
path = "E:/Evil Project Data/def_14a_data/"

i1 = 0
for dirs in os.listdir(path):
    firstDir = os.path.join(path, dirs)
    #read all directories inside parent directory
    if os.path.isdir(firstDir):
        for i in os.listdir(firstDir):
            #join path with parent directory 
            SecondDir = os.path.join(firstDir, i)
            print(SecondDir)
            if os.path.isdir(SecondDir):
                for j in os.listdir(SecondDir):
                    ThirdDir = os.path.join(SecondDir, j)
                    #read files from last directory
                    for file in os.listdir(ThirdDir):
                        os.chdir(ThirdDir)
                        location = os.getcwd()
                        text = ''
                        #To check file type in folder
                        if file.endswith(".txt"):
                            text = file
                    #    if file.endswith(".html"):
                    #        cik1 = file[:10]
                    #        date1 = file[12:22]
                    #        
                    #    if file.endswith(".htm"):
                    #        cik2 = file[:10]
                    #        date2 = file[12:22]
                        
                        if text == file:    
                                    
                            comments = ''
                            
                            #print(file)
                            test_file = open(file)
                            lines = test_file.readlines()
                            
                            #read all the lines from file 
                            for i in range (0, len(lines)):
                                line = lines[i]
                                #Seperating text files which having HTML tags
                                if line.find("<HTML>") == 0 or line.find("<html>") == 0:
                                    break
                                elif line.find("</FONT>") == 0:
                                    break
                                #find below matching upper or lower string in text file
                                elif line.lstrip().upper().find("SUMMARY COMPENSATION TABLE") == 0:
                                    cik.append(file[:10])
                                    date.append(file[12:22])
                                    
                                    var = ''
                                    #Preventing index of range for for loop
                                    countLength = (i+100)
                                    if (i+100) > len(lines):
                                        countLength = len(lines)
                                    
                                    #to avoid '(1)' and '(A)' from headings of table
                                    for i1 in range((i+10), countLength):
                                        #stoping reading files at this keywords
                                        #if lines[i1].find("<FN>") == 0 or lines[i1].find("</TABLE>") == 0:
                                        if var == 'found':
                                            break
                                        #start reading files from bellow conditions
                                        elif (lines[i1].lstrip().startswith("(1)") 
                                                or lines[i1].lstrip().startswith("(A)")):
                                            var = "found"
                                            
                                            #Preventing index of range for for loop
                                            countLength1 = (i+120)
                                            if (i+120) > len(lines):
                                                countLength1 = len(lines)
                                            
                                            for j in range(i1, countLength1):
                                                #To end reading of data on following conditions
                                                if (lines[j].lstrip().upper().find("RETIREMENT PLAN") == 0
                                                    or lines[j].lstrip().upper().find("EMPLOYMENT AGREEMENTS")==0
                                                    or lines[j].lstrip().upper().find("</FN>")==0
                                                    or lines[j].lstrip().upper().find("EMPLOYMENT ARRANGEMENTS")==0
                                                    or lines[j].lstrip().upper().find("RETIREMENT BENEFITS")==0
                                                    or lines[j].lstrip().upper().find("SECTION")==0
                                                    or lines[j].lstrip().upper().find("EXECUTIVE OFFICERS")==0
                                                    or lines[j].lstrip().upper().find("GRANTS OF")==0
                                                    or lines[j].lstrip().upper().find("CHANGE IN") == 0
                                                    or lines[j].lstrip().upper().find("INCENTIVE COMPENSATION PLAN") == 0 
                                                    or lines[j].lstrip().upper().find("STOCK PLANS") == 0 
                                                    or lines[j].lstrip().upper().find("ELECTION OF DIRECTORS") == 0 
                                                    or lines[j].lstrip().find("</TABLE>") == 0
                                                    or lines[j].lstrip().upper().find("PROPOSAL") == 0
                                                    or lines[j].lstrip().find("<TABLE>") == 0
                                                    or lines[j].lstrip().upper().find("AGGREGATED OPTION") == 0
                                                    or lines[j].lstrip().upper().find("DIRECTOR COMPENSATION") == 0
                                                    or lines[j].lstrip().upper().find("OPTION/SAR GRANTS") == 0
                                                    or lines[j].lstrip().upper().find("OPTION EXERCISES") == 0
                                                    or lines[j].lstrip().upper().find("SEVERANCE ARRANGEMENTS") == 0
                                                    or lines[j].lstrip().upper().find("SUPPLEMENTAL EXECUTIVE") == 0
                                                    or lines[j].lstrip().upper().find("OPTIONS/SAR GRANTS") == 0
                                                    or lines[j].lstrip().find("Fiscal Year-End Option") == 0
                                                    or lines[j].lstrip().upper().find("STOCK OPTION") == 0
                                                    or lines[j].lstrip().upper().find("CERTAIN EMPLOYMENT") == 0 
                                                    or lines[j].lstrip().upper().find("OPTION GRANTS") == 0):
                                                    break
                                                comments = comments + lines[j]
                                                        
                                    table_data.append(comments)
                                                
                                    break
                    
finalData = list()
path = "C:/Users/Sonali/Desktop/MS Subjects/BI/Evil Project Output/" 
os.chdir(path)                    
#Creating list having counter, cik number of company, date and footnotes
for i in range(len(table_data)):
    finalData.append([str(i), cik[i], date[i], table_data[i]])
                            
#writing data in csv file
with open('FinalOutput_101To143.csv', 'w') as file1:
    writer1 = csv.writer(file1, delimiter=',', lineterminator = '\n')
    #writer1.writerow(['Index', 'Company Code', 'Date', 'Comments'])
    writer1.writerows(finalData)             
                    
