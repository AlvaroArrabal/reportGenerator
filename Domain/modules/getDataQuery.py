import pandas as pd


def get2G():
    df = pd.read_excel("C:\\Users\\Alvaro.Arrabal\\Desktop\\IT\\babysittingPython\\Data\\2g.xlsx")

    data =  df.groupby("Cell Name").agg({"2G_QF_Cell_Availability_Rate(%)":lambda x: list(x),
                                        "CELL.SPEECH.DISC.TIMES.NO.CIRCUIT.CHAN":lambda x: list(x),
                                        "2G_QF_DCR_Voice(%)":lambda x: list(x),
                                        "2G_QF_CSSR_Data(%)":lambda x: list(x),
                                        "2G_QF_CSSR_Voice(%)":lambda x: list(x),
                                        "2G_QF_Initiated_Calls(#)":lambda x: list(x),
                                        "2G_QF_ICMBand_(% Samples >3)(%)":lambda x: list(x),
                                        "2G_QF_DL_Data_Traffic(kB)":lambda x: list(x),
                                        "2G_QF_UL_Data_Traffic(kB)":lambda x: list(x),}
                                        )
    
    
    
    
    
    
    
    
    

def get3G():
    pass


def get4G():
    pass

def get5G():
    pass


get2G()