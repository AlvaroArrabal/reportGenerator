import pandas as pd
import glob
import warnings
import numpy as np


def get2G(site):
    for file in glob.glob("Data/*.xlsx"):
        if 'GSM' in file:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                df = pd.read_excel(file, engine="openpyxl")
            df = df.replace({"/0": 0})
            df = df.replace({"-": np.nan})
            data =  df.groupby("Cell Name")
    
    return data.get_group(site)



def get3G(site):
    for file in glob.glob("Data/*.xlsx"):
        if 'UMTS' in file:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                df = pd.read_excel(file, engine="openpyxl")
    df = df.replace({"/0": 0})
    df = df.replace({"-": np.nan})
    data =  df.groupby("Cell Name")
    
    return data.get_group(site)


def get4G(site):
    for file in glob.glob("Data/*.xlsx"):
        if 'LTE' in file:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                df = pd.read_excel(file, engine="openpyxl")
    df = df.replace({"/0": 0})
    df = df.replace({"-": np.nan})
    data =  df.groupby("Cell Name")
    
    return data.get_group(site)


def get5G(site):
    for file in glob.glob("Data/*.xlsx"):
        if 'NR' in file:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                df = pd.read_excel(file, engine="openpyxl")
    df = df.replace({"/0": 0})
    df = df.replace({"-": np.nan})
    data =  df.groupby("Cell Name")

    return data.get_group(site)



