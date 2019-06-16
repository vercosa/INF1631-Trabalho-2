import networkx as nx
import tspReadCalcMatDist
import matplotlib.pyplot as plt

def florestaPesoMinimo (grafo, k):
	# CASO BASE
	if k == 1:
		floresta = nx.Graph()
		for vertice in grafo.nodes:
			floresta.add_node(vertice)

		return floresta

	lstComponentes = []
	for c in nx.connected_components(grafo):
		print(c)
		lstComponentes.append(c)
	print(lstComponentes)

	# PASSO INDUTIVO
	floresta = florestaPesoMinimo (grafo, k-1)

	lstComponentes = []
	for c in nx.connected_components(floresta):
		print(c)
		lstComponentes.append(c)

	componenteEscolhido = None
		# guarda componente com tamanho menor que k
	for componente in lstComponentes:
		print(componente)
		if len(componente) < k:
			componenteEscolhido = componente
			print(componenteEscolhido)
			break

		# caso só tenha componentes com tamanho igual a k ou maior
		# sai da iteração
	# if componenteEscolhido == None:
	# 	break

	arestas = grafo.edges()
	arestasUsadas = floresta.edges()
	arestasDisponiveis = []
	for aresta in arestas:
		if aresta not in arestasUsadas:
			arestasDisponiveis.append(aresta)

	arestasVizinhas = []
	for aresta in arestasDisponiveis:
		if aresta[0] in componenteEscolhido:
			arestasVizinhas.append(aresta)	

		# print(grafo.edges)
	arestaPesoMin = (1,1)
	for aresta in arestasVizinhas:
		if grafo.edges[aresta]['weight'] < grafo.edges[arestaPesoMin]['weight']:
			arestaPesoMin = aresta

		# arestaPesoMin = min(arestasVizinhas, key=lambda e: grafo.edges(e)['weight'])

	floresta.add_edge(arestaPesoMin[0],arestaPesoMin[1])

	return floresta

grafo = tspReadCalcMatDist.readTSPcoord("ulysses16.tsp")
resultado = florestaPesoMinimo(grafo, 2)

nx.draw(resultado, with_labels=True)
# plt.savefig('tmp.png')
plt.show()
# print(nx.connected_components(grafo))
# for i in nx.connected_components(grafo):
# 	print(i)

# [print(len(c)) for c in sorted(nx.connected_components(grafo), key=len, reverse=True)]

G = nx.path_graph(4)
nx.add_path(G, [10, 11, 12])
# [print(len(c)) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
nx.draw(G, with_labels=True)
plt.show()
print(nx.connected_components(G))
lista = []
for c in nx.connected_components(G):
	lista.append(c)

print(lista)

# print(lista[0])
# # resultado = florestaPesoMinimo(grafo, 1)
# # nx.draw(resultado, with_labels=True)
# # # plt.savefig('tmp.png')
# # plt.show()
