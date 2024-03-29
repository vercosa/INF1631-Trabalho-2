# https://networkx.github.io/
import networkx as nx
from math import sqrt

# matriz de distâncias TSP
def readTSPcoord (nomeArquivo):
    CoordX = []
    CoordY = []

    # lê o arquivo .tsp
    with open(nomeArquivo, 'r') as tsp:
        if "bays29" in nomeArquivo:
            for line in tsp:
                if 'DIMENSION' in line:
                    Ncities = int(line.split()[1])

                if 'DISPLAY_DATA_SECTION' in line:
                    for indice, line in enumerate(tsp):
                        if 'EOF' in line:
                            break;
                        # listaCidades.append(Cidade(float(line.split()[1]), float(line.split()[2])))
                        CoordX.append(float(line.split()[1]))
                        CoordY.append(float(line.split()[2]))
        elif "dantzig42" in nomeArquivo:
            for line in tsp:
                if 'DIMENSION' in line:
                    Ncities = int(line.split()[2])

                if 'DISPLAY_DATA_SECTION' in line:
                    for indice, line in enumerate(tsp):
                        if 'EOF' in line:
                            break;
                        # listaCidades.append(Cidade(float(line.split()[1]), float(line.split()[2])))
                        CoordX.append(float(line.split()[1]))
                        CoordY.append(float(line.split()[2]))

        elif "eil51" in nomeArquivo or "att48" in nomeArquivo or "eil76" in nomeArquivo or "bier127" in nomeArquivo or "usa13509" in nomeArquivo:
            for line in tsp:
                if 'DIMENSION' in line:
                    Ncities = int(line.split()[2])

                if 'NODE_COORD_SECTION' in line:
                    for indice, line in enumerate(tsp):
                        if 'EOF' in line:
                            break;
                        # listaCidades.append(Cidade(float(line.split()[1]), float(line.split()[2])))
                        CoordX.append(float(line.split()[1]))
                        CoordY.append(float(line.split()[2]))            
        else:
            for line in tsp:
                if 'DIMENSION' in line:
                    Ncities = int(line.split()[1])

                if 'NODE_COORD_SECTION' in line:
                    for indice, line in enumerate(tsp):
                        if 'EOF' in line:
                            break;
                        # listaCidades.append(Cidade(float(line.split()[1]), float(line.split()[2])))
                        CoordX.append(float(line.split()[1]))
                        CoordY.append(float(line.split()[2]))


    # inicializa matriz de adjacência
    Cost = [[-1 for x in range(Ncities)] for y in range(Ncities)] 

    # utiliza o package networkx para inicializar um grafo e
    # facilitar a criação de imagens e acesso aos vértices e arestas
    grafo = nx.Graph()

    # adiciona os vértices no grafo
    for i in range(1, Ncities+1):
    	grafo.add_node(i)

    # O cálculo da distâncias entre 2 cidades deve ser feito
    # da seguinte forma:
    # 1 - Calcular a distancia euclidiana em valor real (float ou double)
    # 2 - Somar 0.5 a essa distancia
    # 3 - Truncar para inteiro
    for i in range(Ncities):
        for j in range(Ncities):
            xd = CoordX[i] - CoordX[j]
            yd = CoordY[i] - CoordY[j]
            zd = sqrt( (xd*xd) + (yd*yd) ) + 0.5
            Cost[i][j] = int(round(zd))
            
            # i+1 e j+1 para corrigir o índice
            # o primeiro vértice do grafo vai ser 1 e não 0
            # no entanto o primeiro índice de CoordX e CoordY é 0
            grafo.add_edge(i+1, j+1, weight = int(round(zd)))

    return grafo