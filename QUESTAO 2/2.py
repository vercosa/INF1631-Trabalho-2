from enum import Enum

# posição das casas em torno da casa X
# 0 1 2
# 3 X 4
# 5 6 7
class CasasEmTorno(Enum):
	TOPO_ESQUERDA = 0
	TOPO_MEIO = 1
	TOPO_DIREITA = 2
	MEIO_ESQUERDA = 3
	MEIO_DIREITA = 4
	INFERIOR_ESQUERDA = 5
	INFERIOR_MEIO = 6
	INFERIOR_DIREITO = 7

# carrega o arquivo e coloca as informações de cada instância do tabuleiro em um dict
def carregarArquivo():
	matrizes = []

	with open('walk.in') as f:
		q = int(f.readline().split()[0])

		while q != 0:
			custos = []
			for i in range(8):
				linha = list(map(int,f.readline().strip().split(' ')))
				custos.append(linha)

			premios = []
			for i in range(8):
				linha = list(map(int,f.readline().strip().split(' ')))
				premios.append(linha)

			matrizes.append({'Energia': q, "Custos": custos, "Premios": premios})

			q = int(f.readline().split()[0])

	return matrizes

def walkOfKing ():
	global premioMax, caminho, dx, dy, custos, premios, energia

	matrizes = carregarArquivo()

	# exemplo com a primeira instancia
	custos = matrizes[0]['Custos']
	premios = matrizes[0]['Premios']
	energia = matrizes[0]['Energia']

	# inicializa matriz que vai guardar o premio maximo no tabuleiro
	premioMax = [[[-3 for k in range(8)] for j in range(8)] for i in range(energia)]
	# inicializa matriz que vai guardar o caminho no tabuleiro
	caminho = [[[-3 for k in range(8)] for j in range(8)] for i in range(energia)]

	# deslocamento no eixo x
	# -1 0 1
	# -1   1
	# -1 0 1
	dx = [-1, 0, 1,-1, 1,-1, 0, 1]
	# deslocamento no eixo y
	# -1 -1 -1
	#  0     0
	#  1  1  1
	dy = [-1,-1,-1, 0, 0, 1, 1, 1]

	for e in range(energia):
		for i in range(8):
			for j in range(8):
				# CASO BASE
				if e == 0:
					walkOfKingCasoBase(i,j,e)
				# PASSO INDUTIVO
				else:
					walkOfKingPassoIndutivo(i,j,e)
		

def walkOfKingCasoBase (i, j, energia):
	# prêmio máximo dessa posição vai ser 0 e o caminho chegará ao fim
	if (i == 0 and j==0):
		premioMax[energia][i][j] = 0
		caminho[energia][i][j] = -1
	# prêmio máximo pode ser considerado menos infinito e não existe um caminho
	else:
		premioMax[energia][i][j] = -1
		caminho[energia][i][j] = -2		

def walkOfKingPassoIndutivo (i, j, energia):
	premioMaxAtual = -1
	direcaoPremioMax = -2

	for direcao in range(CasasEmTorno.TOPO_ESQUERDA.value, CasasEmTorno.INFERIOR_DIREITO.value+1):
		casaX = i + dx[direcao]
		casaY = j + dy[direcao]

		# se (x,y) estiver fora do tabuleiro e não for uma posição válida
		if casaX<0 or casaY<0 or casaX>7 or casaY>7:
			continue;

		casaPremio = premios[casaX][casaY]
		casaCusto = custos[casaX][casaY]

		# se o custo da casa for maior que a energia disponivel
		if (casaCusto > energia):
			continue;

		if casaPremio == -1 or premioMax[energia-casaCusto][casaX][casaY] == -1:
			casaPremio_max = -1
		else:
			casaPremio_max = casaPremio + premioMax[energia-casaCusto][casaX][casaY]

		if (casaPremio_max > premioMaxAtual):
			premioMaxAtual = casaPremio_max
			direcaoPremioMax = direcao

	premioMax[energia][i][j] = premioMaxAtual
	caminho[energia][i][j] = direcaoPremioMax

def imprimirResultado():
	melhorPremio = -1
	energiaUsada = None

	# descobre o melhor prêmio e a energia usada
	for e in range(energia):
		if premioMax[e][0][0] > melhorPremio:
			melhorPremio = premioMax[e][0][0]
			energiaUsada = e

	print("Melhor prêmio possível: {}".format(melhorPremio))
	print("Energia usada: {}".format(energiaUsada+1))

	x = 0
	y = 0
	
	while (caminho[energiaUsada][x][y] != -1 and caminho[energiaUsada][x][y] != -2):
		proximoX = x + dx[caminho[energiaUsada][x][y]]
		proximoY = y + dy[caminho[energiaUsada][x][y]]

		energiaUsada -= custos[proximoX][proximoY]

		x = proximoX
		y = proximoY

# exemplo com a primeira instancia
walkOfKing()
imprimirResultado()

