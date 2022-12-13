#include<stdio.h>
#include <string.h>
#include "interface.h"

char * categoria_1_svc(data *argp, struct svc_req *rqstp){	

	char *s = malloc(sizeof(char) * 20);
	
	if( argp->idade >= 5 && argp->idade <= 7 ){
		strcpy(s,"infatil A");
	}else if( argp->idade >= 8 && argp->idade <= 10){
		strcpy(s,"infatil B");
	}else if(argp->idade >= 11 && argp->idade <= 13){
		strcpy(s,"juvenil A");
	}else if( argp->idade >= 14 && argp->idade <= 17){
		strcpy(s,"juvenil B");
	}else if( argp->idade >= 18 ){
		strcpy(s,"adulto");
	}
	return(s);
}
