import pandas as pd
import modules.getData
import time

offPeakHours = ["01:00","02:00","03:00","04:00","05:00"]

def CDR():
    pass

def CSSR():
    pass

def iniciated_calls(NOK,tech):
    startTime = time.time()
    match tech:
        case "2G":
            df = modules.getData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Established_Calls(#)"]]
            total = data["2G_QF_Established_Calls(#)"].sum()
        case "3G":
            df = modules.getData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Initiated_Calls(#)"]]
            total = data["3G_QF_Initiated_Calls(#)"].sum()
        case "4G":
            df = modules.getData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_VoLTE_Initiated_Calls(#)"]]
            total = data["4G_QF_VoLTE_Initiated_Calls(#)"].sum()
    
    print("--- %s seconds <iniciated_calls> ---" % (time.time() - startTime))
    if total > 0:
        return [NOK[0],NOK[1],True]       # OK
    else:
        return [NOK[0],NOK[1],False]      # NOK

def throughput():
    pass

def interference():
    pass

def availability(NOK,tech):
    startTime = time.time()
    match tech:
        case "2G":
            df = modules.getData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Cell_Availability_Rate(%)"]]
            average = data["2G_QF_Cell_Availability_Rate(%)"].mean()
            
        case "3G":
            df = modules.getData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Cell_Availability_Hourly(%)"]]
            average = data["3G_QF_Cell_Availability_Hourly(%)"].mean()
        case "4G":
            df = modules.getData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_Cell_Availability_Rate_Hourly(%)"]]
            average = data["4G_QF_Cell_Availability_Rate_Hourly(%)"].mean()
        case "5G":
            df = modules.getData.get5G(NOK[0])
            data = df.loc[:,["5G_QF Cell Availability(%)"]]
            average = data["5G_QF Cell Availability(%)"].mean()
    
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


