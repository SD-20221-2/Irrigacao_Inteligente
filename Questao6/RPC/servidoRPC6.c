#include<stdio.h>
#include <string.h>
#include "interface.h"

double * calcular_salario_1_svc(data *argp, struct svc_req *rqstp){
	
	static double sal_liquido ; 
	
	if(strcmp(argp->nivel,"A")){
		if((argp->n_dependentes) > 0){
			sal_liquido = argp->sal_bruto * 0.08;
		}else{
			sal_liquido = argp->sal_bruto * 0.03;
		}
	}else if(strcmp(argp->nivel,"B")){
		if( (argp->n_dependentes) > 0){
			sal_liquido = argp->sal_bruto * 0.1;
		}else{
			sal_liquido = argp->sal_bruto * 0.05;
		}
	}else if(strcmp(argp->nivel,"C")){
		if ((argp->n_dependentes) > 0){
			sal_liquido = argp->sal_bruto * 0.15;
		}else{
			sal_liquido = argp->sal_bruto * 0.08;
		}	
	}else if(strcmp(argp->nivel,"D")){
		if ((argp->n_dependentes) > 0){
			sal_liquido = argp->sal_bruto * 0.17;
		}else{
			sal_liquido = argp->sal_bruto * 0.1;
		}
	}
	
	return(&sal_liquido);
}
