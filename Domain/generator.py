from modules import getData,analyzeKPI
import pandas as pd


data = getData.get2G("M1990E2")


def justification(numCells,numTechs):
    
    # 1º getNOK
    listNOK = getData.getNOK(numCells,numTechs)

    
    # 2º type of NOK?
    for i in range(len(listNOK)):
        match listNOK[i][1]:
            case '5G RLC UL Traffic (GB)':
                # 3º NOK_i = analyzeKPI
                print("RSSI")
            case 'Interference 4G PUSCH UL (RSSI UL 4G)':
                print("PUSCH")
        


justification(2,2)

def word():
    pass