import checkNOK
from modules import graph
import time


numCells = 3
numTechs = 4

startTime = time.time()
KPIoverview, listNOKchecked = checkNOK.justification_consolidation(numCells,numTechs)
print("--- %s seconds <total> ---" % (time.time() - startTime))


for i in KPIoverview:
    cont = 0
    print(i)
    for j in listNOKchecked:
        if i == j[1]:
            print(f"\t{j[0]}, {j[1]}")
            cont +=1
            graph.create_graph(j[0],j[1],cont)

        
    