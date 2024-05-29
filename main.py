from recursos.funcoes import limparTela, aguarde, verificaBancoDeDados

listaDesaparecidos = []
limparTela()
print("Bem-Vindo ao Sistema de Desaparecidos!")
print( verificaBancoDeDados() )
aguarde(1)
while True:
    limparTela()
    print("(0) Sair")
    print("(1) Cadastro de Desaparecidos")
    print("(2) Lista de Desaparecidos")
    print("(3) Excluir Desaparecidos")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome do Desaparecido: ")
        telefone = input("Telefone do Desaparecido: ")
        while True:
            try:
                idade = int(input("Idade: "))
                break
            except:
                print("Idade inválida!")
        registro  = nome + " - " + telefone + " - " + str(idade)
        #listaDesaparecidos.append(registro) # RAM
        # w - write, r - read, a - append  
        # encoding - utf8 - iso8859-1- ....
        arquivo = open("database.mrs", "a", encoding="utf-8") 
        arquivo.write(registro + "\n")
        arquivo.close()
        
        print("Dados Salvos com Sucesso!")
        aguarde(2)
        
        
    elif opcao == "2":
        print("Lista de Desaparecidos:")
        arquivo = open("database.mrs", "r" , encoding="utf-8")
        # readlines devolve os dados no formato de lista
        # read devolve em formato de texto (string)
        # readline devolve somente a primeira linha
        listaDesaparecidos = arquivo.readlines() 
        arquivo.close()
        dados = ""
        for posicao, item in enumerate(listaDesaparecidos):
            dados  = dados  + str(posicao + 1 ) + ' - ' + item
        
        print(dados)
        input("Press enter to continue...")
        
        
    elif opcao == "3":
        print("Lista de Desaparecidos:")
        arquivo = open("database.mrs", "r" , encoding="utf-8")
        listaDesaparecidos = arquivo.readlines() 
        arquivo.close()
        dados = ""
        for posicao, item in enumerate(listaDesaparecidos):
            dados  = dados  + str(posicao + 1 ) + ' - ' + item
        print(dados)
        
        while True:
            try:
                deletarPosicao = int(input("Informe a posição a ser excluída: "))
                break
            except:
                print("Necessário informar uma posição numérica!")
        
        if deletarPosicao > 0: 
            try:
                listaDesaparecidos.pop(deletarPosicao-1)
                print("Registro Excluído com Sucesso!")
                arquivo = open("database.mrs", "w", encoding="utf-8") 
                for item in listaDesaparecidos:
                    arquivo.write(item)
                arquivo.close()
            except:
                print("Essa posição não existe!")
        else:
            print("A posição não pode ser zero ou negativo!")        
        
        
        input("Press enter to continue...")
    else:
        print("Opção Inválida! Tente novamente...")
        aguarde(2)

print("O sistema está sendo fechado!....")
    
    
    
    
