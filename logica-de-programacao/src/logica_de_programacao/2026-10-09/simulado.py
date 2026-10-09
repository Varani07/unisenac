# Matheus Cirne Varani

import os


class CustomException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas = []
        self.media_aproveitamento = 0
        self.conceito = ""
        self.aprovado = None

    def adicionar_nota(self, nota: str) -> None:
        if len(self.notas) > 4:
            raise CustomException("Capacidade máxima de notas registradas.")
        else:
            try:
                nota = float(nota)
            except:
                raise CustomException("Valor não reconhecido.")
            if nota < 0 or nota > 10:
                raise CustomException("Nota inválida.")
            else:
                self.notas.append(nota)

    def calcular_conceito(self) -> str:
        if len(self.notas) != 4:
            raise CustomException("Todas notas precisam ser registradas antes de calcular o conceito.")
        else:
            self.media_aproveitamento = (self.notas[0] + self.notas[1] * 2 + self.notas[2] * 3 + self.notas[3]) / 7

            if self.media_aproveitamento >= 9:
                self.conceito = "A"
            elif self.media_aproveitamento >= 7.5:
                self.conceito = "B"
            elif self.media_aproveitamento >= 6:
                self.conceito = "C"
            elif self.media_aproveitamento >= 4:
                self.conceito = "D"
            else:
                self.conceito = "E"

            return self.conceito

    def mensagem(self) -> str:
        match self.conceito:
            case "A" | "B" | "C": 
                self.aprovado = True
                return "ALUNO APROVADO!"
            case _: 
                self.aprovado = False
                return "ALUNO REPROVADO!"

def cadastrar_aluno(alunos: list[Aluno]):
    nome = ""
    main_loop = True
    while main_loop:
        os.system("clear")
        print("\n=== CADASTRO ===\n\n")
        if nome == "":
            nome = input("> Nome: ").strip()
            if nome == "": break
            else:
                try:
                    if nome in [a.nome for a in alunos]:
                        raise CustomException("Aluno já cadastrado.")
                except CustomException as e:
                    input(f"[ERRO] - {e.message}")
                    nome = ""
                    continue
            aluno = Aluno(nome)
        else: print(f"> Nome: {nome}")
        while len(aluno.notas) != 4:
            for i, n in enumerate(aluno.notas, 1):
                print(f"> {i}º Nota: {n}")
            nota = input(f"> {len(aluno.notas) + 1}º Nota: ")
            if nota == "":
                main_loop = False
                break
            try:
                aluno.adicionar_nota(nota)
                break
            except CustomException as e:
                input(f"[ERRO] - {e.message}")
                break
        if len(aluno.notas) == 4:
            aluno.calcular_conceito()
            alunos.append(aluno)
            nome = ""
            input("\nAluno cadastrado com sucesso!")

def ver_alunos(alunos: list[Aluno]):
    if len(alunos) == 0:
        input("\nNenhum aluno cadastrado...\n")
    else:
        for aluno in alunos:
            print(f"\nNome: {aluno.nome}")
            for i, nota in enumerate(aluno.notas, 1):
                if i != 4:
                    print(f"{i}º Nota: {round(nota, 1)}")
                else:
                    print(f"Média dos exercícios: {round(nota, 1)}")
            print(f"Média de aproveitamento: {round(aluno.media_aproveitamento, 1)}")
            print(f"Conceito: {aluno.conceito}")
            print(f"Mensagem: {aluno.mensagem()}")
        input()

def filtrar_alunos_aprovados(alunos: list[Aluno]):
    ver_alunos([aluno for aluno in alunos if aluno.aprovado == True])

def filtrar_alunos_reprovados(alunos: list[Aluno]):
    ver_alunos([aluno for aluno in alunos if aluno.aprovado == False])

alunos = []
opcoes = [("Cadastrar Aluno", cadastrar_aluno), ("Ver Todos os Alunos", ver_alunos), ("Ver Alunos Aprovados", filtrar_alunos_aprovados), ("Ver Alunos Reprovados", filtrar_alunos_reprovados), ("Sair", None)]

while True:
    os.system("clear")
    print("\n=== MENU ===\n\n")
    for i, opt in enumerate(opcoes, 1):
        print(f"{i} - {opt[0]}")
    resposta = input("\n> ")
    os.system("clear")
    try:
        try:
            resposta = int(resposta)
        except:
            raise CustomException("Valor não reconhecido.")
        if resposta < 1 or resposta > len(opcoes):
            raise CustomException("Opção inválida.")
        if resposta == len(opcoes):
            break
        resposta -= 1 
        opcoes[resposta][1](alunos)
        
    except CustomException as e:
        input(f"\n[ERRO] {e.message}")
    

