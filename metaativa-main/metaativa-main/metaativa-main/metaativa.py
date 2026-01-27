# metaativa
import json

usuarios = {}
perfis = {}
comunidades = []

# --- Manipulação de arquivos (JSON) ---
def carregar_tudo():
    global usuarios, perfis, comunidades
    
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = {linha.strip().split(",")[0]: linha.strip().split(",")[1] 
                       for linha in f}
    except FileNotFoundError:
        pass

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

    try:
        with open("comunidades.json", "r") as f:
            comunidades = json.load(f)
    except FileNotFoundError:
        pass

def salvar_dados():
    with open("usuarios.txt", "w") as f:
        f.writelines(f"{u},{s}\n" for u, s in usuarios.items())

    with open("perfis.txt", "w") as f:
        f.writelines(f"{u},{d['idade']},{d['atividades']},{d['objetivo']}\n" 
                    for u, d in perfis.items())

    with open("comunidades.json", "w") as f:
        json.dump(comunidades, f, indent=4)

carregar_tudo()

def criar_comunidade():
    try:
        print("\nCriar Comunidade")
        comunidade = {
            'nome': input("Nome da comunidade: "),
            'esporte': input("Esporte/Atividade (ex: corrida, yoga): "),
            'local': input("Local (ex: Parque Central): "),
            'dias': input("Dias (ex: seg,qua,sex): ").split(','),
            'horario': input("Horário (ex: 18:30): "),
            'membros': []
        }
        comunidades.append(comunidade)
        print(f"\nComunidade '{comunidade['nome']}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar comunidade: {e}")

def menu_principal():
    while True:
        try:
            print("\n METAATIVA ")
            print("1 - Cadastrar\n2 - Login\n3 - Sair")
            opcao = input("Escolha uma opção (1-3): ")
            
            if opcao == "1":
                nome = input("Digite seu nome de usuário: ")
                if nome in usuarios:
                    print("Usuário já existe!")
                else:
                    usuarios[nome] = input("Digite sua senha: ")
                    perfis[nome] = {"nome": nome, "idade": "", "atividades": "", "objetivo": ""}
                    print("Cadastro realizado!")
                    salvar_dados()
            
            elif opcao == "2":
                nome = input("Usuário: ")
                senha = input("Senha: ")
                
                if nome in usuarios and usuarios[nome] == senha:
                    print(f"\nBem-vindo, {nome}!")
                    menu_logado(nome)
                else:
                    print("Usuário não cadastrado ou senha errada")
            
            elif opcao == "3":
                print("Você saiu da plataforma.")
                break
            else:
                print("Opção inválida!")
        
        except KeyboardInterrupt:
            print("\nOperação interrompida. Use a opção 3 para sair.")
            break
        except Exception as e:
            print(f"Erro: {e}")

def menu_logado(nome):
    while True:
        try:
            print("\n MENU PRINCIPAL ")
            print("1 - Editar perfil\n2 - Criar comunidade\n3 - Ver comunidades\n4 - Sair")
            escolha = input("Escolha uma opção (1-4): ")
            
            if escolha == "1":
                editar_perfil(nome)
            elif escolha == "2":
                criar_comunidade()
                salvar_dados()
            elif escolha == "3":
                visualizar_comunidades(nome)
            elif escolha == "4":
                print("Saiu da conta")
                break
            else:
                print("Opção inválida!")
        
        except Exception as e:
            print(f"Erro: {e}")

def editar_perfil(nome):
    opcoes = {"1": "nome", "2": "idade", "3": "atividades", "4": "objetivo"}
    for key, label in opcoes.items():
        print(f"{key} - {label.capitalize()}: {perfis[nome][label]}")
    print("5 - Voltar")
    
    escolha = input("O que deseja editar? (1-5): ")
    if escolha in opcoes:
        perfis[nome][opcoes[escolha]] = input(f"Novo {opcoes[escolha]}: ")
        salvar_dados()
    elif escolha != "5":
        print("Opção inválida!")

def visualizar_comunidades(nome):
    if not comunidades:
        print("\nNenhuma comunidade disponível.")
        return
    
    print("\n Comunidades Disponíveis ")
    for i, com in enumerate(comunidades, 1):
        print(f"{i}. {com['nome']} - {com['esporte']} | Local: {com['local']}")
        print(f"   Dias: {','.join(com['dias'])} às {com['horario']}")

menu_principal()
