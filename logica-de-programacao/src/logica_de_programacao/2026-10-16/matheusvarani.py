# Matheus Cirne Varani

import os

class Opcao:
    def __init__(self, nome: str = "", mostrar: str = "", valor = None, num: int = 0, tipo: str = "func"):
        self.nome = nome
        self.mostrar = mostrar
        self.valor = valor
        self.num = num
        self.tipo = tipo

class Opcoes:
    def __init__(self, opcoes: list[Opcao] = []):
        self.opcoes = opcoes

    def get_opt(self, num: int) -> Opcao:
        for opt in self.opcoes:
            if opt.num == num:
                return opt
        return Opcao()

    def disponiveis(self) -> list[int]:
        return [opt.num for opt in self.opcoes]

class CustomException(Exception):
    def __init__(self, mensagem: str = ""):
        self.mensagem = mensagem
        super().__init__(mensagem)

class Nadador:
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = self.registrar_idade(idade)

    def registrar_idade(self, idade: int):
        if idade < 5:
            raise CustomException("Idade deve ser igual ou maior a 5")
        return idade

class Categoria:
    def __init__(self, nome: str, nadadores: list[Nadador]):
        self.nome = nome
        self.nadadores = nadadores
        self.quantia = len(nadadores)

    def porcentagem(self, total: int) -> float:
        return round(self.quantia/total*100, 1)

class Relatorio:
    def __init__(self, total: int, categorias: list[Categoria]):
        self.total = total
        self.categorias = categorias

class Nadadores:
    def __init__(self):
        self.nadadores: list[Nadador] = []

    def adicionar(self, nadador: Nadador):
        for n in self.nadadores: 
            if nadador.nome == n.nome and nadador.idade == n.idade:
                raise CustomException("Nadador já cadastrado previamente")
        self.nadadores.append(nadador)

    def gerar_relatorio(self) -> Relatorio:
        total = len(self.nadadores)
        categoria_1 = Categoria("infantil A", [nadador for nadador in self.nadadores if nadador.idade < 8])
        categoria_2 = Categoria("infantil B", [nadador for nadador in self.nadadores if nadador.idade > 7 and nadador.idade < 11])
        categoria_3 = Categoria("juvenil A", [nadador for nadador in self.nadadores if nadador.idade > 10 and nadador.idade < 14])
        categoria_4 = Categoria("juvenil B", [nadador for nadador in self.nadadores if nadador.idade > 13 and nadador.idade < 18])
        categoria_5 = Categoria("adulto", [nadador for nadador in self.nadadores if nadador.idade >= 18])
        return Relatorio(total, [categoria_1, categoria_2, categoria_3, categoria_4, categoria_5])

def validar_numero(valor: str) -> int:
    try:
        valor = int(valor)
        return valor
    except:
        raise CustomException("Valor fornecido deve ser um número")

def cadastrar_nadadores(nadadores: Nadadores):
    while True:
        os.system('clear')
        print("-- Deixe o campo vazio e pressione ENTER para voltar --\n")
        nome = input("> Nome: ")
        if nome == "": break
        idade = input("> Idade: ")
        os.system("clear")
        if idade == "": break
        try:
            idade = validar_numero(idade)
            nadador = Nadador(nome, idade)
            nadadores.adicionar(nadador)
        except CustomException as e:
            input(f"[ERRO] - {e.mensagem}")

def relatorio(nadadores: Nadadores):
    if len(nadadores.nadadores) == 0:
        raise CustomException("Nenhum nadador registrado")
    r = nadadores.gerar_relatorio()
    for categoria in r.categorias:
        print(f"Categoria: {categoria.nome}\nQuantia de nadadores registrados: {categoria.quantia}\nPercentual da quantia em relação ao total: {categoria.porcentagem(r.total)}%\n")
    print(f"Total de nadadores registrados: {r.total}")
    input()

def menu_principal():
    running = True
    nadadores = Nadadores()
    while running:
        os.system('clear')
        opcoes = Opcoes([Opcao("cadastrar_nadadores", "Cadastrar nadadores", num=1, valor=cadastrar_nadadores), Opcao("emitir_relatorio", "Emitir Relatório", num=2, valor=relatorio), Opcao("sair", "Sair", num=0, tipo="exit")])
        print("-----ACNE Natação-----\nMENU\n--------------------")
        for opt in opcoes.opcoes:
            print(f"{opt.num} - {opt.mostrar}")
        stdin = input("\n> ")
        os.system('clear')
        try:
            stdin = validar_numero(stdin)
            if stdin not in opcoes.disponiveis(): raise CustomException("Opção inválida")
            opt = opcoes.get_opt(stdin)
            match opt.tipo:
                case "func":
                    opt.valor(nadadores)
                case "exit":
                    break
        except CustomException as e:
            input(f"[ERRO] - {e.mensagem}")

menu_principal()

