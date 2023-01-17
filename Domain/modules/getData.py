import pandas as pd
import os
currentPath = os.getcwd()
import warnings
import time


def getNOK_700(numCells,numTechs):
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

def getNOK_consolidation(numCells,numTechs):
    startTime = time.time()
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
                NOKList.append([columnsList[i].iloc[0,1] , columnsList[i].iloc[j]["Unnamed: 1"],columnsList[i].iloc[j][1]])
    print("--- %s seconds <getNOK_consolidation> ---" % (time.time() - startTime))
    return NOKList


def get2G(site):
    startTime = time.time()
    path2g = currentPath + "\\Data\\2g.xlsx"
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(path2g, engine="openpyxl")

    data =  df.groupby("Cell Name")
    print("--- %s seconds <get2G> ---" % (time.time() - startTime))
    return data.get_group(site)



def get3G(site):
    startTime = time.time()
    path3g = currentPath + "\\Data\\3g.xlsx"
    df = pd.read_excel(path3g,engine="openpyxl")

    data =  df.groupby("Cell Name")
    print("--- %s seconds <get3G> ---" % (time.time() - startTime))
    return data.get_group(site)


def get4G(site):
    startTime = time.time()
    path4g = currentPath + "\\Data\\4g.xlsx"
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(path4g, engine="openpyxl")

    data =  df.groupby("Cell Name")
    print("--- %s seconds <get4G> ---" % (time.time() - startTime))
    return data.get_group(site)


def get5G(site):
    path5g = currentPath + "\\Data\\5g.xlsx"
    df = pd.read_excel(path5g,engine="openpyxl")

    data =  df.groupby("Cell Name")

    return data.get_group(site)



