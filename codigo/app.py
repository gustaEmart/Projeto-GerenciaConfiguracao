# app.py
# Correção do código, retirando erros de sintáxe e lógica - P
from math import trunc

def main():
    print("Conversor de Número Real para Inteiro (apenas 10 tentativas por vez)")
    contagem = 0
    while contagem < 10:
        valor = input("\nDigite um número real (ou digite 'sair' para encerrar): ")
        if valor.lower() == 'sair':
            print("Encerrando programa...")
            break
        # Refatoração de código feita para tratar entradas inválidas - P.   
        try:
            num = float(valor)
            print(f"O valor digitado foi {num}")
            print(f"Número inteiro (com math.trunc): {trunc(num)}")
            print(f"Número inteiro (com int):        {int(num)}")
            print(f"Arredondado:                    {round(num)}") # adição de nova função round.
            contagem += 1
        except ValueError:
            print("Entrada inválida. Tente novamente com um número.")

 """ Proxímo passo é:
    Calcula a média ponderada de uma lista de valores com seus respectivos pesos.
    
    Args:
        valores (list): Uma lista de números (ex: notas).
        pesos (list): Uma lista de pesos correspondentes a cada valor.
        
    Returns:
        float: O valor da média ponderada.
        
    Raises:
        ValueError: Se as listas de valores e pesos não tiverem o mesmo tamanho
                    ou se a soma dos pesos for zero.
    """

    
def calcular_media_ponderada(valores, pesos):
    
    # 1. Verifica se as listas têm o mesmo número de elementos
    if len(valores) != len(pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    # 2. Calcula o numerador: a soma de cada valor multiplicado pelo seu peso
    numerador = 0
    for i in range(len(valores)):
        numerador += valores[i] * pesos[i]

    # 3. Calcula o denominador: a soma de todos os pesos
    denominador = sum(pesos)
    
    # 4. Verifica se a soma dos pesos é zero para evitar divisão por zero
    if denominador == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    # 5. Retorna o resultado da divisão
    return numerador / denominador

notas = [8.0, 7.5, 9.5]
pesos_notas = [2, 3, 5]  # A última nota tem o maior peso

media_final = calcular_media_ponderada(notas, pesos_notas)

print(f"Notas: {notas}")
print(f"Pesos: {pesos_notas}")
print(f"A média ponderada final é: {media_final:.2f}") 
# Saída esperada: A média ponderada final é: 8.70

  

if __name__ == "__main__":
    main()
    print("Meu nome foi Kauan, e Pedro, agora é Glauber")
