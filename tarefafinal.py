import datetime
import json
class Profissional:
    def __init__(self,nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome


    def get_especialidade(self):
        return self.__especialidade


    def get_sala(self):
        return  self.__sala 




class Visitante:
    def __init__(self,nome, documento):
        self.__nome = nome
        self.__documento = documento
       
    def get_nome(self):
        return self.__nome


    def get_documento(self):
        return self.__documento


class Visita:
    def __init__(self, visitante, profissional, data_entrada):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = data_entrada
       

    def get_visitante(self):
        return self.__visitante


    def get_profissional(self):
        return self.__profissional


    def get_data_entrada(self):
        return self.__data_entrada


def aaaa():
    visitante = input ("Qual o nome do visitante?")
    for visita in l_visitantes:
        if visitante == visita.get_visitante():
            print ("nome: " , visita.get_visitante()) 


l_visitantes = [
    Visitante("Carlos", "123456789"),
    Visitante("Ana", "987654321"),
    Visitante("Pedro", "456789123")
]


l_profissionais = [
    Profissional("João", "Cardiologia", "Sala 1"),
    Profissional("Maria", "Dermatologia", "Sala 2"),
    Profissional("Luiza", "Ortopedia", "Sala 3")
]

    
dict_visita ={}


def cadastrar_profissional():
    nome = input("Nome do profissional: ")
    especialidade = input("Especialidade do profissional: ")
    sala = input("Sala onde o profissional atende: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")


def cadastrar_visitante():
    nome = input("Nome do visitante: ")
    documento = input("Documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    print("Visitante cadastrado com sucesso!")



def localizar_profissional():
    opcao = input("1 - Localizar por nome\n2 - Localizar por especialidade\nEscolha uma opção: ")
    if opcao == "1":
        nome = input("Nome do profissional: ")
        profissionais_encontrados = [profissional for profissional in l_profissionais if profissional.get_nome() == nome]
    elif opcao == "2":
        especialidade = input("Especialidade do profissional: ")
        profissionais_encontrados = [profissional for profissional in l_profissionais if profissional.get_especialidade == especialidade]
    else:
        print("Opção inválida!")
        return

    if len(profissionais_encontrados) > 0:
        for profissional in profissionais_encontrados:
            print(f"Nome: {profissional.get_nome()}")
            print(f"Especialidade: {profissional.get_especialidade()}")
            print(f"Sala: {profissional.get_sala()}")
    else:
        print("Nenhum profissional encontrado com os critérios informados.")

    


def registrar_visita():
    if len(l_visitantes) == 0:
        print("Nenhum visitante cadastrado.")
        return
    if len(l_profissionais) == 0:
        print("Nenhum profissional cadastrado.")
        return

    print("Selecione o visitante:")
    for i, visitante in enumerate(l_visitantes):
        print(f"{i + 1}. Nome: {visitante.get_nome()}, Documento: {visitante.get_documento()}")
    visitante_index = int(input("Escolha o número do visitante: ")) - 1

    print("Selecione o profissional:")
    for i, profissional in enumerate(l_profissionais):
        print(f"{i + 1}. Nome: {profissional.get_nome()}, Especialidade: {profissional.get_especialidade()}, Sala: {profissional.get_sala()}")
    profissional_index = int(input("Escolha o número do profissional: ")) - 1

    visitante = l_visitantes[visitante_index]
    profissional = l_profissionais[profissional_index]
    hora_entrada = datetime.datetime.now().strftime("%H:%M:%S")
    sala = profissional.get_sala()
    if visitante.get_documento() not in l_visitantes:
        dict_visita[visitante.get_documento()]= {
        "profissional": profissional.get_nome(),
        "hora_entrada": hora_entrada,
        "sala": sala 
        }
    print("Visita registrada com sucesso!")
    print (dict_visita)


def relatorio_conferencia():
    if len(l_profissionais) == 0:
        print("Nenhum profissional cadastrado.")
        return

    print("Selecione o profissional:")
    for i, profissional in enumerate(l_profissionais):
        print(f"{i + 1}. Nome: {profissional.get_nome()}, Especialidade: {profissional.get_especialidade()}, Sala: {profissional.get_sala()}")
    profissional_index = int(input("Escolha o número do profissional: ")) - 1

    profissional = l_profissionais[profissional_index]
    print(f"Relatório de conferência para o profissional {profissional.get_nome()}:\n")
    for visitante_documento, visita in dict_visita.items():
        for visitante, profissional in dict_visita.items():
            print(f"Profissional: {profissional}; Visitante: {visitante}, {visita}")



def gerar_arquivo_registros():
    if len(dict_visita) == 0:
        print("Nenhum registro de visita encontrado.")
        return

    registros = {}
    for visitante_documento in dict_visita.items():
        for nome_profissional, visitante_documento in dict_visita.items():
            hora_entrada = dict_visita["hora_entrada"]
            sala = dict_visita["sala"]
            registros[visitante_documento] = {
                "nome_profissional": nome_profissional,
                "hora_entrada": hora_entrada,
                "sala": sala
            }

    with open("registros.json", "w") as file:
        json.dump(registros, file, indent=4)
    print("Arquivo de registros gerado com sucesso!")



def ler_arquivos():
    print(l_profissionais)
    with open("profissionais.txt", "r") as f:
        profissionais = l_profissionais
        linhas = f.readlines()
        for linha in linhas:
            atributos = linha.split(":")
            nome = atributos[0]
            especialidade = atributos[1]
            sala = atributos[2]
            profissional = Profissional(nome, especialidade, sala)
            profissionais.append(profissional)
        print(l_profissionais)
    
    with open("visitantes.txt", "r") as f:
        visitantes = l_visitantes
        linhas = f.readlines()
        for linha in linhas:
            atributos = linha.strip().split(";")
            nome = atributos[0]
            documento = atributos[1]
            visitante = Visitante(nome, documento)
            visitantes.append(visitante)
            
    return 



   



   


while True:
    print("""======================
MENU
======================
1- Cadastrar Profissional
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Relatório de Conferência
6- Gerar arquivo de Registros do dia
7- Ler arquivos profissionais / visitantes
""")
    escolha = input("Escolha: ")
    if escolha == "1":
        cadastrar_profissional()
    if escolha == "2":
        cadastrar_visitante()
    if escolha == "3":
        localizar_profissional()
    if escolha == "4":
        registrar_visita()
    if escolha == "5":
        relatorio_conferencia()
    if escolha == "6":
        gerar_arquivo_registros()
    if escolha == "7":
        ler_arquivos()
    
