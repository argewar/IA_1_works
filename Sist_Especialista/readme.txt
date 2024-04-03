BASE DE CONHECIMENTO
-localização
-Orientação (Norte geográfico)
-Irradiação no plano do telhado
-área disponível p/instalação
-consumo médio anual (kWh)
-tipo de consumidor (A, B,)

BASE DE REGRAS
-SE o consumo > 7000 (kWh)
	ENTÃO SE area disponivel <= area projetada
	ENTAO SE tipo de consumidor == A
	ENTAO SE retorno <= 6 (anos)
-ENTAO ML.

-SE o consumo <= 7000 (kWh)
	ENTAO SE area disponivel >= area projetada
	ENTAO SE tipo de consumidor == B
	ENTAO SE retorno <= 6 (anos)
-ENTAO AUTOPRODUÇÃO

-SE o consumo > 7000 (kWh)
	ENTAO SE area disponivel >= area projetada
	ENTAO SE tipo de consumidor == A
	ENTAO SE retorno <= 6 (anos)
-ENTAO AUTOPRODUÇÃO

-SE o consumo <= 7000 (kWh)
	ENTAO SE area disponivel <= area projetada
-ENTAO AÇÕES EFICIENCIA

MÁQUINA DE INFERÊNCIA
decidir = sistema_fotovoltaico() ou mercado_livre_energia() ou ações_eficiencia_energetica ()
SE decidir:
	printar(decidir)
SE NÃO:
	printar(reveja os dados)