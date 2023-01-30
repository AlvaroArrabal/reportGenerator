import pandas as pd
import os
currentPath = os.getcwd()
import warnings



def expansion(numCells,numTechs):
    pathNOK = currentPath + "\\Data\\Babysitting_1.xlsx"
    df = pd.read_excel(pathNOK, engine="openpyxl")
    columns = []

    for i in range(0,numCells*numTechs*2,2): 
        columns.append([i+5, i+6,"Unnamed: " + str(i+5),"Unnamed: " + str(i+6)])
    columnsList = []

    for i in columns:
        columnsList.append(df.iloc[:,[3,i[0],i[1]]])
    
    NOKList = []

    for i in range(len(columnsList)):
        for j in range(len(columnsList[i])):
            if columnsList[i].iloc[j][columns[i][3]] == "NOK": 
                NOKList.append([columnsList[i].iloc[0,1] , columnsList[i].iloc[j]["Unnamed: 3"]])
    return NOKList

def consolidation(numCells,numTechs):
    pathNOK = currentPath + "\\Data\\Babysitting.xlsx"
    
    df = pd.read_excel(pathNOK, engine="openpyxl")

    columns = []

    for i in range(0,numCells*numTechs*2,2): 
        columns.append([i+3, i+4,"Unnamed: " + str(i+3),"Unnamed: " + str(i+4)])
    columnsList = []

    for i in columns:
        columnsList.append(df.iloc[:,[1,i[0],i[1]]])
    
    NOKList = []

    for i in range(len(columnsList)):
        for j in range(len(columnsList[i])):
            if columnsList[i].iloc[j][columns[i][3]] == "NOK": 
                #NOKList.append([columnsList[i].iloc[0,1] , columnsList[i].iloc[j]["Unnamed: 1"],columnsList[i].iloc[j][1]])
                NOKList.append([columnsList[i].iloc[0,1] , columnsList[i].iloc[j]["Unnamed: 1"]])
    return NOKList
