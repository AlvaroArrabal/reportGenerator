from modules import analyzeKPI,graph,getNOKreport
import pandas as pd
import time


def justification_consolidation(numCells,numTechs):

    listNOK = getNOKreport.consolidation(numCells,numTechs)
    KPIoverview = set()

    startTime = time.time()
    listNOKchecked = []
    for i in range(len(listNOK)):
        KPIoverview.add(listNOK[i][1])

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
                listNOKchecked.append(analyzeKPI.interference(listNOK[i]))
            case '3G RTWP (dBm)':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"3G"))
            case '4G Interference PUSCH (dBm)':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"4G"))
                graph.create_graph(listNOK[i],"4G_QF_UL_PUSCH_Interference(dBm)")
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
                listNOKchecked.append(analyzeKPI.CSFB(listNOK[i]))
            case '4G CA in PCELL':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"primaryCell"))
            case '4G CA in SCELL':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"secondaryCell"))
            case '2G Speech disconnections':
                pass
            case '3G Calls ending in 2G (%)':
                pass
            case '4G IntraLTE HOSR (including preparation) (%)':
                pass
            case '4G SRVCC HO Att':
                listNOKchecked.append(analyzeKPI.SRVCC(listNOK[i]))
                pass
    print("--- %s seconds <justification_consolidation> ---" % (time.time() - startTime))
    return KPIoverview, listNOKchecked
          
a,b = justification_consolidation(3,4)

print(f"overview: {a}")
print(f"detail: {b}")

def justification_expansion(numCells,numTechs):
    
    # 1º getNOK
    listNOK = getNOKreport.expansion(numCells,numTechs)
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