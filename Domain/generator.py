from modules import getData,analyzeKPI
import pandas as pd
import time



def justification_consolidation(numCells,numTechs):

    listNOK = getData.getNOK_consolidation(numCells,numTechs)
    startTime = time.time()
    listNOKchecked = []
    for i in range(len(listNOK)):
        match listNOK[i][1]:
            case '2G CDR CS (%)':
                # 3º NOK_i = analyzeKPI
                pass
            case '3G CDR CS (%)':
                pass
            case '4G CDR CS (%)':
                pass
            case '4G_DCR_DATA ':
                pass
            case '2G CSSR CS (%)':
                pass
            case '3G CSSR CS (%)':
                pass
            case '4G CSSR CS (%)':
                pass
            case '2G Iniciated calls':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"2G"))
            case '3G Iniciated calls':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"3G"))
            case '4G Iniciated calls (VoLTE)':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"4G"))
            case '2G DL Data traffic (KB)':
                pass
            case '2G UL Data traffic (KB)':
                pass
            case '3G DL Data traffic (KB)':
                pass
            case '3G UL Data traffic (KB)':
                pass
            case '4G DL Data traffic (MB)':
                pass
            case '4G UL Data traffic (MB)':
                pass
            case 'Tput DL 4G >2Mbps':
                pass
            case 'Tput UL 4G >500kbps':
                pass
            case 'Tput UL 4G >500kbps':
                pass
            case '2G ICMBand () ':
                pass
            case '3G RTWP (dBm)':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"3G"))
            case '4G Interference PUSCH (dBm)':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"4G"))
            case '2G Cell Availability (%)':
                listNOKchecked.append(analyzeKPI.availability(listNOK[i],"2G"))
            case '3G Cell Availability (%)':
                listNOKchecked.append(analyzeKPI.availability(listNOK[i],"3G"))
            case '4G Cell Availability (%)':
                listNOKchecked.append(analyzeKPI.availability(listNOK[i],"4G"))
            case '4G MIMO (Rank2) (%)':
                pass
            case '4G MIMO (Rank4) (%)':
                pass
            case '4G CSFB E2W':
                pass
            case '4G CA in PCELL':
                pass
            case '4G CA in SCELL':
                pass
            case '2G Speech disconnections':
                pass
            case '3G Calls ending in 2G (%)':
                pass
            case '4G IntraLTE HOSR (including preparation) (%)':
                pass
            case '4G SRVCC HO Att':
                pass
    print("--- %s seconds <justification_consolidation> ---" % (time.time() - startTime))
    return listNOKchecked
          
a = justification_consolidation(3,4)

print(a)

def justification_700(numCells,numTechs):
    
    # 1º getNOK
    listNOK = getData.getNOK_700(numCells,numTechs)
    print(listNOK)
    
    # 2º type of NOK?
    for i in range(len(listNOK)):
        match listNOK[i][1]:
            case '5G RLC UL Traffic (GB)':
                # 3º NOK_i = analyzeKPI
                print("RSSI")
            case 'Interference 4G PUSCH UL (RSSI UL 4G)':
                print("PUSCH")



def word():
    pass