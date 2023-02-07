from Domain.reportGenerator import generate,checkNOK


def run():
    numCells = 3
    numTechs = 4
    site = 'XXX1234'

    generate(numCells,numTechs,site)