import pandas as pd

def getNOK(numCells,numTechs):
    df = pd.read_excel("C:\\Users\\Alvaro.Arrabal\\Desktop\\IT\\babysittingPython\\Data\\babysitting.xlsx")

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
                

gsmStructure = {}

def get2G(site):
    df = pd.read_excel("C:\\Users\\Alvaro.Arrabal\\Desktop\\IT\\babysittingPython\\Data\\2g.xlsx")

    data =  df.groupby("Cell Name")

    return data.get_group(site)


def get3G():
    pass


def get4G():
    pass

def get5G():
    pass
