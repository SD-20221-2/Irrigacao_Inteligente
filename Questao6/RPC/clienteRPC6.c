#include<stdio.h>
#include "interface.h"

double salarioLiquido (CLIENT *clnt,char *nome, char *nivel, double sal_bruto, int n_dependentes){
	data dt;
	static double *sal_liquido;
	
	dt.nome = nome;
	dt.nivel = nivel;
	dt.sal_bruto = sal_bruto;
	dt.n_dependentes = n_dependentes;
	
	sal_liquido = calcular_salario_1(&dt,clnt);
	if(sal_liquido == NULL){
		printf("Problemas ao chamar a função remota\n");
		exit(1);
	}
	return (*sal_liquido);
}

int main(int argc, char *argv[]){
	CLIENT *clnt;
	char *x,*y;
	double z;
	int w;
	
	if(argc!=5){
		fprintf(stderr,"Sintaxe: %s hostname operando1\n",argv[0]);
		exit(1);
	}
	
	clnt = clnt_create(argv[1], CALCULA_LIQUIDO, CALCULA_VERSION,"udp");
	
	if(clnt == (CLIENT *) NULL){
		clnt_pcreateerror (argv[1]);
		exit(1);
	}

	x = argv[2];
	y = argv[3];
	z = atof(argv[4]);
	w = atoi(argv[5]);
	
	printf("Salario liquido: %lf \n Nome: %c \n Nivel: %c \n Salario Bruto: %lf \n Número de Denpendentes : %d\n", salarioLiquido(clnt,x,y,z,w));

	return(0); 

}
