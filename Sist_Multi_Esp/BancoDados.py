#banco de dados para sistema multi-especialistas

class Cliente(object):
    def variaveis(self, kWh, preco, pay, pr, ir):
        self.kWh = kWh
        self.preco = preco
        self.pay = pay
        self.pr = pr
        self.ir = ir
    
    def consumo_diario(self):
        return self.kWh
    
    def tarifa(self):
        return self.preco
    
    def pagamento(self):
        return self.pay
    
    def performance(self):
        return self.pr
    
    def irrad(self):
        return self.ir
    
cliente = Cliente()
cliente.variaveis(4.29, 0.89, 150, 0.82, 4.29)
csm_diario = cliente.consumo_diario()
cliente_preco = cliente.tarifa()
cliente_pagamento = cliente.pagamento()
cliente_perfomance = cliente.performance()
cliente_irrad = cliente.irrad()


