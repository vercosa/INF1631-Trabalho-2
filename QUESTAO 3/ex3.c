#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	FILE *arquivoTexto;  	// Arquivo com as instancias
	char Frase[1500];    	// A
	char Palavra[20];  		// B
	int n = 0;          	// Tamanho da Frase  
	int m = 0;          	// Tamanho da Palavra
	int l = 0;            // Indice Linha do Start
	int g = 0;						// Indice Coluna do Start
	int numText;          // Quantidade de textos
	int numPalavra;       // Quantidade de Palavras
	char t[20];
	int Start[9][9];      // Posicao inicial onde B == A
	int Next[20];         
	int i = 0;
	int j = 0;
	
	while(l < 9) { 				// Inicia o valor de Start
		while(g < 9) {
			Start[l][g] = 0;
			g++;
		}
		g = 0;
		l++;
	}
	l = 0;
	while(j < 20) {
		Next[j] = 0;
		j++;
	}
	j = 0;
	arquivoTexto = fopen("instanciasT2-prob3.txt","rt");
	fscanf(arquivoTexto,"%d",&numText); // Comeca o programa
	while(numText != 0) {
		memset(Frase, 0, sizeof(Frase));  // Reseta a Frase
		fscanf(arquivoTexto,"%s", &t);    // Pega o primeiro valor T
		while(strcmp(t,"W ") != 0) {      // Enquanto nao achar W
			memset(t, 0, sizeof(t));        // Reseta o t auxiliar
			fscanf(arquivoTexto,"%s", &t);  // Le palavra
			n = n + strlen(t) + 1;          // Adiciona mais um ao indice
			t[strlen(t)] = ' ';             // Adiciona espacamento
			while(i != n) {                 // Bota a palavra na Frase
				Frase[i] = t[j];
				i++;
				j++;
			}
			j = 0;
		}
		n = n - 2;                        // Remove o W
		i = 0;
		printf("Frase: %s\n",Frase);
		fscanf(arquivoTexto,"%d",&numPalavra);  // Numero de palavras para comparar
		while(numPalavra != 0) {
			fscanf(arquivoTexto,"%s", &Palavra); 
			m = strlen(Palavra);
			printf("Palavra: %s\n",Palavra);
			numPalavra--;
			// ----------------------Treta Start----------------------------------------------
			Next[0] = -1;
			Next[1] = 0;
			for(i = 2;i < m;i++) {
				j = Next[i-1] + 1;
				while(Palavra[i-1] != Palavra[j]) {
					j = Next[j] + 1;
				}
				Next[i] = j;
			}
			i = 0;
			j = 0;
			while(Start[l][g] == 0 && i <= n) {
				if(Palavra[j] == Frase[i]) {
					j += 1;
					i += 1;
				}
				else {
					j = Next[j];
					if(j == 0) {
						j = 1;
						i += 1;
					}
				}
				if(j == m) {
					Start[l][g] = i-m;
				}
				printf("Erro %d %d\n",i,j);
			}
			// -------------------------Treta End----------------------------------------------------
			g++;
		}           // Prepara para a proxima iteracao
		n = 0;
		m = 0;
		i = 0;
		j = 0;
		g = 0;
		l++;
		numText--;
	}
	for(i = 0; i < 3; i++) {
		printf("Frase %d:\n",i+1);
		for(j = 0; j < 3; j++) {
			printf("Posicao Palavra %d: %d\n",j+1,Start[i][j]);
		}
	}
	fclose(arquivoTexto);
	return 0;
}
