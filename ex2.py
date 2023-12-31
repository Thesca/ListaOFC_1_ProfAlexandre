import os
#Verifica a coluna recebida se há ganhadores
def vence_coluna(col):
    if var_control_player % 2 == 0:
        return all([tab[x][col] == 'X' for x in range (len(tab))])
    else:
        return all([tab[x][col] == 'O' for x in range (len(tab))])

#Verifica diagonal principal
def vence_diag_prin():
    if var_control_player % 2 == 0:
        return all([tab[i][i] == 'X' for i in range(len(tab))])
    else:
        return all([tab[i][i] == 'O' for i in range(len(tab))])

#Verifica diagonal secundaria
def vence_diag_sec():
    if var_control_player % 2 == 0:
        return all([tab[i][len(tab) - i - 1] == 'X' for i in range(len(tab))])
    else:
        return all([tab[i][len(tab) - i - 1] == 'O' for i in range(len(tab))])
    
#Verifica a linha recebida se há ganhadores
def vence_linha(row):
    if var_control_player % 2 == 0:
        return all([x == 'X' for x in row])
    else:
        return all([x == 'O' for x in row])


def printa_tela():
    """
    Função genérica para printar o tabuleiro baseado na ordem da matriz
    """
    os.system("cls")
    out = '    '
    for i in range(ordem):
        out += (f"{i}   ")
    out += ("\n") 
    for i in range(ordem):
        out += (f"{i}:  ")
        for j in range(ordem):
            out += (f"{tab[i][j]}")
            if j == ordem - 1:
                break
            out += (f" | ")
        out += ("\n   ")
        count = 0
        while True:
            if i == ordem-1:
                break
            count += 1
            if count > ordem:
                break
            out += (f"----")
        out += ("\n")
    out += ("\n\n")
    print(out)
    
var_control_player = 0 #Variavel de controle, mesma do exercicio 1
def ambiente():
    """
    Função para definir a ordem do tabuleiro e setar variaveis que serão usadas pelo printa_matriz e para contruir o tabuleiro
    """
    global ordem
    global tab
    ordem = int(input("Qual a ordem do jogo da velha? "))
    tab = [[' ' for i in range(ordem)] for j in range(ordem)]

max_jogadas = 0
def game():
    """
    Função principal onde toda a lógica é feita
    """
    global var_control_player
    global tab
    while max_jogadas != 16:
        printa_tela()
        print("Vez do/a jogador X") if var_control_player % 2 == 0 else print("Vez do/a jogador O")
        user_input_row = int(input("Informe a linha: "))
        user_input_col = int(input("Informe a coluna: "))
        if (user_input_row > ordem - 1 or user_input_row < 0) and (user_input_col > ordem - 1 or user_input_col < 0):
            print("Informe valores válidos.")
            continue
        if tab[user_input_row][user_input_col] != ' ':
            print("Informe uma jogada válida.")
            continue
        tab[user_input_row][user_input_col] = 'X' if var_control_player % 2 == 0 else "O"
        col_result = vence_coluna(user_input_col)
        row_result = vence_linha(tab[user_input_row])
        diag_prin_result = vence_diag_prin()
        diag_sec_result = vence_diag_sec()
        if col_result == True or row_result == True or  diag_prin_result == True or diag_sec_result == True:
            printa_tela()
            print("Jogador/a X venceu!") if var_control_player % 2 == 0 else print("Jogador/a O venceu!")
            exit()
        var_control_player += 1
    print("Deu velha!")
ambiente() #Chamada para definir a ordem e contruir o tabuleiro
game() #Chamada para começar o jogo
