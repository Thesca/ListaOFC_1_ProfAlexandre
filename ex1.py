import os
#funções all e any
"""
l = [1,2,3,4,5,6]
#funcao que retorna se todos sao pares

def soh_pares(lista):
    for i in lista:
        if i % 2 != 0:
            return False
    return True

# verifica se uma lista possui valor True
print(([x for x in l if x % 2 == 0]))

#verificar se uma lista possui string
print(any([type(x) == str for x in l]))
"""

#verificar se todos sao int
tab = [[' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' '],
       [' ', ' ', ' ', ' ']]
#verificar se todos sao int
#print(all([type(x) == int for x in l]))

#coluna
def vence_coluna(col):
    if var_control_player % 2 == 0:
        return all([tab[x][col] == 'X' for x in range (len(tab))])
    else:
        return all([tab[x][col] == 'O' for x in range (len(tab))])

#diagonal principal
def vence_diag_prin():
    if var_control_player % 2 == 0:
        return all([tab[i][i] == 'X' for i in range(len(tab))])
    else:
        return all([tab[i][i] == 'O' for i in range(len(tab))])

#diagonal secundaria
def vence_diag_sec():
    if var_control_player % 2 == 0:
        return all([tab[i][len(tab) - i - 1] == 'X' for i in range(len(tab))])
    else:
        return all([tab[i][len(tab) - i - 1] == 'O' for i in range(len(tab))])
    
#linha
def vence_linha(row):
    if var_control_player % 2 == 0:
        return all([x == 'X' for x in row])
    else:
        return all([x == 'O' for x in row])

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
    
max_jogadas = 0
var_control_player = 0
def game():
    global var_control_player
    global tab
    while max_jogadas != 16:
        printa_tela()
        print("Vez do/a jogador X") if var_control_player % 2 == 0 else print("Vez do/a jogador O")
        user_input_row = int(input("Informe a linha: "))
        user_input_col = int(input("Informe a coluna: "))
        if (user_input_row > 3 or user_input_row < 0) and (user_input_col > 3 or user_input_col < 0):
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
game()
"""
while True:
    print("Vez do/a jogador X") if var_control_player % 2 == 0 else print("Vez do/a jogador O")
    user_input_row = int(input("Informe a linha: "))
    user_input_col = int(input("Informe a coluna: "))
    if (user_input_row > 3 or user_input_row < 0) and (user_input_col > 3 or user_input_col < 0):
        print("Informe valores válidos.")
        continue
    if tab[user_input_row][user_input_col] != ' ':
        print("Informe uma jogada válida.")
        continue
    tab[user_input_row][user_input_col] = 'X' if var_control_player % 2 == 0 else "O"
    var_control_player += 1
"""
    
    
