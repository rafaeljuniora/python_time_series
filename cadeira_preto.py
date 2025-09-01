# oque é um cabeçalho dentro de um arquivo python e pra que serve oque é um docstring e pra que serve
# é o comentario inicial do arquivo utilizado para informar o proposito e funcionalidade do arquivo
# docstring no python são strings usadas para documentar módulos, classes, funções e métodos, utiliza """ pra demarcar e o __doc__ para acessar o comentario




######################################################################

# formate o cabeçalho deste arquivo, depois implemente as funções abaixo e coloque as docstrings

def maximo(nums):
    """O Metodo atual percorre a lista e seleciona o maior numero
    Recebe um numero do tipo INT
    Retorna o maior numero"""
    if not nums:
        raise ValueError("A lista não pode estar vazia")
    
    maior = nums[0]
    for num in nums:
        if num > maior:
            maior = num
    return maior

import re
from typing import Dict, Tuple, Any

def limpa_texto(s: str) -> str:
    """Transforma todo o texto em minusculo e remove todas as pontuações"""
    texto = s.lower()
    texto_limpo = re.sub(r'[.,;:!?\'"()\-_]', ' ', texto)
    return "".join(texto_limpo.split())

def melhor_vendedor(totais: dict):
    """
    Recebe nome do vendedor e o total vendido.
    Retorna (nome, total) com o maior total.
    Se dict vazio, levante ValueError.
    """
    if not totais:
        raise ValueError("O dicionario não pode ser nullo")
    
    melhor_nome = None
    melhor_total= float('-inf')

    for nome,total in totais.items():
        if total > melhor_total:
            melhor_total=total
            melhor_nome=nome
    return (melhor_nome,melhor_total)


print(maximo([3,1,4,1,5,9,6]))

texto = "Teste dO LiMpa nOMes"
print(limpa_texto(texto))

vendas = {"Rafael": 5500, "Pedro": 3200, "Antony": 2800}
print(melhor_vendedor(vendas))
