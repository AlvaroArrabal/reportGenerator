import pandas as pd
import os
currentPath = os.getcwd()
import warnings



def get2G(site):
    
    path2g = currentPath + "\\Data\\2g.xlsx"
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(path2g, engine="openpyxl")

    data =  df.groupby("Cell Name")
    
    return data.get_group(site)



def get3G(site):
    
    path3g = currentPath + "\\Data\\3g.xlsx"
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(path3g, engine="openpyxl")

    data =  df.groupby("Cell Name")
    
    return data.get_group(site)


def get4G(site):
    
    path4g = currentPath + "\\Data\\4g.xlsx"
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        df = pd.read_excel(path4g, engine="openpyxl")

    data =  df.groupby("Cell Name")
    
    return data.get_group(site)


def get5G(site):
    path5g = currentPath + "\\Data\\5g.xlsx"
    df = pd.read_excel(path5g,engine="openpyxl")

    data =  df.groupby("Cell Name")

    return data.get_group(site)



