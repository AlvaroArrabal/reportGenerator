import pandas as pd

gsmStructure = {}

def get2G(site):
    df = pd.read_excel("C:\\Users\\Alvaro.Arrabal\\Desktop\\IT\\babysittingPython\\Data\\2g.xlsx")

    data =  df.groupby("Cell Name")

    cell = data.get_group(site)

    pass
    for i in range(len(cell)):
        if cell.iloc[i]["2G_QF_Initiated_Calls(#)"] > 0:
            a = cell.iloc[i]["Date"]
            b = cell.iloc[i]["2G_QF_Initiated_Calls(#)"]
            print(f"{a} - {b}")

def get3G():
    pass


def get4G():
    pass

def get5G():
    pass

site = "M1990E2"
get2G(site)