import pandas as pd
import modules.getQueryData


offPeakHours = ["01:00","02:00","03:00","04:00","05:00"]

def CDR():
    # check for multiple peaks or a single peak (or two)
    pass

def CSSR():
    pass

def calls_ending_3g2g():
    pass

def iniciated_calls(NOK,tech):

    match tech:
        case "2G":
            df = modules.getQueryData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Established_Calls(#)"]]
            total = data["2G_QF_Established_Calls(#)"].sum()
        case "3G":
            df = modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Initiated_Calls(#)"]]
            total = data["3G_QF_Initiated_Calls(#)"].sum()
        case "4G":
            df = modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_VoLTE_Initiated_Calls(#)"]]
            total = data["4G_QF_VoLTE_Initiated_Calls(#)"].sum()
    

    if total > 0:
        return [NOK[0],NOK[1],True]       # OK
    else:
        return [NOK[0],NOK[1],False]      # NOK

def throughput():
    pass

def interference(NOK):
    # For ICM Band in 2G

    df = modules.getQueryData.get2G(NOK[0])
    data = df.loc[:,["Date","2G_QF_ICMBand_(% Samples >3)(%)"]]

    totalRssi = []
    for i in range(len(data)):
        hour = data.iloc[i][0][-5:]
        if hour in offPeakHours:
            totalRssi.append(data.iloc[i][1])
    
    average = sum(totalRssi)/len(totalRssi)
    if average > 2:
        return [NOK[0],NOK[1],False]        # NOK
    else:
        return [NOK[0],NOK[1],True]         # OK
    

def availability(NOK,tech):
    match tech:
        case "2G":
            df = modules.getQueryData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Cell_Availability_Rate(%)"]]
            average = data["2G_QF_Cell_Availability_Rate(%)"].mean()
            
        case "3G":
            df = modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Cell_Availability_Hourly(%)"]]
            average = data["3G_QF_Cell_Availability_Hourly(%)"].mean()
        case "4G":
            df = modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_Cell_Availability_Rate_Hourly(%)"]]
            average = data["4G_QF_Cell_Availability_Rate_Hourly(%)"].mean()
        case "5G":
            df = modules.getQueryData.get5G(NOK[0])
            data = df.loc[:,["5G_QF Cell Availability(%)"]]
            average = data["5G_QF Cell Availability(%)"].mean()
    
    if average < 95:
        return [NOK[0],NOK[1],False]       # NOK
    else:
        return [NOK[0],NOK[1],True]       # OK
    

def MIMO_rank2(NOK):

    df = modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_MIMO_RANK2(%)"]]
    average = data["4G_QF_MIMO_RANK2(%)"].mean()

    if average < 10:
        return [NOK[0],NOK[1],False]       # NOK
    else:
        return [NOK[0],NOK[1],True]       # OK

def MIMO_rank4(NOK):
    df = modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_MIMO_RANK4(%)"]]
    average = data["4G_QF_MIMO_RANK4(%)"].mean()

    if average < 10:
        return [NOK[0],NOK[1],False]       # NOK
    else:
        return [NOK[0],NOK[1],True]       # OK

def CSFB(NOK):

    df = modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_CSFB_E2W_Attempts(#)"]]
    total = data["4G_QF_CSFB_E2W_Attempts(#)"].sum()
    
    if total > 0:
        return [NOK[0],NOK[1],True]       # OK
    else:
        return [NOK[0],NOK[1],False]      # NOK

def CA(NOK,num):

    match num:
        case "primaryCell":
            df = modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_CA_Primary_Cell(%)"]]
            total = data["4G_QF_CA_Primary_Cell(%)"].sum()
        case "secondaryCell":
            df = modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_CA_Secondary_Cell(%)"]]
            total = data["4G_QF_CA_Secondary_Cell(%)"].sum()
    
    if total > 0:
        return [NOK[0],NOK[1],True]       # OK
    else:
        return [NOK[0],NOK[1],False]      # NOK


def intraLTEHosr ():
    pass

def SRVCC(NOK):

    df = modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["Date","SRVCC_Succ(#)","4G_QF_VoLTE_Initiated_Calls(#)"]]

    peakSRVCC = data["SRVCC_Succ(#)"].max()

    if peakSRVCC > 0:
        return [NOK[0],NOK[1],True]         # OK
    else:
        peakCalls = data["4G_QF_VoLTE_Initiated_Calls(#)"].max()

        if peakCalls > 15:
            return [NOK[0],NOK[1],False]        # NOK
        else:
            return [NOK[0],NOK[1],True]         # OK

def RSSI(NOK,tech):

    match tech:
        case "3G":
            df = modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["Date","3G_QF_RSSI_UL(dBm)"]]
        case "4G":
            df = modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["Date","4G_QF_UL_PUSCH_Interference(dBm)"]]
        case "5G":
            df = modules.getQueryData.get5G(NOK[0])
            data = df.loc[:,["Date","5G_QF RSSI(dBm)"]]
    
    totalRssi = []
    for i in range(len(data)):
        hour = data.iloc[i][0][-5:]
        if hour in offPeakHours:
            totalRssi.append(data.iloc[i][1])
    
    average = sum(totalRssi)/len(totalRssi)
    if average > -114:
        return [NOK[0],NOK[1],False]        # NOK
    else:
        return [NOK[0],NOK[1],True]         # OK


