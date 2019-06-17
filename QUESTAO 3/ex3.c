#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	FILE *arquivoTexto;  	// Arquivo com as instancias
	char* Frase;    			// A
	char* Palavra;  			// B
	int n;          			// Tamanho da Frase  
	int m;          			// Tamanho da Palavra
	int numText;
	char t[15];
	int Start = 0;        // Posicao inicial onde B == A
	int *Next;         
	int i = 0;
	int j = 0;
	
	arquivoTexto = fopen("instanciasT2-prob3.txt","rt");
	fscanf(arquivoTexto,"%d",&numText);
	fscanf(arquivoTexto,"%s", &t);
	while(fscanf(arquivoTexto,"%s", &t) != EOF
	//Completa a Frase e a Palavra
	
	while(Start == 0 && i <= n) {
		if(strcmp(Palavra[j],Frase[i]) == 0) {
			j += 1;
			i += 1;
		}
		else {
			j = Next[j] + 1;
			if(j < 0) {
				j = 0;
				i += 1;
			}
		}
		if(j == m+1) {
			Start = i-m;
		} 
	}

	return 0;
}
