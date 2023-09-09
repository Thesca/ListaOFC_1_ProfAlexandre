import random
from unidecode import unidecode

arquivo = "lista_palavras.txt"

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas """    
    with open(arq, encoding='utf-8') as f:
        # método strip remove o '\n' do final da linha
        return [linha.strip() for linha in f] 

lista_aux = le_arquivo(arquivo)
lista = [x for x in lista_aux if len(x) == 5]

palavra = lista[random.randint(0, len(lista))]
palavra = unidecode(palavra)
print(palavra)

