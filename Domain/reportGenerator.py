import checkNOK
from modules import graph
import time


numCells = 3
numTechs = 4

startTime = time.time()
KPIoverview, listNOKchecked = checkNOK.justification_consolidation(numCells,numTechs)
print("--- %s seconds <total> ---" % (time.time() - startTime))

startTime = time.time()
for i in KPIoverview:
    graphList = []
    for j in listNOKchecked:
        if i == j[1]:
            graphList.append([j[0],j[1]])
    graph.create_graph(graphList)
print("--- %s seconds <graphs> ---" % (time.time() - startTime))  
        
    