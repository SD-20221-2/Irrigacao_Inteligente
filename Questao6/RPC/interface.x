struct data{
	char *nome;
	char *nivel;
	double sal_bruto;
	int n_dependentes;
};

program CALCULA_LIQUIDO{
	version CALCULA_VERSION{
		double calcular_salario(data) = 1;
	} = 1;
} = 0x20000001;
