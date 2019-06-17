import matplotlib.pyplot as plt
import networkx as nx
import tspReadCalcMatDist

def arvorePesoMaximo (grafo, k):
	# CASO BASE
	if k == 1:
		arvore = nx.Graph()
		arvore.add_node(1)
		return arvore

	# PASSO INDUTIVO
	arvore = arvorePesoMaximo(grafo, k-1)

	vertices = grafo.nodes()
	verticesUsados = arvore.nodes()
	verticesAux = []
	for vertice in vertices:
		# guarda os vértices que ainda
		# não estão na árvore de peso máximo
		if vertice not in verticesUsados:
			verticesAux.append(vertice)

	arestas = []
	for verticeUsado in verticesUsados:
		for verticeAux in verticesAux:
			# se existir aresta entre vértice da árvore de peso máximo
			# e o subgrafo auxiliar
			if grafo[verticeUsado][verticeAux]:
				arestas.append((verticeUsado, verticeAux))

	# inicializa a aresta que vai ser adicionada na árvore
	# de peso máximo
	nova_aresta = (1,1)
	for aresta in arestas:
		if grafo.edges([aresta]) > grafo.edges([nova_aresta]):
			nova_aresta = aresta

	a, b = nova_aresta
	arvore.add_node(b)
	arvore.add_edge(a, b)

	return arvore
	

grafo = tspReadCalcMatDist.readTSPcoord("ulysses16.tsp")

resultado = arvorePesoMaximo(grafo, len(grafo))
nx.draw(resultado, with_labels=True)
# plt.savefig('tmp.png')
plt.show()
