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
# 5 -> for CSSR and CDR

equivalent = {"2G CDR CS (%)":["2G_QF_DCR_Voice(%)",5,"2G_QF_DCR_Voice_Attempts(#)"],
                "2G CSSR CS (%)":["2G_QF_CSSR_Voice(%)",5,"2G_QF_CSSR_Voice_Attempts(#)"],
                "2G CSSR PS (%)":["2G_QF_CSSR_Data(%)",5,"2G_QF_CSSR_Data_Attempts(#)"],
                "2G Iniciated calls":["2G_QF_Initiated_Calls(#)",1],
                "2G DL Data traffic (KB)":["2G_QF_DL_Data_Traffic(KB)",0],
                "2G UL Data traffic (KB)":["2G_QF_UL_Data_Traffic(KB)",0],
                "2G ICMBand () ":["2G_QF_ICMBand_(% Samples >3)(%)",3],
                "2G Cell Availability (%)":["2G_QF_Cell_Availability_Rate(%)",2],
                "2G Speech disconnections":["CELL.SPEECH.DISC.TIMES.NO.CIRCUIT.CHAN",0],
                "3G CDR CS (%)":["3G_QF_DCR_Voice(%)",3],
                "3G CSSR CS (%)":["3G_QF_CSSR_CS(%)",5,"3G_QF_CSSR_CS_Attempts(#)"],
                "3G CSSR PS (%)":["3G_QF_CSSR_PS(%)",5,"3G_QF_CSSR_PS_Attempts(#)"],
                "3G Iniciated calls":["3G_QF_Initiated_Calls(#)",1],
                "3G DL Data traffic (KB)":["3G_QF_DL_Data_Traffic(KB)",0],
                "3G UL Data traffic (KB)":["3G_QF_UL_Data_Traffic(KB)",0],
                "3G RTWP (dBm)":["UL RSSI(dBm)",4,-100],
                "3G Cell Availability (%)":["3G_QF_Cell_Availability_Hourly(%)",2],
                "3G Calls ending in 2G (%)":["3G_QF_Calls ending in 2G(%)",3],
                "TH DL (2G3G4G)":["User Throughput (Kbps)(kbit/s)",0],
                "TH UL (2G3G4G)":["3G_QF_User_HSUPA_Throughput(Kbps)",0],
                "4G CDR (VoLTE) (%)":["4G_QF_VoLTE_DCR(%)",5,"4G_QF_VoLTE_DCR_Attempts(#)"],
                "4G_DCR_DATA":["4G_QF_DCR_PS(%)",5,"4G_QF_DCR_PS_Attempt(#)"],
                "4G CSSR (VoLTE) (%)":["4G_QF_VoLTE_CSSR(%)",5,"4G_QF_VoLTE_CSSR_Attempts(#)"],
                "4G CSSR PS (%)":["4G_QF_CSSR_PS_ERAB(%)",5,"4G_QF_CSSR_PS_ERAB_Attempt(#)"],
                "4G Iniciated calls (VoLTE)":["4G_QF_VoLTE_Initiated_Calls(#)",1],
                "4G DL Data traffic (MB)":["4G_QF_Downlink_Traffic_Volume(MB)",0],
                "4G UL Data traffic (MB)":["4G_QF_Uplink_Traffic_Volume(MB)",0],
                "4G Interference PUSCH (dBm)":["4G_QF_UL_PUSCH_Interference(dBm)",4,-114],
                "4G Cell Availability (%)":["4G_QF_Cell_Availability_Rate_Hourly(%)",2],
                "4G MIMO (Rank2) (%)":["4G_QF_MIMO_RANK2(%)",0],
                "4G MIMO (Rank4) (%)":["4G_QF_MIMO_RANK4(%)",0],
                "4G CSFB E2W":["L.CSFB.PrepAtt",1],
                "4G CA in PCELL":["4G_QF_CA_Primary_Cell(%)",0],
                "4G CA in SCELL":["4G_QF_CA_Secondary_Cell(%)",0],
                "4G IntraLTE HOSR (including preparation) (%)":["4G_QF_IntraLTE HOSR (including preparation)(%)",3],
                "4G SRVCC HO Att":["SRVCC_Att(#)",1],
                "Tput DL 4G >2Mbps":["4G_QF_Throughput_DL(Mbps)",4,2],
                "Tput UL 4G >500kbps":["4G_QF_Throughput_UL(Mbps)",4,0.5],
                '4G_DCR_CS (VoLTE)':["4G_QF_VoLTE_DCR(%)",3],
                '4G CSSR CS (VoLTE)':["4G_QF_VoLTE_CSSR(%)",3],
                '4G_CSSR_PS_Success_Rate':["4G_QF_CSSR_PS_ERAB(%)",3],
                '5G_CSSR_PS_Success_Rate':["5GNR Setup Success Rate(%)",3],
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
                '4G_% MIMO':["4G_QF_MIMO_RANK2(%)",0],
                'CSFB attempts (L.CSFB.E2W + L.CSFB.E2G)':["4G_QF_CSFB_E2W_Attempts(#)",1],
                'CA in Primary Cell':["4G_QF_CA_Primary_Cell(%)",0],
                'CA in Secondary Cell':["4G_QF_CA_Secondary_Cell(%)",0],
                '5G: Intra-SgNB PSCell Change Success Rate':["5G_QF Intra-SgNB PSCell Change Success Rate(%)",3],
                'TH DL / Maximo  TH DL Diario 4G  > 7 Mbps ':["4G_QF_Throughput_DL(Mbps)",4,7],
                'TH UL / TH UL 4G 0,5> Mbps':["4G_QF_Throughput_UL(Mbps)",4,0.5],
                'FDD TH DL 5G':[],
                'FDD TH UL 5G':[],
                'Maximo TH DL 5G':["5G_QF DL Throughput Cell(Mbps)",0],
                'Maximo TH UL 5G':["5G_QF UL Throughput Cell(Mbps)",0],
                '5G SgNB_Addition_Success_Rate':["5GNR Setup Success Rate(%)",3],
                '5G Average User Number':["5G_QF Maximum User Number(#)",1],
                '5G RLC DL Traffic (GB)':["5G_QF DL Traffic Volume(GB)",0],
                '5G RLC UL Traffic (GB)':["5G_QF UL Traffic Volume(GB)",0],
                'L.CSFB.E2W':["L.CSFB.E2W()",1],
                'Maximo  TH DL Diario 4G ':["4G_QF_Throughput_DL(Mbps)",4,7],
                'TH UL 4G':["4G_QF_Throughput_UL(Mbps)",4,0.5],
                'NR Throughput DL User':["5G_QF DL Throughput Cell(Mbps)",0],
                'NR Throughput UL User':["5G_QF UL Throughput Cell(Mbps)",0],
                '5G Iniciated PS calls':["5G_QF Maximum User Number(#)",1],
                '5G_DCR_DATA (*)':["5G_QF SgNB-Triggered Abnormal SgNB Release Rate(%)",3],
                '4G_DCR_DATA ':["4G_QF_DCR_PS(%)",3],
                '5G Inter-SgNB PSCell Change Success Rate':["5G_QF Inter-SgNB PSCell Change Success Rate(%)",3],
            }

def create(graphList):
    pos = 1
    plt. rc ('xtick', labelsize = 4 )
    plt. rc ('ytick', labelsize = 4 )
    plt. rc ('axes', labelsize = 6 )
    plt. rc ('axes', titlesize = 6 )

    for i in graphList:
        fig = plt.figure(figsize=(8,3),dpi=200)
            
        try:
            df = getQueryData.get2G(i[0])
        except:
            try:
                df = getQueryData.get3G(i[0])
            except:
                try:
                    df = getQueryData.get4G(i[0])
                except:
                    try:
                        df = getQueryData.get5G(i[0])
                    except:
                        print("No se encuentra KPI")

        if i[2] == "OK" or i[2] == "NOK":
        
            

            ax = plt.subplot()
            # Type of graph
            if equivalent[i[1]][1] == 0:
                data = df.loc[:,["Date",equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])

                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                plt.ylim(bottom=0)

            elif equivalent[i[1]][1] == 1:
                data = df.loc[:,["Date",equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])
                
                ax.bar(data["Date"], data[equivalent[i[1]][0]],color='orange',width=0.03)

            elif equivalent[i[1]][1] == 2:
                data = df.loc[:,["Date",equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])
                
                ax.fill_between(data["Date"], data[equivalent[i[1]][0]],color='cornflowerblue',edgecolor='black')
                plt.ylim(0,10)

            elif equivalent[i[1]][1] == 3:
                data = df.loc[:,["Date",equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])
                
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                plt.ylim(0,110)
            elif equivalent[i[1]][1] == 4:
                data = df.loc[:,["Date",equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])
                
                ax.plot(data["Date"], data[equivalent[i[1]][0]])
                plt.axhline(equivalent[i[1]][2], color = "red", linewidth = 0.5, linestyle = "dashed")
            elif equivalent[i[1]][1] == 5:
                data = df.loc[:,["Date",equivalent[i[1]][2],equivalent[i[1]][0]]]
                data["Date"] = pd.to_datetime(data["Date"])

                ax.bar(data["Date"], data[equivalent[i[1]][2]],color='orange',width=0.03)
                ax_twin = ax.twinx()
                ax_twin.plot(data["Date"], data[equivalent[i[1]][0]])
                ax_twin.set_ylabel(equivalent[i[1]][0])
                plt.ylim(bottom=0)
                
                
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
        
        if equivalent[i[1]][1] != 5:
            ax.set_ylabel(i[1])
        else:
            ax.set_ylabel(equivalent[i[1]][2])

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

