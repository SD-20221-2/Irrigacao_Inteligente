struct data{
	int idade;
};

program CALCULA_CATEGORIA{
	version CATEGORIA_VERSION{
		char CATEGORIA(data) = 1;
	} = 1;
} = 0x20000001;
