# metaativa
#protótipo de uma rede social que tem o objetivo de conectar as pessoas através dos exercícios físicos.
import json
# Dicionário para armazenar usuários (nome: senha)
usuarios = {}

# Dicionário para o perfil do usuário
perfis = {}  # armazena vários perfis

# Lista para armazenar comunidades
comunidades = []

# --- Manipulação de arquivos (JSON) ---
def carregar_tudo():

    # Carregar usuários
    try:
        with open("usuarios.txt", "r") as f:
            for linha in f:
                usuario, senha = linha.strip().split(",")
                usuarios[usuario] = senha
    except FileNotFoundError:
        pass

    # Carregar perfis
    try:
        with open("perfis.txt", "r") as f:
            for linha in f:
                dados = linha.strip().split(",")
                if len(dados) == 4:
                    perfis[dados[0]] = {
                        "nome": dados[0],
                        "idade": dados[1],
                        "atividades": dados[2],
                        "objetivo": dados[3]
                    }
    except FileNotFoundError:
        pass

    # Carregar comunidades 
    try:
        with open("comunidades.json", "r") as f:
            comunidades.extend(json.load(f))
    except FileNotFoundError:
        pass

def salvar_dados():
    # Salvar usuários
    with open("usuarios.txt", "w") as f:
        for usuario, senha in usuarios.items():
            f.write(f"{usuario},{senha}\n")

    # Salvar perfis
    with open("perfis.txt", "w") as f:
        for usuario, dados in perfis.items():
            f.write(f"{usuario},{dados['idade']},{dados['atividades']},{dados['objetivo']}\n")

    # Salvar comunidades
    with open("comunidades.json", "w") as f:
        json.dump(comunidades, f, indent=4)

# --- Carregar os dados ao iniciar o programa ---
carregar_tudo()

# criar crud para adicionar os membros dentro da comunidade


def criar_comunidade():
    try:
        print("\nCriar Comunidade")
        nome = input("Nome da comunidade: ")
        esporte = input("Esporte/Atividade (ex: corrida, yoga): ")
        local = input("Local (ex: Parque Central): ")
        dias = input("Dias (ex: seg,qua,sex): ").split(',')
        horario = input("Horário (ex: 18:30): ")
        
        comunidade = {
            'nome': nome,
            'esporte': esporte,
            'local': local,
            'dias': dias,
            'horario': horario,
            'membros': []
        }
        # A comunidade criada entra na lista de comunidades
        comunidades.append(comunidade)
        print(f"\nComunidade '{nome}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar comunidade: {e}")
        
        
        def menu() :
            print("\n METAATIVA ")
            print("1 - Cadastrar")
            print("2 - Login")
            print("3 - Sair")
        
            opcao = input("Escolha uma opção (1-3): ")

# Menu principal
while True:
    try:
        print("\n METAATIVA ")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção (1-3): ")
        
        if opcao == "1":
            try:
                # Cadastro
                nome = input("Digite seu nome de usuário: ")
                if nome in usuarios:
                    print("Usuário já existe!")
                else:
                    senha = input("Digite sua senha: ")
                    usuarios[nome] = senha # O nome digitado é associado a uma senha e ambos entram no dicionário "usuarios" criando uma relação key value
                    perfis[nome] = { # Este mesmo nome digitado entra no dicionário perfis e este nome tem várias informações key value, ou seja, é um dicionário dentro de outro
                        "nome": nome,
                        "idade": "",
                        "atividades": "",
                        "objetivo": ""
                    }
                    print("Cadastro realizado!")
            except Exception as e:
                print(f"Erro durante cadastro: {e}")
        
        elif opcao == "2":
            try:
                # Login
                nome = input("Usuário: ")
                senha = input("Senha: ")
                
                if nome in usuarios and usuarios[nome] == senha:
                    print(f"\nBem-vindo, {nome}!")
                    
                elif nome not in usuarios or senha not in usuarios[nome]:
                    print("Usuário não cadastrado ou senha errada")
                    #return funcção menu
                    # chegando aqui, deveria voltar para o menu inicial #
                    
                    while True:
                        try:
                            print("\n MENU PRINCIPAL ")
                            print("1 - Editar perfil")
                            print("2 - Criar comunidade")
                            print("3 - Ver e entrar em comunidades")
                            print("4 - Sair da conta")
                            
                            escolha_aba_app = input("Escolha uma opção (1-4): ")
                            
                            if escolha_aba_app == "1":
                                try:
                                    # Editar perfil
                                    print("\n Editar Perfil ")
                                    print(f"1 - Nome: {perfis[nome]['nome']}")# cada parte dessa acessa o dicionário "perfis", entra no elemento "nome" e...
                                    print(f"2 - Idade: {perfis[nome]['idade']}")# no elemento nome busca algum outro elemento já que "nome" també é um dicionário
                                    print(f"3 - Atividades de interesse: {perfis[nome]['atividades']}")
                                    print(f"4 - Objetivo: {perfis[nome]['objetivo']}")
                                    print("5 - Voltar")
                                    
                                    escolha_editar_perfil = input("O que deseja editar? (1-5): ")
                                    
                                    if escolha_editar_perfil == "1":
                                        perfis[nome]['nome'] = input("Novo nome: ")
                                    elif escolha_editar_perfil == "2":
                                        perfis[nome]['idade'] = input("Nova idade: ")
                                    elif escolha_editar_perfil == "3":
                                        perfis[nome]['atividades'] = input("Novas atividades: ")
                                    elif escolha_editar_perfil == "4":
                                        perfis[nome]['objetivo'] = input("Novo objetivo: ")
                                    elif escolha_editar_perfil == "5":
                                        continue
                                    else:
                                        print("Opção inválida!")
                                except Exception as e:
                                    print(f"Erro ao editar perfil: {e}")
                            
                            elif escolha_aba_app == "2":
                                try:
                                    criar_comunidade()# executa a função criar_comunidade que foi criada lá em cima
                                except Exception as e:
                                    print(f"Erro ao criar comunidade: {e}")
                            
                            elif escolha_aba_app == "3":
                                try:
                                    if not comunidades:# if not verifica a não existencia de comunidades
                                        print("\nNenhuma comunidade disponível.")
                                    else:
                                        print("\n Comunidades Disponíveis ")
                                        for i, com in enumerate(comunidades, 1):
                                            print(f"{i}. {com['nome']} - {com['esporte']}")
                                            print(f"   Local: {com['local']}")
                                            print(f"   Dias: {','.join(com['dias'])} às {com['horario']}")
                                            print(f"   Membros: {com['membros']}")
                                        
                                        num = input("Digite o número da comunidade para entrar (ou 0 para voltar): ")
                                        
                                        #aqui o usuário deveria entrar em uma comunidade, mas não conseguimos desenvolver
                                        
                                except Exception as e:
                                    print(f"Erro ao visualizar comunidades: {e}")
                            
                            elif escolha_aba_app == "4":
                                print("Saiu da conta")
                                break
                            
                            else:
                                print("Opção inválida!")
                        
                        except ValueError:
                            print("Por favor, digite um número válido.")
                        except Exception as e:
                            print(f"Erro inesperado: {e}")
                
                else:
                    print("Usuário não cadastrado ou senha errada")
            
            except Exception as e:
                print(f"Erro durante login: {e}")
        
        elif opcao == "3":
            print("Você saiu da plataforma.")
            break
        
        else:
            print("Opção inválida!")
    
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário. Use a opção 3 para sair corretamente.")
        break
    except Exception as e:
        print(f"Erro inesperado no menu principal: {e}")
