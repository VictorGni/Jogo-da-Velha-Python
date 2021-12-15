import os

#Função para cirar um novo jogador
def criaNovoJogador():
    nome = input("Digite o nome de usuário do jogador: ")
    nome = nome.upper()
#Caso o jogador já exista será redirecionado para o menu e exibida uma mensagem
    if os.path.isfile("./PROJETO/./historico/"+ nome + ".txt"):
        print()
        print("------------------------------------")
        print("Jogador ja registrado!!")
        print("------------------------------------")
        print()

# Criação de um usuário novo e adicionando no banco de dados
    else:    
        arquivo = open("./PROJETO/./historico/" +  nome + ".txt", "w")
        n=0
        arquivo.write("%d\n"%n)
        arquivo.write("%d"%n)
        arquivo.close()
        print()
        print("------------------------------------")
        print("Jogador",nome,"criado!!")
        print("------------------------------------")
        print()
        
# Função paga excluir o jogador
def excluirJogador():
    nome = input("Digite o nome a ser excluido: ")
    nome = nome.upper()
    if os.path.isfile("./PROJETO/./historico/" + nome + ".txt"):
        print()
        print("------------------------------------")
        print("Exluido o jogador",nome)
        print("------------------------------------")
        print()
        os.remove("./PROJETO/./historico/" + nome + ".txt")
    else:
        print()
        print("------------------------------------")
        print("O jogador inserido não existe !!")
        print("------------------------------------")    


# Função ler histórico realiza a leitura o número de vitórias e número de derrotas do jogador inserido
def lerHistorico():
    nome = input("Digite o nome do jogador: ")
    nome = nome.upper()
# Comando verifica se existe o arquivo solicitado, caso sim, ele realiza a leitura e exibe o número de vitórias e derrotas de acordo com index
    if os.path.isfile("./PROJETO/./historico/" + nome + ".txt"):
        arquivo = open("./PROJETO/./historico/" + nome + ".txt", "r")
        historico = arquivo.readlines()
        vitorias = int(historico[0])
        derrota = int(historico[1])
        print()
        print("------------------------------------")
        print("Vitórias:",vitorias,"   Derrotas:",derrota)
        print("------------------------------------")
        print()
    else:
        print()
        print("------------------------------------")
        print("Usuário não existe!!")
        print("------------------------------------")
        print()

# Função "partida" realiza a criação da matriz e a lógica do jogo
def partida():
    
    matriz = [
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "],
        [" "," "," "," "," "]
        ]

# Função para imprimir o tabuleiro por meio da matriz
    def imprimirJogo():
        tabuleiro = """
         {} | {} | {} | {} | {}
        ---+---+---+---+---
         {} | {} | {} | {} | {}   
        ---+---+---+---+---
         {} | {} | {} | {} | {}
        ---+---+---+---+---
         {} | {} | {} | {} | {}
        ---+---+---+---+---
         {} | {} | {} | {} | {}
        """.format(matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3],matriz[0][4], 
        matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3],matriz[1][4],
        matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3],matriz[2][4],
        matriz[3][0],matriz[3][1],matriz[3][2],matriz[3][3],matriz[3][4],
        matriz[4][0],matriz[4][1],matriz[4][2],matriz[4][3],matriz[4][4])
        print(tabuleiro)



   
# Função para validar os jogadores antes de iniciar a partida
    def jogadores():
        print()
        print("Ensira os nomes dos jogadores antes de inicar a partida!")
        print()
        nome =input("Digite o nome do jogador 1 (x): ")
        nome = nome.upper()
    # Condição para verificar se o arquivo existe no BD
        if os.path.isfile("./PROJETO/./historico/" + nome + ".txt"):
            nome2 = input("Digite o nome do jogar 2 (O): ")
            nome2 = nome2.upper()
            if os.path.isfile("./PROJETO/./historico/" + nome2 + ".txt"):
                imprimirJogo()
    # Depois de validado função envia os nomes para o def jogo
                jogo(nome,nome2)
    # Caso a função não encontre o nome será direcionado para a criação do mesmo            
            else:
                print()
                print("------------------------------------")
                print("Esse jogador não existe!!")
                print("Criar novo jogador")
                print("------------------------------------")
                main()
        else:
                print()
                print("------------------------------------")
                print("Esse jogador não existe!!")
                print("Criar novo jogador")
                print("------------------------------------")
                main() 

                

# Essa função faz a lógica do jogo
# A mesma recebe dois nomes para indicar de qual é a vez de cada jogador  
    def jogo(nome,nome2):
        jogadas = 0
        while jogadas<25:
            # Condição para verificar qual a vez de cada jogador
            # A lógica é a mesma porem está separado por jogador 1 e 2
            if jogadas%2==0:
                # While para retornar caso o espaço já esteja preenchido
                while True:
                    print("É a vez do jogador %s"%nome)
                    # While para que o jogador 1 digite a linha maneira correta
                    while True:
                        linha = int(input("Digite o número da linha: "))   
                    
                        if linha >4 or linha<0:
                            print("O range da linha é de 0 a 4, digite a linha novamente")
                        
                        if linha<=4 and linha >=0:
                            break
                    # While para o jogador digitar a coluna da forma correta
                    while True:
                        coluna = int(input("Digite o número da coluna: "))
                        if coluna > 4 or coluna<0:
                            print("O range da coluna é de 0 a 4, digite a coluna novamente")
                            
                        if coluna <=4 and coluna>=0:
                            break
                    # Condição para verificar se o espaço ja está preenchido
                    if matriz[linha][coluna]=="X" or matriz[linha][coluna]=="O" :
                        print("Estas cordenadas já foram preenchidas")

                    # Caso não esteja preenchido ele marca a posição e chama a função para printar o tabuleiro e a função para verificar se o mesmo venceu    
                    else:
                        matriz[linha][coluna]= "X"
                        jogadas+=1
                        imprimirJogo()
                    # Lógica para ver se o jogador 1 venceu antes de ser a vez do jogador 2
                        vencedor1(nome,nome2)                                   
                        break

            # Segunda condição para vericar a vez do jogador
            # Lógicas de condição são as mesmas do jogador 1 acima
            if jogadas%2!=0:
                while True:
                    print("É a vez do jogador %s"%nome2)
                    # While para que o jogador 2 digite a linha maneira correta
                    while True:
                        linha = int(input("Digite o número da linha: "))   
                
                        if linha >4 or linha<0:
                            print("O range da linha é de 0 a 4, digite a linha novamente")
                        
                        if linha<=4 and linha >=0:
                            break
                    # While para que o jogador digite a coluna da maneira correta
                    while True:
                        coluna = int(input("Digite o número da coluna: "))
                        if coluna > 4 or coluna<0:
                            print("O range da coluna é de 0 a 4, digite a coluna novamente")
                            
                        if coluna <=4 and coluna>=0:
                            break
                    # Condição para verificar se o espaço está preenchido        
                    if matriz[linha][coluna]=="X" or matriz[linha][coluna]=="O":
                        print("Estas cordenadas já foram preenchidas")

                    # Caso não esteja, é marcado a posição e chama outras funções
                    else: 
                        matriz[linha][coluna] ="O"
                        jogadas+=1
                        imprimirJogo()
                        vencedor2(nome2,nome)
                        break 
            # Condição caso o jogo empate 
            if jogadas == 24:
                print("O jogo empatou!!")
                main()


    # Lógica para ver se o jogador 1 venceu a partida, função recebe duas variaveis (nomes) que será utilizado no banco de dados               
    def vencedor1(nome,nome2):
        # Condição para verificar as linhas do jogador 1
        if matriz[0][0]=="X" and  matriz[0][1]=="X" and  matriz[0][2]=="X" and  matriz[0][3]=="X":
            # Caso a sequência seja preenchida um print na tela mostrara o nome do jogador vencedor
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            # E enviara para função reset o nome do vencedor(x) e o nome do perdedor(o)
            reset(nome,nome2)
        # Isso se repete para todas as condições
        elif matriz[0][4]=="X" and  matriz[0][1]=="X" and  matriz[0][2]=="X" and  matriz[0][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[1][4]=="X" and  matriz[1][1]=="X" and  matriz[1][2]=="X" and  matriz[1][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[1][0]=="X" and  matriz[1][1]=="X" and  matriz[1][2]=="X" and  matriz[1][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[2][0]=="X" and  matriz[2][1]=="X" and  matriz[2][2]=="X" and  matriz[2][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[2][4]=="X" and  matriz[2][1]=="X" and  matriz[2][2]=="X" and  matriz[2][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[3][4]=="X" and  matriz[3][1]=="X" and  matriz[3][2]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[3][0]=="X" and  matriz[3][1]=="X" and  matriz[3][2]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][0]=="X" and  matriz[4][1]=="X" and  matriz[4][2]=="X" and  matriz[4][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][4]=="X" and  matriz[4][1]=="X" and  matriz[4][2]=="X" and  matriz[4][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

        # Condição para verificar as colunas do jogador 1
        elif matriz[0][0]=="X" and  matriz[1][0]=="X" and  matriz[2][0]=="X" and  matriz[3][0]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][0]=="X" and  matriz[1][0]=="X" and  matriz[2][0]=="X" and  matriz[3][0]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[0][1]=="X" and  matriz[1][1]=="X" and  matriz[2][1]=="X" and  matriz[3][1]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][1]=="X" and  matriz[1][1]=="X" and  matriz[2][1]=="X" and  matriz[3][1]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[0][2]=="X" and  matriz[1][2]=="X" and  matriz[2][2]=="X" and  matriz[3][2]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][2]=="X" and  matriz[1][2]=="X" and  matriz[2][2]=="X" and  matriz[3][2]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[0][3]=="X" and  matriz[1][3]=="X" and  matriz[2][3]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][3]=="X" and  matriz[1][3]=="X" and  matriz[2][3]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[4][4]=="X" and  matriz[1][4]=="X" and  matriz[2][4]=="X" and  matriz[3][4]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        elif matriz[0][4]=="X" and  matriz[1][4]=="X" and  matriz[2][4]=="X" and  matriz[3][4]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)


       # Condições para verificar todas as sequências diagonais do jogador 1
        elif matriz[0][3]=="X" and  matriz[1][2]=="X" and  matriz[2][1]=="X" and  matriz[3][0]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
        
        elif matriz[1][4]=="X" and  matriz[2][3]=="X" and  matriz[3][2]=="X" and  matriz[4][1]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
            
        elif matriz[1][0]=="X" and  matriz[2][1]=="X" and  matriz[3][2]=="X" and  matriz[4][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

        elif matriz[0][1]=="X" and  matriz[1][2]=="X" and  matriz[2][3]=="X" and  matriz[3][4]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

        elif matriz[0][0]=="X" and  matriz[1][1]=="X" and  matriz[2][2]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

        elif matriz[4][4]=="X" and  matriz[1][1]=="X" and  matriz[2][2]=="X" and  matriz[3][3]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

        elif matriz[0][4]=="X" and  matriz[1][3]=="X" and  matriz[2][2]=="X" and  matriz[3][1]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)
    
        elif matriz[4][0]=="X" and  matriz[1][3]=="X" and  matriz[2][2]=="X" and  matriz[3][1]=="X":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome)
            print("------------------------------------")
            reset(nome,nome2)

    # Lógica para ver se o jogador 2 venceu a partida, função recebe duas variaveis (nomes) que será utilizado no banco de dados 
    def vencedor2(nome2,nome):
        
        # Condição para verificar as linhas do jogador 2
        if matriz[0][0]=="O" and  matriz[0][1]=="O" and  matriz[0][2]=="O" and  matriz[0][3]=="O":
            # Se acondição for verdadeira o programa irá printar o nome do vencedor
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            # E envia o nome do vencedor para reset como "x" e do perdedor como "y"
            reset(nome2,nome)
        # Isso se repete para todas as condições
        elif matriz[0][4]=="O" and  matriz[0][1]=="O" and  matriz[0][2]=="O" and  matriz[0][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[1][4]=="O" and  matriz[1][1]=="O" and  matriz[1][2]=="O" and  matriz[1][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[1][0]=="O" and  matriz[1][1]=="O" and  matriz[1][2]=="O" and  matriz[1][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[2][0]=="O" and  matriz[2][1]=="O" and  matriz[2][2]=="O" and  matriz[2][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[2][4]=="O" and  matriz[2][1]=="O" and  matriz[2][2]=="O" and  matriz[2][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[3][4]=="O" and  matriz[3][1]=="O" and  matriz[3][2]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[3][0]=="O" and  matriz[3][1]=="O" and  matriz[3][2]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][0]=="O" and  matriz[4][1]=="O" and  matriz[4][2]=="O" and  matriz[4][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][4]=="O" and  matriz[4][1]=="O" and  matriz[4][2]=="O" and  matriz[4][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        # Condição para verificar as colunas do jogador 2
        elif matriz[0][0]=="O" and  matriz[1][0]=="O" and  matriz[2][0]=="O" and  matriz[3][0]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][0]=="O" and  matriz[1][0]=="O" and  matriz[2][0]=="O" and  matriz[3][0]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[0][1]=="O" and  matriz[1][1]=="O" and  matriz[2][1]=="O" and  matriz[3][1]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][1]=="O" and  matriz[1][1]=="O" and  matriz[2][1]=="O" and  matriz[3][1]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[0][2]=="O" and  matriz[1][2]=="O" and  matriz[2][2]=="O" and  matriz[3][2]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][2]=="O" and  matriz[1][2]=="O" and  matriz[2][2]=="O" and  matriz[3][2]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[0][3]=="O" and  matriz[1][3]=="O" and  matriz[2][3]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][3]=="O" and  matriz[1][3]=="O" and  matriz[2][3]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[4][4]=="O" and  matriz[1][4]=="O" and  matriz[2][4]=="X" and  matriz[3][4]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        elif matriz[0][4]=="O" and  matriz[1][4]=="O" and  matriz[2][4]=="O" and  matriz[3][4]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        # Condições para verificar todas as sequências diagonais do jogador 2
        elif matriz[0][3]=="O" and  matriz[1][2]=="O" and  matriz[2][1]=="O" and  matriz[3][0]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
        
        elif matriz[1][4]=="O" and  matriz[2][3]=="O" and  matriz[3][2]=="O" and  matriz[4][1]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
            
        elif matriz[1][0]=="O" and  matriz[2][1]=="O" and  matriz[3][2]=="O" and  matriz[4][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        elif matriz[0][1]=="O" and  matriz[1][2]=="O" and  matriz[2][3]=="O" and  matriz[3][4]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        elif matriz[0][0]=="O" and  matriz[1][1]=="O" and  matriz[2][2]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        elif matriz[4][4]=="O" and  matriz[1][1]=="O" and  matriz[2][2]=="O" and  matriz[3][3]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

        elif matriz[0][4]=="O" and  matriz[1][3]=="O" and  matriz[2][2]=="O" and  matriz[3][1]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)
    
        elif matriz[4][0]=="O" and  matriz[1][3]=="O" and  matriz[2][2]=="O" and  matriz[3][1]=="O":
            print("------------------------------------")
            print("O JOGADOR %s VENCEU!!"%nome2)
            print("------------------------------------")
            reset(nome2,nome)

     # Função para adicionar vitorias e derrotas no banco de dados e voltar para o menu     
    def reset(x,y):

        # O "x" sempre será o nome vencedor e o "Y" o nome do perdedor

        # Abre o arquivo e adiciona o conteudo em uma lista
        arquivo = open("./PROJETO/./historico/" +  x + ".txt", "r")
        lista  = arquivo.readlines()
        arquivo.close()
        # Abre o arquivo como writing, adiciona 1 na lista de vitória e copia a lista de derrota
        arquivo = open("./PROJETO/./historico/" +  x + ".txt", "w")
        vitoria=int(lista[0])
        derrota=(lista[1])
        vitoria+=1
        arquivo.write("%d\n"%vitoria)
        arquivo.write(derrota)
        arquivo.close()

        # Realiza a mesma função do que esta acima, porem acrescenta na derrota
        arquivob = open("./PROJETO/./historico/" +  y + ".txt", "r")
        listab  = arquivob.readlines()
        arquivob.close()
        arquivob = open("./PROJETO/./historico/" +  y + ".txt", "w")
        vitoriab=(listab[0])
        derrotab = int(listab[1])
        derrotab+=1
        arquivob.write(vitoriab)
        arquivob.write("%d"%derrotab)
        arquivob.close()

        # Chama a função main para que o usuário decida o que fazer dps
        main()    
    

    # Chamando a função jogadores para dar início a partida
    jogadores()            
    
   
    


def main():
    while True:
        print("-----------------Menu--------------")
        print("1 - Criar novo jogador")
        print("2 - Exibir histórico")
        print("3 - Excluir Jogador")
        print("4 - Iniciar uma partida")
        print("5 - Sair do jogo")
        print("------------------------------------")
        print()

        opcao = (input("Escolha uma das opções: "))

      
        if opcao == "1":
            criaNovoJogador()
        elif opcao == "2":
            lerHistorico()
        elif opcao == "3":
            excluirJogador()
        elif opcao == "4":
            partida()
        elif opcao == "5":
            exit()
    
        elif opcao!= "1"  or opcao!= "2" or opcao!= "3" or opcao!= "4" or opcao!= "5":
            print("Opção não existe, por gentileza escolher entre 1 a 5")


   

     



main()