from docx import Document
from docx.shared import Cm
import time
# 'KPI':['OK','NOK']

dic = { "2G CDR CS (%)":['',''],
        "2G CSSR CS (%)":['',''],
        "2G CSSR PS (%)":['',''],
        "2G Iniciated calls":['Hay llamadas iniciadas','No hay llamadas iniciadas'],
        "2G DL Data traffic (KB)":['',''],
        "2G UL Data traffic (KB)":['',''],
        "2G ICMBand () ":['Se cumple el target en horas valle','Valores elevados en horas valle'],
        "2G Cell Availability (%)":['Valores correctos de availability','Problemas de availability en '],
        "2G Speech disconnections":['',''],
        "3G CDR CS (%)":['',''],
        "3G CSSR CS (%)":['',''],
        "3G CSSR PS (%)":['',''],
        "3G Iniciated calls":['Hay llamadas iniciadas','No hay llamadas iniciadas en'],
        "3G DL Data traffic (KB)":['',''],
        "3G UL Data traffic (KB)":['',''],
        "3G RTWP (dBm)":['Se cumple el target en horas valle','Valores elevados en horas valle en'],
        "3G Cell Availability (%)":['Valores correctos de availability','Problemas de availability en '],
        "3G Calls ending in 2G (%)":['Valores por debajo del umbral del 10%','Valores elevados de 3G calls ending in 2G en '],
        "TH DL (2G3G4G)":['',''],
        "TH UL (2G3G4G)":['',''],
        "4G CDR (VoLTE) (%)":['',''],
        "4G_DCR_DATA":['',''],
        "4G CSSR (VoLTE) (%)":['',''],
        "4G CSSR PS (%)":['',''],
        "4G Iniciated calls (VoLTE)":['Hay llamadas iniciadas','No hay llamadas iniciadas '],
        "4G DL Data traffic (MB)":['',''],
        "4G UL Data traffic (MB)":['',''],
        "4G Interference PUSCH (dBm)":['Se cumple el target en horas valle','Valores elevados en horas valle en '],
        "4G Cell Availability (%)":['Valores correctos de availability','Problemas de availability'],
        "4G MIMO (Rank2) ()":['',''],
        "4G MIMO (Rank4) ()":['Valores correctos de MIMO Rank4','No hay valores de MIMO Rank4'],
        "4G CSFB E2W":['',''],
        "4G CA in PCELL":['',''],
        "4G CA in SCELL":['',''],
        "4G IntraLTE HOSR (including preparation) ()":['',''],
        "4G SRVCC HO Att":['Hay intentos de SRVCC en','Sin intentos de SRVCC en','Teniendo en cuenta la cantidad de llamadas iniciadas, se considera que el comportamiento es el esperado'],
        "Tput DL 4G >2Mbps":['',''],
        "Tput UL 4G >500kbps":['','']}


def justification(cellList):
    text = ': '
    status = ''
    cellsNOK = []
    for i in cellList:
        
        if i[2] == "NOK":
            cellsNOK.append(i[0])
    
    if len(cellsNOK) > 0:
        cells = ', '.join(cellsNOK)
        status = 'NOK. ' + dic[i[1]][1] + cells + '. Ha quedado escalado al adjudicatario.'
    else:
        
        cont = 0
        for i in cellList:
            if i[2] != "NOK" and i[2] != "OK":
                cont += 1
                status = 'OK. ' + dic[i[1]][2] + '.'
            if cont == 0:
                status = 'OK. ' + dic[i[1]][0] + '.'    
                         
    text += status

    return text       
    
def create(listNOK,listNOKchecked,site):
    
    word = Document()
    
    now = time.strftime("%X")
    
    if now < str(12):
        word.add_paragraph(f"Buenos días,\nSe adjunta informe Babysitting 48 del site {site}. A continuación, se justifican sus KPI NOK.\n")
    else:
        word.add_paragraph(f"Buenas tardes,\nSe adjunta informe Babysitting 48 del site {site}. A continuación, se justifican sus KPI NOK.\n")

    for i in listNOK:
        total = ''
        cellList = []
        for j in listNOKchecked:
            if i == j[1]:
                cellList.append(j)      
        total += justification(cellList)
        p = word.add_paragraph()
        p.add_run(i).bold = True
        p.add_run(total)

        for k in range(len(cellList)):
            word.add_picture(f'.\\graphs\\{i}_{k+1}.png',width=Cm(20))

    
    word.save("babysitting.docx")
        

listNOK = {'4G SRVCC HO Att', '4G Cell Availability (%)', '2G ICMBand () ', '4G Iniciated calls (VoLTE)', '4G Interference PUSCH (dBm)', '2G Iniciated calls', '3G Iniciated calls', '2G Cell Availability (%)', '3G Cell Availability (%)'}

listNOKchecked = [['CLMX7711M3A', '4G Interference PUSCH (dBm)', 'NOK'], ['CLMX7711M3A', '4G Cell Availability (%)', 'OK'], ['CLMX7711M2A', '4G Iniciated calls (VoLTE)', 'OK'], ['CLMX7711M2A', '4G Interference PUSCH (dBm)', 'OK'], ['CLMX7711M1A', '4G Interference PUSCH (dBm)', 'OK'], ['CLMX7711M1A', '4G Cell Availability (%)', 'OK'], ['CLMX7711N2A', '4G Interference PUSCH (dBm)', 'OK'], ['CLMX7711N1A', '4G SRVCC HO Att', '4G_QF_VoLTE_Initiated_Calls(#)'], ['X7711F3', '3G Cell Availability (%)', 'OK'], ['X7711F1', '3G Iniciated calls', 'OK'], ['X7711F1', '3G Cell Availability (%)', 'OK'], ['X7711E3', '2G ICMBand () ', 'OK'], ['X7711E3', '2G Cell Availability (%)', 'OK'], ['X7711E2', '2G Iniciated calls', 'OK'], ['X7711E2', '2G Cell Availability (%)', 'OK'], ['X7711E1', '2G Cell Availability (%)', 'NOK']] 

#create(listNOK,listNOKchecked)
