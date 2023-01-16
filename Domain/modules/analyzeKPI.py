import pandas as pd
import modules.getData

offPeakHours = ["01:00","02:00","03:00","04:00","05:00"]

def CDR():
    pass

def CSSR():
    pass

def iniciated_calls():
    pass

def throughput():
    pass

def interference():
    pass

def availability():
    pass

def MIMO_rank2():
    pass

def MIMO_rank4():
    pass

def CSFB():
    pass

def CA_pcell():
    pass

def CA_scell():
    pass

def intraLTEHosr ():
    pass

def SRVCC():
    pass

def PUSCH(NOK):

    df = modules.getData.get4G(NOK[0])

    data = df.loc[:,["Date","4G_QF_UL_PUSCH_Interference(dBm)"]]
    listPusch = []
    for i in range(len(data)):
        hour = data.iloc[i][0][-5:]
        if hour in offPeakHours:
            listPusch.append(data.iloc[i][1])
    
    average = sum(listPusch)/len(listPusch)

    if average > -114:
        return [NOK[0],False]       # NOK
    else:
        return [NOK[0],True]       # OK


