import pandas as pd
import modules.getData
import time

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

def availability(NOK,tech):
    startTime = time.time()
    match tech:
        case "2G":
            df = modules.getData.get2G(NOK[0])
            data = df.loc[:,["Date","2G_QF_Cell_Availability_Rate(%)"]]
        case "3G":
            df = modules.getData.get3G(NOK[0])
            data = df.loc[:,["Date","3G_QF_Cell_Availability_Hourly(%)"]]
        case "4G":
            df = modules.getData.get4G(NOK[0])
            data = df.loc[:,["Date","4G_QF_UL_PUSCH_Interference(dBm)"]]
        case "5G":
            df = modules.getData.get5G(NOK[0])
            data = df.loc[:,["Date","5G_QF Cell Availability(%)"]]
    
    totalAvailability = []
    for i in range(len(data)):
        totalAvailability.append(data.iloc[i][1])

    average = sum(totalAvailability)/len(totalAvailability)
    print("--- %s seconds <availability> ---" % (time.time() - startTime))
    if average < 95:
        return [NOK[0],NOK[1],False]       # NOK
    else:
        return [NOK[0],NOK[1],True]       # OK
    

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

def RSSI(NOK,tech):
    startTime = time.time()

    match tech:
        case "3G":
            df = modules.getData.get3G(NOK[0])
            data = df.loc[:,["Date","VS.MeanRTWP(dBm)"]]
        case "4G":
            df = modules.getData.get4G(NOK[0])
            data = df.loc[:,["Date","4G_QF_UL_PUSCH_Interference(dBm)"]]
        case "5G":
            df = modules.getData.get5G(NOK[0])
            data = df.loc[:,["Date","5G_QF RSSI(dBm)"]]
    
    totalRssi = []
    for i in range(len(data)):
        hour = data.iloc[i][0][-5:]
        if hour in offPeakHours:
            totalRssi.append(data.iloc[i][1])
    
    average = sum(totalRssi)/len(totalRssi)
    print("--- %s seconds <PUSCH> ---" % (time.time() - startTime))
    if average > -114:
        return [NOK[0],NOK[1],False]       # NOK
    else:
        return [NOK[0],NOK[1],True]       # OK


