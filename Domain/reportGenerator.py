from Domain import checkNOK
from Domain.modules import graph,word

def generate_consolidation_report(numCells,numTechs,site,pathSave,babysittingPath):
    
    KPIoverview, listNOKchecked = checkNOK.justification_consolidation(numCells,numTechs,babysittingPath)

    for i in KPIoverview:
        graphList = []
        for j in listNOKchecked:
            if i == j[1]:
                graphList.append(j)
        graph.create(graphList)

    word.create(KPIoverview, listNOKchecked,site,pathSave,'consolidation')



def generate_expansion_report(numCells,numTechs,site,pathSave,babysittingPath):
    KPIoverview, listNOKchecked = checkNOK.justification_expansion(numCells,numTechs,babysittingPath)
    for i in KPIoverview:
        graphList = []
        for j in listNOKchecked:
            if i == j[1]:
                graphList.append(j)
        graph.create(graphList)

    word.create(KPIoverview, listNOKchecked,site,pathSave,'expansion')