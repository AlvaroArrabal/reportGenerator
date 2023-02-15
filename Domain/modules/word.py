from docx import Document
from docx.shared import Cm
import time
# 'KPI':['OK','NOK']

dic = { "2G CDR CS (%)":['Degradación puntual','Degradaciones repetitivas en '],
        "2G CSSR CS (%)":['',''],
        "2G CSSR PS (%)":['',''],
        "2G Iniciated calls":['Hay llamadas iniciadas','No hay llamadas iniciadas en '],
        "2G DL Data traffic (KB)":['',''],
        "2G UL Data traffic (KB)":['',''],
        "2G ICMBand () ":['Se cumple el target en horas valle','Valores elevados en horas valle en'],
        "2G Cell Availability (%)":['Valores correctos de availability','Problemas de availability en '],
        "2G Speech disconnections":['',''],
        "3G CDR CS (%)":['Degradación puntual','Degradaciones repetitivas en '],
        "3G CSSR CS (%)":['',''],
        "3G CSSR PS (%)":['',''],
        "3G Iniciated calls":['Hay llamadas iniciadas','No hay llamadas iniciadas en '],
        "3G DL Data traffic (KB)":['',''],
        "3G UL Data traffic (KB)":['',''],
        "3G RTWP (dBm)":['Se cumple el target en horas valle','Valores elevados en horas valle en '],
        "3G Cell Availability (%)":['Valores correctos de availability','Problemas de availability en '],
        "3G Calls ending in 2G (%)":['Valores por debajo del umbral del 10%','Valores elevados de 3G calls ending in 2G en '],
        "TH DL (2G3G4G)":['',''],
        "TH UL (2G3G4G)":['',''],
        "4G CDR (VoLTE) (%)":['Degradación puntual','Degradaciones repetitivas en '],
        "4G_DCR_DATA":['Degradación puntual','Degradaciones repetitivas en '],
        "4G CSSR (VoLTE) (%)":['',''],
        "4G CSSR PS (%)":['',''],
        "4G Iniciated calls (VoLTE)":['Hay llamadas iniciadas','No hay llamadas iniciadas en '],
        "4G DL Data traffic (MB)":['',''],
        "4G UL Data traffic (MB)":['',''],
        "4G Interference PUSCH (dBm)":['Se cumple el target en horas valle','Valores elevados en horas valle en '],
        "4G Cell Availability (%)":['Valores correctos de availability','Problemas de availability en '],
        "4G MIMO (Rank2) ()":['',''],
        "4G MIMO (Rank4) ()":['Valores correctos de MIMO Rank4','No hay valores de MIMO Rank4 en '],
        "4G CSFB E2W":['',''],
        "4G CA in PCELL":['',''],
        "4G CA in SCELL":['',''],
        "4G IntraLTE HOSR (including preparation) ()":['',''],
        "4G SRVCC HO Att":['Hay intentos de SRVCC en','Sin intentos de SRVCC en ','Teniendo en cuenta la cantidad de llamadas iniciadas, se considera que el comportamiento es el esperado'],
        "Tput DL 4G >2Mbps":['',''],
        "Tput UL 4G >500kbps":['Valores entorno al target objetivo de TH (0.5 Mbps)','Valores bajos de TH en ']}


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
    
def create(listNOK,listNOKchecked,site,path):
    
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
            if i.find('>') == -1:
                word.add_picture(f'.\\graphs\\{i}_{k+1}.png',width=Cm(20))
            else:
                element = i.replace('>','')
                word.add_picture(f'.\\graphs\\{element}_{k+1}.png',width=Cm(20))

    name = path + '\\Babysitting_' + site + '.docx'
    word.save(name)
   
