from Domain.modules import analyzeKPI,getNOKreport


def justification_consolidation(numCells,numTechs,babysittingPath):

    listNOK = getNOKreport.consolidation(numCells,numTechs,babysittingPath)
    KPIoverview = set()

    listNOKchecked = []
    for i in range(len(listNOK)):
        KPIoverview.add(listNOK[i][1])
        match listNOK[i][1]:
            case '2G CDR CS (%)':
                # 3º NOK_i = analyzeKPI
                listNOKchecked.append(analyzeKPI.CDR(listNOK[i],"2G"))
            case '3G CDR CS (%)':
                listNOKchecked.append(analyzeKPI.CDR(listNOK[i],"3G"))
            case '4G CDR (VoLTE) (%)':
                listNOKchecked.append(analyzeKPI.CDR(listNOK[i],"4G_Voice"))
            case '4G_DCR_DATA ':
                listNOKchecked.append(analyzeKPI.CDR(listNOK[i],"4G_Packect"))
            case '2G CSSR CS (%)':
                listNOKchecked.append(analyzeKPI.CSSR_voice(listNOK[i],"2G"))
            case '3G CSSR CS (%)':
                listNOKchecked.append(analyzeKPI.CSSR_voice(listNOK[i],"3G"))
            case '4G CSSR CS (%)':
                listNOKchecked.append(analyzeKPI.CSSR_voice(listNOK[i],"4G"))
            case '2G Iniciated calls':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"2G"))
            case '3G Iniciated calls':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"3G"))
            case '4G Iniciated calls (VoLTE)':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"4G"))
            case '2G DL Data traffic (KB)':
                listNOKchecked.append(analyzeKPI.traffic_DL(listNOK[i],"2G"))
            case '2G UL Data traffic (KB)':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"2G"))
            case '3G DL Data traffic (KB)':
                pass
            case '3G UL Data traffic (KB)':
                pass
            case '4G DL Data traffic (MB)':
                listNOKchecked.append(analyzeKPI.traffic_DL(listNOK[i],"4G"))
            case '4G UL Data traffic (MB)':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"4G"))
            case 'Tput DL 4G >2Mbps':
                listNOKchecked.append(analyzeKPI.throughput_DL(listNOK[i],"4G"))
            case 'Tput UL 4G >500kbps':
                listNOKchecked.append(analyzeKPI.throughput_UL(listNOK[i],"4G"))
            case '2G ICMBand () ':
                listNOKchecked.append(analyzeKPI.interference(listNOK[i]))
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
                listNOKchecked.append(analyzeKPI.MIMO_rank2(listNOK[i]))
            case '4G MIMO (Rank4) (%)':
                listNOKchecked.append(analyzeKPI.MIMO_rank4(listNOK[i]))
            case '4G CSFB E2W':
                listNOKchecked.append(analyzeKPI.CSFB(listNOK[i]))
            case '4G CA in PCELL':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"primaryCell"))
            case '4G CA in SCELL':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"secondaryCell"))
            case '2G Speech disconnections':
                listNOKchecked.append(analyzeKPI.speech_disconnections(listNOK[i]))
            case '3G Calls ending in 2G (%)':
                listNOKchecked.append(analyzeKPI.calls_ending_3g2g(listNOK[i]))
            case '4G IntraLTE HOSR (including preparation) (%)':
                pass
            case '4G SRVCC HO Att':
                listNOKchecked.append(analyzeKPI.SRVCC(listNOK[i]))
            case "2G CSSR PS (%)":
                listNOKchecked.append(analyzeKPI.CSSR_data(listNOK[i],"2G"))
            case "3G CSSR PS (%)":
                listNOKchecked.append(analyzeKPI.CSSR_data(listNOK[i],"3G"))
            case "4G CSSR PS (%)":
                listNOKchecked.append(analyzeKPI.CSSR_data(listNOK[i],"4G"))

                
    return KPIoverview, listNOKchecked
          

def justification_expansion(numCells,numTechs,babysittingPath):
    
    # 1º getNOK
    listNOK = getNOKreport.expansion(numCells,numTechs,babysittingPath)
    KPIoverview = set()

    listNOKchecked = []
    # 2º type of NOK?
    for i in range(len(listNOK)):
        KPIoverview.add(listNOK[i][1])
        match listNOK[i][1]:
            case '4G_DCR_CS (VoLTE)':
                # 3º NOK_i = analyzeKPI
                listNOKchecked.append(analyzeKPI.CDR(listNOK[i],"4G_Voice"))
            case '4G CSSR CS (VoLTE)':
                pass
            case '4G_CSSR_PS_Success_Rate':
                pass
            case '5G_CSSR_PS_Success_Rate':
                pass
            case '4G VoLTE Iniciated calls':
                listNOKchecked.append(analyzeKPI.iniciated_calls(listNOK[i],"4G"))
            case '5G Iniciated PS calls':
                pass
            case '4G_Downlink_Traffic_Volume_MB':
                listNOKchecked.append(analyzeKPI.traffic_DL(listNOK[i],"4G"))
            case '4G_Uplink_Traffic_Volume_MB':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"4G"))
            case '5G_Downlink_Traffic_Volume_MB':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"5G"))
            case '5G_Uplink_Traffic_Volume_MB':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"5G"))
            case 'Interference 4G PUSCH UL (RSSI UL 4G) ':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"4G"))
            case 'Interference 4G PUSCH UL (RSSI UL 4G)':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"4G"))
            case 'Interference 5G UL (RSSI UL 5G) *':
                listNOKchecked.append(analyzeKPI.RSSI(listNOK[i],"5G"))
            case '4G_Availability_Cell_Rate_Hourly':
                listNOKchecked.append(analyzeKPI.availability(listNOK[i],"4G"))
            case '5G_Availability_Cell_Rate_Hourly':
                listNOKchecked.append(analyzeKPI.availability(listNOK[i],"5G"))
            case '4G_% MIMO':
                listNOKchecked.append(analyzeKPI.MIMO_rank2(listNOK[i]))
            case 'CSFB attempts (L.CSFB.E2W + L.CSFB.E2G)':
                listNOKchecked.append(analyzeKPI.CSFB(listNOK[i]))
            case 'CA in Primary Cell':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"primaryCell"))
            case 'CA in Secondary Cell':
                listNOKchecked.append(analyzeKPI.CA(listNOK[i],"secondaryCell"))
            case '5G: Intra-SgNB PSCell Change Success Rate':
                pass
            case 'TH DL / Maximo  TH DL Diario 4G  > 7 Mbps ':
                listNOKchecked.append(analyzeKPI.throughput_DL(listNOK[i],"4G"))
            case 'TH UL / TH UL 4G 0,5> Mbps':
                listNOKchecked.append(analyzeKPI.throughput_UL(listNOK[i],"4G"))
            case 'TDD TH DL 5G':
                KPIoverview.discard('TDD TH DL 5G')
            case 'TDD TH UL 5G':
                KPIoverview.discard('TDD TH UL 5G')
            case 'FDD TH DL 5G':
                pass
            case 'FDD TH UL 5G':
                pass
            case 'Maximo TH DL 5G':
                listNOKchecked.append(analyzeKPI.throughput_DL(listNOK[i],"5G"))
            case 'Maximo TH UL 5G':
                listNOKchecked.append(analyzeKPI.throughput_UL(listNOK[i],"5G"))
            case '5G SgNB_Addition_Success_Rate':
                pass
            case '5G Average User Number':
                pass
            case '5G RLC DL Traffic (GB)':
                listNOKchecked.append(analyzeKPI.traffic_DL(listNOK[i],"5G"))
            case '5G RLC UL Traffic (GB)':
                listNOKchecked.append(analyzeKPI.traffic_UL(listNOK[i],"5G"))
            case 'L.CSFB.E2W':
                listNOKchecked.append(analyzeKPI.CSFB(listNOK[i]))
            case 'Maximo  TH DL Diario 4G ':
                listNOKchecked.append(analyzeKPI.throughput_DL(listNOK[i],"4G"))
            case 'TH UL 4G':
                listNOKchecked.append(analyzeKPI.throughput_UL(listNOK[i],"4G"))
            case 'NR Throughput DL User':
                listNOKchecked.append(analyzeKPI.throughput_DL(listNOK[i],"5G"))
            case 'NR Throughput UL User':
                listNOKchecked.append(analyzeKPI.throughput_UL(listNOK[i],"5G"))

    listNOKchecked_no_none =[]
    for i in listNOKchecked:
        if i != None:
            listNOKchecked_no_none.append(i)

    return KPIoverview, listNOKchecked_no_none
