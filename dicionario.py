#Armazenar os usuários
banco_usuarios = []

# Cadastrar um usuário
def cadastrar_usuario(campos_obrigatorios):
    usuario = {}
    
    # Preenche os campos obrigatórios
    for campo in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    while True:
        campo_adicional = input("Digite um campo adicional (ou 'sair' para finalizar): ")
        if campo_adicional.lower() == 'sair':
            break
        valor_adicional = input(f"Digite o valor para o campo '{campo_adicional}': ")
        usuario[campo_adicional] = valor_adicional
    
    # Adicionar o usuário ao banco de dados 
    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

# Imprimir os usuários
def imprimir_usuarios(*args, **kwargs):
    if not args and not kwargs:
        # Se nada for fornecido, imprime todos os usuários
        for usuario in banco_usuarios:
            print(usuario)
    elif args:
        # Se nomes foram fornecidos, imprime os usuários com esses nomes
        for nome in args:
            for usuario in banco_usuarios:
                if usuario.get('nome') == nome:
                    print(usuario)
    elif kwargs:
        resultados = []
        # Se os campos foram fornecidos, filtra os usuários que atendem a essas condições
        for usuario in banco_usuarios:
            satisfaz_condicoes = True
            for campo, valor in kwargs.items():
                if campo not in usuario or usuario[campo] != valor:
                    satisfaz_condicoes = False
                    break
            if satisfaz_condicoes:
                resultados.append(usuario)
        for usuario in resultados:
            print(usuario)

# Função principal do programa
def main():
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(',')
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            sub_opcao = input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nEscolha uma sub-opção: ")
            if sub_opcao == '1':
                imprimir_usuarios()
            elif sub_opcao == '2':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                imprimir_usuarios(*nomes)
            elif sub_opcao == '3':
                campos = input("Digite os campos separados por vírgula: ").split(',')
                valores = input("Digite os valores separados por vírgula: ").split(',')
                kwargs = dict(zip(campos, valores))
                imprimir_usuarios(**kwargs)
            elif sub_opcao == '4':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                campos = input("Digite os campos separados por vírgula: ").split(',')
                valores = input("Digite os valores separados por vírgula: ").split(',')
                kwargs = dict(zip(campos, valores))
                imprimir_usuarios(*nomes, **kwargs)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
