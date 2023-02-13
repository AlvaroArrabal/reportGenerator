from Domain import checkNOK
from Domain.modules import graph,word
import time
import os


def generate_consolidation_report(numCells,numTechs,site):
    startTime = time.time()
    KPIoverview, listNOKchecked = checkNOK.justification_consolidation(numCells,numTechs)
    print("--- %s seconds <check NOK> ---" % (time.time() - startTime))
    #print(KPIoverview)
    #print(listNOKchecked)

    startTime = time.time()
    for i in KPIoverview:
        graphList = []
        for j in listNOKchecked:
            if i == j[1]:
                graphList.append(j)
        graph.create_graph(graphList)
    print("--- %s seconds <graphs> ---" % (time.time() - startTime))

    
    startTime = time.time()
    word.create(KPIoverview, listNOKchecked,site)
    print("--- %s seconds <word> ---" % (time.time() - startTime))


