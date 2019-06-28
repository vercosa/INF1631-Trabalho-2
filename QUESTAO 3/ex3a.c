#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void) {
	double soma_tempo = 0;
	int QtExec = 0;
	clock_t ti;           // Pega o Tempo de Execucao
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
	arquivoTexto = fopen("instanciasT2-prob3.txt","rt");
	fscanf(arquivoTexto,"%d",&numText); // Comeca o programa
	ti = clock();
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
		//printf("Frase: %s\n",Frase);
		fscanf(arquivoTexto,"%d",&numPalavra);  // Numero de palavras para comparar
		while(numPalavra != 0) {
			fscanf(arquivoTexto,"%s", &Palavra); 
			m = strlen(Palavra);
			//printf("Palavra: %s\n",Palavra);
			numPalavra--;
			j = 0;
			i = 0;
			while(Start[l][g] == 0 && i <= n) {
				if(Palavra[j] == Frase[i]) {
					//printf("Achei igual: Palavra[%d]: %c == Frase[%d]: %c\n",j,Palavra[j],i,Frase[i]);
					j++;
					i++;
				}
				else {
					j = 0;
					i++;
				}
				if(j == m) {
					Start[l][g] = i - m;
				}
			}
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
	ti = clock() - ti;
	double tempo_total = ((double)ti)/CLOCKS_PER_SEC;
	for(i = 0; i < 3; i++) {
		printf("Frase %d:\n",i+1);
		for(j = 0; j < 3; j++) {
			printf("Posicao Palavra %d: %d\n",j+1,Start[i][j]);
		}
	}
	printf("Tempo de execucao: %f segundos\n",tempo_total);
	fclose(arquivoTexto);
	return 0;
}
