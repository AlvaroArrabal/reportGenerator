import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from Domain.modules import getQueryData



# { KPI : [ KPI_name_in_query , type of graph (config) , target (if necesary) ] }

# config: 
# 0 -> line graph without limits
# 1 -> bar graph
# 2 -> fill graph
# 3 -> line graph with limits
# 4 -> line graph with target

equivalent = {"2G CDR CS (%)":["2G_QF_DCR_Voice(%)",0],
                "2G CSSR CS (%)":["2G_QF_CSSR_Voice(%)",0],
                "2G CSSR PS (%)":["2G_QF_CSSR_Data(%)",0],
                "2G Iniciated calls":["2G_QF_Initiated_Calls(#)",1],
                "2G DL Data traffic (KB)":["2G_QF_DL_Data_Traffic(KB)",0],
                "2G UL Data traffic (KB)":["2G_QF_UL_Data_Traffic(KB)",0],
                "2G ICMBand () ":["2G_QF_ICMBand_(% Samples >3)(%)",3],
                "2G Cell Availability (%)":["2G_QF_Cell_Availability_Rate(%)",2],
                "2G Speech disconnections":["CELL.SPEECH.DISC.TIMES.NO.CIRCUIT.CHAN(Times)",0],
                "3G CDR CS (%)":["3G_QF_DCR_Voice(%)",0],
                "3G CSSR CS (%)":["3G_QF_CSSR_CS(%)",0],
                "3G CSSR PS (%)":["3G_QF_CSSR_PS(%)",0],
                "3G Iniciated calls":["3G_QF_Initiated_Calls(#)",1],
                "3G DL Data traffic (KB)":["3G_QF_DL_Data_Traffic(KB)",0],
                "3G UL Data traffic (KB)":["3G_QF_UL_Data_Traffic(KB)",0],
                "3G RTWP (dBm)":["UL RSSI(dBm)",4,-100],
                "3G Cell Availability (%)":["3G_QF_Cell_Availability_Hourly(%)",2],
                "3G Calls ending in 2G (%)":["3G_QF_Calls ending in 2G(%)",3],
                "TH DL (2G3G4G)":["User Throughput (Kbps)(kbit/s)",0],
                "TH UL (2G3G4G)":["3G_QF_User_HSUPA_Throughput(Kbps)",0],
                "4G CDR (VoLTE) (%)":["4G_QF_VoLTE_DCR(%)",0],
                "4G_DCR_DATA":["4G_QF_DCR_PS(%)",0],
                "4G CSSR (VoLTE) (%)":["4G_QF_VoLTE_CSSR(%)",0],
                "4G CSSR PS (%)":["4G_QF_CSSR_PS_ERAB(%)",0],
                "4G Iniciated calls (VoLTE)":["4G_QF_VoLTE_Initiated_Calls(#)",1],
                "4G DL Data traffic (MB)":["4G_QF_Downlink_Traffic_Volume(MB)",0],
                "4G UL Data traffic (MB)":["4G_QF_Uplink_Traffic_Volume(MB)",0],
                "4G Interference PUSCH (dBm)":["4G_QF_UL_PUSCH_Interference(dBm)",4,-114],
                "4G Cell Availability (%)":["4G_QF_Cell_Availability_Rate_Hourly(%)",2],
                "4G MIMO (Rank2) (%)":["4G_QF_MIMO_RANK2(%)",0],
                "4G MIMO (Rank4) (%)":["4G_QF_MIMO_RANK4(%)",0],
                "4G CSFB E2W":["L.CSFB.E2W()",1],
                "4G CA in PCELL":["4G_QF_CA_Primary_Cell(%)",0],
                "4G CA in SCELL":["4G_QF_CA_Secondary_Cell(%)",0],
                "4G IntraLTE HOSR (including preparation) ()":["4G_QF_IntraLTE HOSR (including preparation)()",0],
                "4G SRVCC HO Att":["SRVCC_Att(#)",1],
                "Tput DL 4G >2Mbps":["4G_QF_Throughput_DL(Mbps)",4,2],
                "Tput UL 4G >500kbps":["4G_QF_Throughput_UL(Mbps)",4,0.5],
                '4G_DCR_CS (VoLTE)':["4G_QF_VoLTE_DCR(%)",0],
                '4G CSSR CS (VoLTE)':["4G_QF_VoLTE_CSSR(%)",0],
                '4G_CSSR_PS_Success_Rate':["4G_QF_CSSR_PS_ERAB(%)",0],
                '5G_CSSR_PS_Success_Rate':[],
                '4G VoLTE Iniciated calls':["4G_QF_VoLTE_Initiated_Calls(#)",1],       
                '4G_Downlink_Traffic_Volume_MB':[],
                '4G_Uplink_Traffic_Volume_MB':[],
                '5G_Downlink_Traffic_Volume_MB':["5G_QF DL Traffic Volume(GB)",0],
                '5G_Uplink_Traffic_Volume_MB':["5G_QF UL Traffic Volume(GB)",0],
                'Interference 4G PUSCH UL (RSSI UL 4G) ':["4G_QF_UL_PUSCH_Interference(dBm)",4,-114],
                'Interference 4G PUSCH UL (RSSI UL 4G)':["4G_QF_UL_PUSCH_Interference(dBm)",4,-114],
                'Interference 5G UL (RSSI UL 5G) *':["5G_QF RSSI(dBm)",4,-114],
                '4G_Availability_Cell_Rate_Hourly':["4G_QF_Cell_Availability_Rate_Hourly(%)",2],
                '5G_Availability_Cell_Rate_Hourly':["5G_QF Cell Availability(%)",2],
                '4G_% MIMO':["4G_QF_RANK2_MIMO()",0],
                'CSFB attempts (L.CSFB.E2W + L.CSFB.E2G)':[],
                'CA in Primary Cell':["4G_QF_CA_Primary_Cell(%)",0],
                'CA in Secondary Cell':["4G_QF_CA_Secondary_Cell(%)",0],
                '5G: Intra-SgNB PSCell Change Success Rate' :[],
                'TH DL / Maximo  TH DL Diario 4G  > 7 Mbps ':["4G_QF_Throughput_DL(Mbps)",4,7],
                'TH UL / TH UL 4G 0,5> Mbps':["4G_QF_Throughput_UL(Mbps)",4,0.5],
                'FDD TH DL 5G':[],
                'FDD TH UL 5G':[],
                'Maximo TH DL 5G':["5G_QF DL Throughput Cell(Mbps)",0],
                'Maximo TH UL 5G':["5G_QF UL Throughput Cell(Mbps)",0],
                '5G SgNB_Addition_Success_Rate':[],               
                '5G Average User Number':[],              
                '5G RLC DL Traffic (GB)':["5G_QF DL Traffic Volume(GB)",0],
                '5G RLC UL Traffic (GB)':["5G_QF UL Traffic Volume(GB)",0],
                'L.CSFB.E2W':["L.CSFB.E2W()",1],
                'Maximo  TH DL Diario 4G ':["4G_QF_Throughput_DL(Mbps)",4,7],
                'TH UL 4G':["4G_QF_Throughput_UL(Mbps)",4,0.5],
                'NR Throughput DL User':["5G_QF DL Throughput Cell(Mbps)",0],
                'NR Throughput UL User':["5G_QF UL Throughput Cell(Mbps)",0]}

def create(graphList):
    pos = 1
    plt. rc ('xtick', labelsize = 4 )
    plt. rc ('ytick', labelsize = 4 )
    plt. rc ('axes', labelsize = 6 )
    plt. rc ('axes', titlesize = 6 )

    for i in graphList:
        fig = plt.figure(figsize=(8,3),dpi=200)
            
            
        if "2G" in i[1] and "3G" not in i[1]:
            df = getQueryData.get2G(i[0])
        elif "3G" in i[1]:
            df = getQueryData.get3G(i[0])
        elif "4G" in i[1]:
            df = getQueryData.get4G(i[0])
        elif "5G" in i[1]:
            df = getQueryData.get5G(i[0])

        if i[2] == "OK" or i[2] == "NOK":
        
            data = df.loc[:,["Date",equivalent[i[1]][0]]]
            
            data["Date"] = pd.to_datetime(data["Date"])

            ax = plt.subplot()
            # Type of graph
            if equivalent[i[1]][1] == 0:
                ax.plot(data["Date"], data[equivalent[i[1]][0]])

            elif equivalent[i[1]][1] == 1:
                ax.bar(data["Date"], data[equivalent[i[1]][0]],color='orange',width=0.03)

            elif equivalent[i[1]][1] == 2:
                ax.fill_between(data["Date"], data[equivalent[i[1]][0]],color='cornflowerblue',edgecolor='black')
                plt.ylim(0,110)

            elif equivalent[i[1]][1] == 3:
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                plt.ylim(0,110)
            elif equivalent[i[1]][1] == 4:
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                plt.axhline(equivalent[i[1]][2], color = "red", linewidth = 0.5, linestyle = "dashed")
                
            ax.grid(axis='y',linewidth=0.5)
            
        else:

            data = df.loc[:,["Date",equivalent[i[1]][0],i[2]]]
            
            data["Date"] = pd.to_datetime(data["Date"])
            
            ax = plt.subplot()
            if equivalent[i[1]][1] == 0:
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                ax.plot(data["Date"], data[i[2]])
                ax.grid()
            else:
                ax.bar(data["Date"], data[equivalent[i[1]][0]],color='orange',width=0.03)
                ax.bar(data["Date"], data[i[2]],color='blue',width=0.03)
            ax.legend([equivalent[i[1]][0],i[2]],fontsize=4)
        
        fig.autofmt_xdate(rotation=90)
        ax.set_xticks(data["Date"])
        xfmt = mdates.DateFormatter('%d/%m %H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
            
        ax.set_title(i[0])
        ax.set_ylabel(i[1])

        if i[1].find('>') == -1 and i[1].find('*') == -1:
            graphname = ".\\graphs\\" +  i[1] + "_" + str(pos) + ".png"
        elif i[1].find('>') != -1:
            element = i[1].replace('>','')
            graphname = ".\\graphs\\" +  element + "_" + str(pos) + ".png"
        elif i[1].find('*') != -1:
            element = i[1].replace('*','')
            graphname = ".\\graphs\\" +  element + "_" + str(pos) + ".png"
        pos += 1
        fig.savefig(graphname,dpi= 300)
        plt.close()

