import pandas as pd
import os

currentPath = os.getcwd()

def getNOK(numCells,numTechs):
    pathNOK = currentPath + "\\Data\\Babysitting.xlsx"
    df = pd.read_excel(pathNOK)

    columns = []

    for i in range(0,numCells*numTechs*2,2): 
        columns.append([i+5, i+6,"Unnamed: " + str(i+6)])

    columnsList = []

    for i in columns:
        columnsList.append(df.iloc[:,[3,i[0],i[1]]])
        
    NOKList = []

    for i in range(len(columnsList)):
        for j in range(len(columnsList[i])):
            if columnsList[i].iloc[j][columns[i][2]] == "NOK":
                NOKList.append(columnsList[i].iloc[j]["Unnamed: 3"])
                

def get2G(site):
    path2g = currentPath + "\\Data\\2g.xlsx"
    df = pd.read_excel(path2g)

    data =  df.groupby("Cell Name")

    return data.get_group(site)


def get3G(site):
    path3g = currentPath + "\\Data\\3g.xlsx"
    df = pd.read_excel(path3g)

    data =  df.groupby("Cell Name")

    return data.get_group(site)


def get4G(site):
    path4g = currentPath + "\\Data\\4g.xlsx"
    df = pd.read_excel(path4g)

    data =  df.groupby("Cell Name")

    return data.get_group(site)

def get5G(site):
    path5g = currentPath + "\\Data\\5g.xlsx"
    df = pd.read_excel(path5g)

    data =  df.groupby("Cell Name")

    return data.get_group(site)



