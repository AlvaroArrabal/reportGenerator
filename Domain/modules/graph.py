import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from modules import getQueryData


equivalent = {"2G CDR CS (%)":"2G_QF_DCR_Voice(%)",
                "2G CSSR CS (%)":"2G_QF_CSSR_Voice(%)",
                "2G CSSR PS (%)":"2G_QF_CSSR_Data(%)",
                "2G Iniciated calls":"2G_QF_Initiated_Calls(#)",
                "2G DL Data traffic (KB)":"2G_QF_DL_Data_Traffic(KB)",
                "2G UL Data traffic (KB)":"2G_QF_UL_Data_Traffic(KB)",
                "2G ICMBand () ":"2G_QF_ICMBand_(% Samples >3)(%)",
                "2G Cell Availability (%)":"2G_QF_Cell_Availability_Rate(%)",
                "2G Speech disconnections":"CELL.SPEECH.DISC.TIMES.NO.CIRCUIT.CHAN(Times)",
                "3G CDR CS (%)":"3G_QF_DCR_Voice(%)",
                "3G CSSR CS (%)":"3G_QF_CSSR_CS(%)",
                "3G CSSR PS (%)":"3G_QF_CSSR_PS(%)",
                "3G Iniciated calls":"3G_QF_Initiated_Calls(#)",
                "3G DL Data traffic (KB)":"3G_QF_DL_Data_Traffic(KB)",
                "3G UL Data traffic (KB)":"3G_QF_UL_Data_Traffic(KB)",
                "3G RTWP (dBm)":"3G_QF_RSSI_UL(dBm)",
                "3G Cell Availability (%)":"3G_QF_Cell_Availability_Hourly(%)",
                "3G Calls ending in 2G (%)":"3G_QF_Calls ending in 2G(%)",
                "TH DL (2G3G4G)":"User Throughput (Kbps)(kbit/s)",
                "TH UL (2G3G4G)":"3G_QF_User_HSUPA_Throughput(Kbps)",
                "4G CDR (VoLTE) (%)":"4G_QF_VoLTE_DCR(%)",
                "4G_DCR_DATA":"4G_QF_DCR_PS(%)",
                "4G CSSR (VoLTE) (%)":"4G_QF_VoLTE_CSSR(%)",
                "4G CSSR PS (%)":"4G_QF_CSSR_PS_ERAB(%)",
                "4G Iniciated calls (VoLTE)":"4G_QF_VoLTE_Initiated_Calls(#)",
                "4G DL Data traffic (MB)":"4G_QF_Downlink_Traffic_Volume(MB)",
                "4G UL Data traffic (MB)":"4G_QF_Uplink_Traffic_Volume(MB)",
                "4G Interference PUSCH (dBm)":"4G_QF_UL_PUSCH_Interference(dBm)",
                "4G Cell Availability (%)":"4G_QF_Cell_Availability_Rate_Hourly(%)",
                "4G MIMO (Rank2) ()":"4G_QF_RANK2_MIMO()",
                "4G MIMO (Rank4) ()":"4G_QF_RANK4_MIMO()",
                "4G CSFB E2W":"L.CSFB.E2W()",
                "4G CA in PCELL":"4G_QF_CA_Primary_Cell(%)",
                "4G CA in SCELL":"4G_QF_CA_Secondary_Cell(%)",
                "4G IntraLTE HOSR (including preparation) ()":"4G_QF_IntraLTE HOSR (including preparation)()",
                "4G SRVCC HO Att":"4G_QF_SRVCC HO Att(n)",
                "Tput DL 4G >2Mbps":"4G_QF_Throughput_DL(Mbps)",
                "Tput UL 4G >500kbps":"4G_QF_Throughput_UL(Mbps)"}

def create_graph(graphList):
    pos = 1
    fig = plt.figure(figsize=(12,10*len(graphList)))
    for i in graphList:
        if "2G" in i[1]:
            df = getQueryData.get2G(i[0])
        elif "3G" in i[1]:
            df = getQueryData.get3G(i[0])
        elif "4G" in i[1]:
            df = getQueryData.get4G(i[0])
    
        data = df.loc[:,["Date",equivalent[i[1]]]]
        data["Date"] = pd.to_datetime(data["Date"])

        ax = plt.subplot(len(graphList),1,pos)

        ax.plot(data["Date"], data[equivalent[i[1]]])
        pos += 1
        fig.autofmt_xdate(rotation=90)
        ax.set_xticks(data["Date"])
        xfmt = mdates.DateFormatter('%d/%m/%Y %H:%M:%S')
        ax.xaxis.set_major_formatter(xfmt)
        ax.grid()
        ax.set_title(i[0])
        ax.set_ylabel(i[1])
        ax.set_xlabel("Date")

    graphname = ".\\graphs\\" +  i[1] + ".png"

    fig.savefig(graphname)