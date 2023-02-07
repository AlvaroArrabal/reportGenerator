import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from Domain.modules import getQueryData

# config: 
# 0 -> line graph without limits
# 1 -> bar graph
# 2 -> fill graph
# 3 -> line graph with limits

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
                "3G RTWP (dBm)":["3G_QF_RSSI_UL(dBm)",0],
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
                "4G Interference PUSCH (dBm)":["4G_QF_UL_PUSCH_Interference(dBm)",0],
                "4G Cell Availability (%)":["4G_QF_Cell_Availability_Rate_Hourly(%)",2],
                "4G MIMO (Rank2) ()":["4G_QF_RANK2_MIMO()",0],
                "4G MIMO (Rank4) ()":["4G_QF_RANK4_MIMO()",0],
                "4G CSFB E2W":["L.CSFB.E2W()",1],
                "4G CA in PCELL":["4G_QF_CA_Primary_Cell(%)",0],
                "4G CA in SCELL":["4G_QF_CA_Secondary_Cell(%)",0],
                "4G IntraLTE HOSR (including preparation) ()":["4G_QF_IntraLTE HOSR (including preparation)()",0],
                "4G SRVCC HO Att":["SRVCC_Succ(#)",1],
                "Tput DL 4G >2Mbps":["4G_QF_Throughput_DL(Mbps)",0],
                "Tput UL 4G >500kbps":["4G_QF_Throughput_UL(Mbps)",0]}

def create_graph(graphList):
    pos = 1
    plt. rc ('xtick', labelsize = 4 )
    plt. rc ('ytick', labelsize = 4 )
    plt. rc ('axes', labelsize = 6 )
    plt. rc ('axes', titlesize = 6 )

    for i in graphList:

        if i[2] == "OK" or i[2] == "NOK":
            fig = plt.figure(figsize=(8,3),dpi=200)
            
            
            if "2G" in i[1] and "3G" not in i[1]:
                df = getQueryData.get2G(i[0])
            elif "3G" in i[1]:
                df = getQueryData.get3G(i[0])
            elif "4G" in i[1]:
                df = getQueryData.get4G(i[0])
        
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

            ax.grid(axis='y',linewidth=0.5)
            fig.autofmt_xdate(rotation=90)
            ax.set_xticks(data["Date"])
            xfmt = mdates.DateFormatter('%d/%m %H:%M:%S')
            ax.xaxis.set_major_formatter(xfmt)
            
            ax.set_title(i[0])
            ax.set_ylabel(i[1])

            graphname = ".\\Graphs\\" +  i[1] + "_" + str(pos) + ".png"
            pos += 1
            fig.savefig(graphname,dpi= 300)
        else:
            fig = plt.figure(figsize=(8,3),dpi=200)
            
            
            if "2G" in i[1] and "3G" not in i[1]:
                df = getQueryData.get2G(i[0])
            elif "3G" in i[1]:
                df = getQueryData.get3G(i[0])
            elif "4G" in i[1]:
                df = getQueryData.get4G(i[0])


            data = df.loc[:,["Date",equivalent[i[1]][0],i[2]]]
            data["Date"] = pd.to_datetime(data["Date"])
            
            ax = plt.subplot()
            if equivalent[i[1]][1] == 0:
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
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

            graphname = ".\\graphs\\" +  i[1] + "_" + str(pos) + ".png"
            pos += 1
            fig.savefig(graphname,dpi= 300)

