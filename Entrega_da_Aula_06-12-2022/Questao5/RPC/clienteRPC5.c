#include<stdio.h>
#include "interface.h"

char categoria (CLIENT *clnt, int idade){
	data dt;
	char *cat;
	
	dt.idade = idade;
	
	cat = categoria_1(&dt,clnt);
	if(cat == NULL){
		printf("Problemas ao chamar a função remota\n");
		exit(1);
	}
	return (*cat);
}

int main(int argc, char *argv[]){
	CLIENT *clnt;
	int x;
	
	if(argc!=4){
		fprintf(stderr,"Sintaxe: %s hostname operando1\n",argv[0]);
		exit(1);
	}
	
	clnt = clnt_create(argv[1], CALCULA_CATEGORIA, CATEGORIA_VERSION,"udp");
	
	if(clnt == (CLIENT *) NULL){
		clnt_pcreateerror (argv[1]);
		exit(1);
	
	}

	x = atoi(argv[2]);
	
	printf("Categoria : %c" , categoria(clnt,x));

	return(0); 

}
