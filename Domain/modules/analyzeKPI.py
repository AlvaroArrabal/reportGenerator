import Domain.modules.getQueryData


offPeakHours = ["01:00","02:00","03:00","04:00","05:00"]

def CDR(NOK,tech):
    # check for multiple peaks or a single peak (or two)
    match tech:
        case "2G":
            df = Domain.modules.getQueryData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_DCR_Voice(%)"]]
        case "3G":
            df = Domain.modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_DCR_Voice(%)"]]
        case "4G_Voice":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_VoLTE_DCR(%)"]]
        case "4G_Packect":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_DCR_PS(%)"]]
    
    cont = 0
    for i in range(len(data)):
        if type(data.iloc[i][0]) != str and data.iloc[i][0] > 15:
            cont += 1
    if cont > 3:
        return [NOK[0],NOK[1],"NOK"]     # NOK
    else:
        return [NOK[0],NOK[1],"OK"]      # OK

def CSSR():
    pass

def calls_ending_3g2g(NOK):
    df = Domain.modules.getQueryData.get3G(NOK[0])
    data = df.loc[:,["3G_QF_Calls ending in 2G(%)"]]

    cont = 0
    firstHours = 0
    for i in range(len(data)):
        if type(data.iloc[i][0]) != str and firstHours > 8 and data.iloc[i][0] > 10:
            cont += 1
        firstHours += 1
    if cont > 0:
        return [NOK[0],NOK[1],"NOK"]     # NOK
    else:
        return [NOK[0],NOK[1],"OK"]      # OK

def iniciated_calls(NOK,tech):

    match tech:
        case "2G":
            df = Domain.modules.getQueryData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Established_Calls(#)"]]
            total = data["2G_QF_Established_Calls(#)"].sum()
        case "3G":
            df = Domain.modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Initiated_Calls(#)"]]
            total = data["3G_QF_Initiated_Calls(#)"].sum()
        case "4G":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_VoLTE_Initiated_Calls(#)"]]
            total = data["4G_QF_VoLTE_Initiated_Calls(#)"].sum()
    

    if total > 0:
        return [NOK[0],NOK[1],"OK"]       # OK
    else:
        return [NOK[0],NOK[1],"NOK"]      # NOK

def throughput(NOK,tech):
    match tech:
        case "2G":
            pass
        case "3G":
            pass
        case "4G":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_Throughput_UL(Mbps)"]]
             
    cont =0
    for i in range(len(data)):
        if type(data.iloc[i][0]) != str and data.iloc[i][0] >= 0.5:
            cont += 1
        
    if cont < 5:
        return [NOK[0],NOK[1],"NOK"]        # NOK
    else:
        return [NOK[0],NOK[1],"OK"]         # OK
    

def interference(NOK):
    # For ICM Band in 2G

    df = Domain.modules.getQueryData.get2G(NOK[0])
    data = df.loc[:,["Date","2G_QF_ICMBand_(% Samples >3)(%)"]]

    totalRssi = []
    for i in range(len(data)):
        hour = data.iloc[i][0][-5:]
        if hour in offPeakHours:
            totalRssi.append(data.iloc[i][1])
    
    average = sum(totalRssi)/len(totalRssi)
    if average > 2:
        return [NOK[0],NOK[1],"NOK"]        # NOK
    else:
        return [NOK[0],NOK[1],"OK"]         # OK
    

def availability(NOK,tech):
    match tech:
        case "2G":
            df = Domain.modules.getQueryData.get2G(NOK[0])
            data = df.loc[:,["2G_QF_Cell_Availability_Rate(%)"]]
            average = data["2G_QF_Cell_Availability_Rate(%)"].mean()
            
        case "3G":
            df = Domain.modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["3G_QF_Cell_Availability_Hourly(%)"]]
            average = data["3G_QF_Cell_Availability_Hourly(%)"].mean()
        case "4G":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_Cell_Availability_Rate_Hourly(%)"]]
            average = data["4G_QF_Cell_Availability_Rate_Hourly(%)"].mean()
        case "5G":
            df = Domain.modules.getQueryData.get5G(NOK[0])
            data = df.loc[:,["5G_QF Cell Availability(%)"]]
            average = data["5G_QF Cell Availability(%)"].mean()
    
    if average < 95:
        return [NOK[0],NOK[1],"NOK"]       # NOK
    else:
        return [NOK[0],NOK[1],"OK"]       # OK
    

def MIMO_rank2(NOK):

    df = Domain.modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_MIMO_RANK2(%)"]]
    average = data["4G_QF_MIMO_RANK2(%)"].mean()

    if average < 10:
        return [NOK[0],NOK[1],"NOK"]       # NOK
    else:
        return [NOK[0],NOK[1],"OK"]       # OK

def MIMO_rank4(NOK):
    df = Domain.modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_MIMO_RANK4(%)"]]
    average = data["4G_QF_MIMO_RANK4(%)"].mean()

    if average < 10:
        return [NOK[0],NOK[1],"NOK"]       # NOK
    else:
        return [NOK[0],NOK[1],"OK"]       # OK

def CSFB(NOK):

    df = Domain.modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["4G_QF_CSFB_E2W_Attempts(#)"]]
    total = data["4G_QF_CSFB_E2W_Attempts(#)"].sum()
    
    if total > 0:
        return [NOK[0],NOK[1],"OK"]       # OK
    else:
        return [NOK[0],NOK[1],"NOK"]      # NOK

def CA(NOK,num):

    match num:
        case "primaryCell":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_CA_Primary_Cell(%)"]]
            total = data["4G_QF_CA_Primary_Cell(%)"].sum()
        case "secondaryCell":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["4G_QF_CA_Secondary_Cell(%)"]]
            total = data["4G_QF_CA_Secondary_Cell(%)"].sum()
    
    if total > 0:
        return [NOK[0],NOK[1],"OK"]       # OK
    else:
        return [NOK[0],NOK[1],"NOK"]      # NOK


def intraLTEHosr ():
    pass

def SRVCC(NOK):

    df = Domain.modules.getQueryData.get4G(NOK[0])
    data = df.loc[:,["Date","SRVCC_Succ(#)","4G_QF_VoLTE_Initiated_Calls(#)"]]

    peakSRVCC = data["SRVCC_Succ(#)"].max()

    if peakSRVCC > 0:
        return [NOK[0],NOK[1],"OK"]         # OK
    else:
        peakCalls = data["4G_QF_VoLTE_Initiated_Calls(#)"].max()

        if peakCalls > 15:
            return [NOK[0],NOK[1],"NOK"]        # NOK
        else:
            return [NOK[0],NOK[1],"4G_QF_VoLTE_Initiated_Calls(#)"]         # OK

def RSSI(NOK,tech):

    match tech:
        case "3G":
            df = Domain.modules.getQueryData.get3G(NOK[0])
            data = df.loc[:,["Date","3G_QF_RSSI_UL(dBm)"]]
            target = -100
        case "4G":
            df = Domain.modules.getQueryData.get4G(NOK[0])
            data = df.loc[:,["Date","4G_QF_UL_PUSCH_Interference(dBm)"]]
            target = -113
        case "5G":
            df = Domain.modules.getQueryData.get5G(NOK[0])
            data = df.loc[:,["Date","5G_QF RSSI(dBm)"]]
            target = -113
    
    totalRssi = []
    for i in range(len(data)):
        
        hour = data.iloc[i][0][-5:]
        
        if hour in offPeakHours and type(data.iloc[i][1]) != str:
            totalRssi.append(data.iloc[i][1])

    average = sum(totalRssi)/len(totalRssi)
    if average > target:
        return [NOK[0],NOK[1],"NOK"]        # NOK
    else:
        return [NOK[0],NOK[1],"OK"]         # OK


