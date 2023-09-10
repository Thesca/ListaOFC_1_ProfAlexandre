import os

tab = [[' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ']]

"""
O jogo é controlado pela variavel var_control_player, quando ela é par o jogador é o X, quando impar, o O.
"""

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

#Função para printar a tela
def printa_tela():
    os.system("cls")
    print("    0   1   2   3")
    print("0:  " +tab[0][0] + " | " + tab[0][1] + " | " + tab[0][2] + " | " + tab[0][3])
    print("   ----------------")
    print("1:  " +tab[1][0] + " | " + tab[1][1] + " | " + tab[1][2] + " | " + tab[1][3])
    print("   ----------------")
    print("2:  " +tab[2][0] + " | " + tab[2][1] + " | " + tab[2][2] + " | " + tab[2][3])
    print("   ----------------")
    print("3:  " +tab[3][0] + " | " + tab[3][1] + " | " + tab[3][2] + " | " + tab[3][3])
    print()
    print()
    
max_jogadas = 0 #Variável para não haver mais jogadas do que espaços no tab
var_control_player = 0 #Variavel de controle
def game():
    global var_control_player
    global max_jogadas
    global tab
    while max_jogadas < 16:
        """
        Função principal, aqui serão feitas a lógica do jogo
        """
        printa_tela()
        print("Vez do/a jogador X") if var_control_player % 2 == 0 else print("Vez do/a jogador O")
        user_input_row = int(input("Informe a linha: "))
        user_input_col = int(input("Informe a coluna: "))
        if (user_input_row > 3 or user_input_row < 0) and (user_input_col > 3 or user_input_col < 0): # Verifica os valores inputados
            print("Informe valores válidos.")
            continue
        if tab[user_input_row][user_input_col] != ' ': # Verifica o espaço inputado
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
        max_jogadas += 1
    print("Deu velha!")
game() #Chamada para começar o jogo