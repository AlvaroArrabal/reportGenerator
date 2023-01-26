import pandas as pd
import os
currentPath = os.getcwd()
import warnings
import time


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



