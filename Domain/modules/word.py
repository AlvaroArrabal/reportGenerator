from docx import Document
from docx.shared import Cm
# 'KPI':['OK','NOK']

dic = { "2G CDR CS (%)":['',''],
        "2G CSSR CS (%)":['',''],
        "2G CSSR PS (%)":['',''],
        "2G Iniciated calls":['hay llamadas iniciadas','no hay llamadas iniciadas'],
        "2G DL Data traffic (KB)":['',''],
        "2G UL Data traffic (KB)":['',''],
        "2G ICMBand () ":['se cumple el target en horas valle','valores elevados en horas valle'],
        "2G Cell Availability (%)":['valores correctos de availability','problemas de availability en '],
        "2G Speech disconnections":['',''],
        "3G CDR CS (%)":['',''],
        "3G CSSR CS (%)":['',''],
        "3G CSSR PS (%)":['',''],
        "3G Iniciated calls":['hay llamadas iniciadas','no hay llamadas iniciadas'],
        "3G DL Data traffic (KB)":['',''],
        "3G UL Data traffic (KB)":['',''],
        "3G RTWP (dBm)":['se cumple el target en horas valle','valores elevados en horas valle'],
        "3G Cell Availability (%)":['valores correctos de availability','problemas de availability'],
        "3G Calls ending in 2G (%)":['',''],
        "TH DL (2G3G4G)":['',''],
        "TH UL (2G3G4G)":['',''],
        "4G CDR (VoLTE) (%)":['',''],
        "4G_DCR_DATA":['',''],
        "4G CSSR (VoLTE) (%)":['',''],
        "4G CSSR PS (%)":['',''],
        "4G Iniciated calls (VoLTE)":['hay llamadas iniciadas','no hay llamadas iniciadas '],
        "4G DL Data traffic (MB)":['',''],
        "4G UL Data traffic (MB)":['',''],
        "4G Interference PUSCH (dBm)":['se cumple el target en horas valle','valores elevados en horas valle en '],
        "4G Cell Availability (%)":['valores correctos de availability','problemas de availability'],
        "4G MIMO (Rank2) ()":['',''],
        "4G MIMO (Rank4) ()":['valores correctos de MIMO Rank4','no hay valores de MIMO Rank4'],
        "4G CSFB E2W":['',''],
        "4G CA in PCELL":['',''],
        "4G CA in SCELL":['',''],
        "4G IntraLTE HOSR (including preparation) ()":['',''],
        "4G SRVCC HO Att":['',''],
        "Tput DL 4G >2Mbps":['',''],
        "Tput UL 4G >500kbps":['','']}


def justification(cellList):
    text = ''
    text += cellList[0][1] + ': '

    cellsNOK = []
    for i in cellList:
        if i[2] == False:
            cellsNOK.append(i[0])
    
    if len(cellsNOK) > 0:
        cells = ', '.join(cellsNOK)
        status= 'NOK. ' + dic[i[1]][1] + cells + '. Ha quedado escalado al adjudicatario.'
    else:
        status = 'OK. ' + dic[i[1]][0] + '\n'
    text += status

    return text       
    
def create(listNOK,listNOKchecked):
    
    word = Document()
    for i in listNOK:
        total = ''
        cellList = []
        for j in listNOKchecked:
            if i == j[1]:
                cellList.append(j)
        total += justification(cellList)
        word.add_paragraph(total)
        word.add_picture(f'.\\graphs\\{i}.png',width=Cm(20))
    
    word.save("babysitting.docx")
        




