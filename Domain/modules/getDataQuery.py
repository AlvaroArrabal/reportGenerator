import pandas as pd

gsmStructure = {}

def get2G(site):
    df = pd.read_excel("C:\\Users\\Alvaro.Arrabal\\Desktop\\IT\\babysittingPython\\Data\\2g.xlsx")

    data =  df.groupby("Cell Name")

    avalilability = data.get_group(site)["2G_QF_Cell_Availability_Rate(%)"].tolist()
    dropVoz = data.get_group(site)["2G_QF_DCR_Voice(%)"].tolist()
    print(dropVoz)
    

def get3G():
    pass


def get4G():
    pass

def get5G():
    pass

site = "M1990E2"
get2G(site)