class Produto:
    def __init__(self, name, preço, quantidade):
        self.name = name
        self.preço = preço
        self.quantidade = quantidade

    def reduzir_produto(self):
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidade(s) de {nome} compradas com sucesso. Estoque atualizado {self.quantidade} ")
        else:
            print(f"Quantidade insuficiente em estoque do {self.nome}")
