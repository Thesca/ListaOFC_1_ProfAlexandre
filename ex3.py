import random
from unidecode import unidecode
from colorama import Back, Fore, Style

arquivo = "lista_palavras.txt"
alfabeto = "abcdefghijklmnopqrstuvwxyz" #String com todas as letras do alfabeto, para mostrar letras_disponiveis depois

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding='utf-8') as f:
        # método strip remove o '\n' do final da linha
        return [linha.strip() for linha in f] 

lista_aux = le_arquivo(arquivo)
lista = [x for x in lista_aux if len(x) == 5] #Obter todas as palavras somente com 5 letras da lista

# Escolher uma palavra aleatória da lista
palavra = lista[random.randint(0, len(lista) - 1)]
palavra = unidecode(palavra)

# Inicializar o contador de tentativas
tentativas = 5

print("Bem-vindo ao Termo!")

letras_disponiveis = list(alfabeto)

while tentativas > 0:
    print(f"\nVocê tem {tentativas} tentativas restantes.")
    
    user_input = input("Informe uma palavra de 5 letras: ").strip().lower() #Tentativa informada pelo usuário
    
    if len(user_input) != 5: #Looping até o usuario informar palavra válida
        print("Por favor, informe uma palavra de 5 letras.")
        continue
    
    acertos = 0  # Contador de letras na posição correta
    erros = 0   # Contador de letras na palavra, mas na posição errada
    
    for i in range(5):
        """
        if Letra correta, posição correta: verde 
        elif Letra correta, posição errada: amarelo 
        else Letra errada, posição errada: vermelho
        """
        if user_input[i] == palavra[i]:
            print(Fore.GREEN + user_input[i], end=' ')
            acertos += 1
        elif user_input[i] in palavra:
            print(Fore.YELLOW + user_input[i], end=' ')
            erros += 1
        else:
            print(Fore.RED + user_input[i], end=' ')
    
    print(Style.RESET_ALL)  # Resetar as cores do terminal
    
    if acertos == 5:
        print(f"Parabéns! Você acertou. A palavra era '{palavra}'.")
        break #Quebra o looping e acaba o jogo
    else:
        tentativas -= 1
        print(f"{acertos} letras na posição correta, {erros} letras na palavra mas na posição errada. Tente novamente.")
    
    letras_disponiveis = [letra for letra in letras_disponiveis if letra not in user_input] # Remover as letras já usadas das letras disponíveis
    
    print("Letras disponíveis:", ", ".join(letras_disponiveis)) # Mostrar as letras disponíveis do alfabeto

if tentativas == 0:
    print(f"Você esgotou todas as tentativas. A palavra correta era '{palavra}'. O jogo acabou.")
