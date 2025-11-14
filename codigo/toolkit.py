# app.py
# Um toolkit de matemática com várias funcionalidades.
# Código original de Kauan e Pedro, refatorado e organizado por Kauan;

import math
import random

# ==============================================================================
# 1. FUNÇÕES DO CONVERSOR NUMÉRICO
# ==============================================================================

def converter_real_para_inteiro():
    """
    Inicia um programa interativo para converter números reais para inteiros.
    Permite até 10 conversões por sessão.
    """
    print("\n--- Conversor de Número Real para Inteiro ---")
    print("Você tem 10 tentativas. Digite 'sair' para voltar ao menu.")
    
    contagem = 0
    while contagem < 10:
        valor_str = input(f"\n[Tentativa {contagem + 1}/10] Digite um número real: ")
        
        if valor_str.lower() == 'sair':
            print("Voltando ao menu principal...")
            break
        
        try:
            num = float(valor_str)
            print(f"O valor digitado foi {num}")
            print(f"Número inteiro (com math.trunc): {math.trunc(num)}")
            print(f"Número inteiro (com int):        {int(num)}")
            print(f"Arredondado (com round):         {round(num)}")
            contagem += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido.")

# ==============================================================================
# 2. FUNÇÕES DE MÉDIA PONDERADA
# ==============================================================================

def calcular_media_ponderada(valores, pesos):
    """
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
    if len(valores) != len(pesos):
        raise ValueError("As listas de valores e pesos devem ter o mesmo tamanho.")

    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    numerador = sum(valor * peso for valor, peso in zip(valores, pesos))
    
    return numerador / soma_pesos

def exemplo_media_ponderada():
    """Demonstra o cálculo da média ponderada com um exemplo de notas."""
    print("\n--- Exemplo: Média Ponderada de Notas ---")
    notas = [8.0, 7.5, 9.5]
    pesos_notas = [2, 3, 5]
    
    try:
        media_final = calcular_media_ponderada(notas, pesos_notas)
        print(f"Notas: {notas}")
        print(f"Pesos: {pesos_notas}")
        print(f"A média ponderada final é: {media_final:.2f}")
    except ValueError as e:
        print(f"Erro no cálculo: {e}")

# ==============================================================================
# 3. FUNÇÕES DE PROBABILIDADE
# ==============================================================================

def calcular_probabilidade_simples(favoraveis, total):
    """Calcula a probabilidade de um evento simples."""
    if total == 0:
        raise ValueError("O número total de resultados não pode ser zero.")
    return favoraveis / total

def exemplo_probabilidade_simples():
    """Demonstra o cálculo da probabilidade de tirar um número par em um dado."""
    print("\n--- Exemplo: Probabilidade de Tirar um Número Par em um Dado ---")
    total_resultados = 6
    resultados_favoraveis = 3
    
    probabilidade = calcular_probabilidade_simples(resultados_favoraveis, total_resultados)
    
    print(f"A probabilidade é de {probabilidade:.2f} ou {probabilidade:.2%}")

def exemplo_probabilidade_combinatoria():
    """Demonstra o cálculo de probabilidade usando combinatória (cartas de baralho)."""
    print("\n--- Exemplo: Probabilidade de Tirar 2 Reis de um Baralho ---")
    
    # Total de maneiras de pegar 2 cartas de 52
    total_combinacoes = math.comb(52, 2)
    
    # Total de maneiras de pegar 2 Reis de 4
    combinacoes_favoraveis = math.comb(4, 2)
    
    probabilidade = combinacoes_favoraveis / total_combinacoes
    
    print(f"Total de combinações de 2 cartas: {total_combinacoes}")
    print(f"Combinações favoráveis (2 Reis): {combinacoes_favoraveis}")
    print(f"A probabilidade é de {probabilidade:.4f} ou {probabilidade:.4%}")

def simular_soma_dados(numero_de_simulacoes=100_000):
    """Estima a probabilidade da soma de dois dados ser 7 através da simulação."""
    sucessos = 0
    for _ in range(numero_de_simulacoes):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        if dado1 + dado2 == 7:
            sucessos += 1
    return sucessos / numero_de_simulacoes

def exemplo_probabilidade_simulacao():
    """Demonstra a estimativa de probabilidade por simulação (soma de dados)."""
    print("\n--- Exemplo: Simulação da Soma de Dois Dados ser 7 ---")
    num_simulacoes = 1_000_000
    probabilidade_estimada = simular_soma_dados(num_simulacoes)
    
    print(f"Após {num_simulacoes:,} simulações...")
    print(f"A probabilidade estimada é de {probabilidade_estimada:.4f} ou aproximadamente {probabilidade_estimada:.2%}")

# ==============================================================================
# MENU PRINCIPAL E EXECUÇÃO
# ==============================================================================

def main():
    """Função principal que exibe o menu e gerencia o programa."""
    while True:
        print("\n===== TOOLKIT DE MATEMÁTICA =====")
        print("1. Conversor de Número Real para Inteiro")
        print("2. Exemplo: Calcular Média Ponderada")
        print("3. Exemplo: Probabilidade Simples (Dado)")
        print("4. Exemplo: Probabilidade com Combinatória (Cartas)")
        print("5. Exemplo: Probabilidade por Simulação (Soma de Dados)")
        print("0. Sair do Programa")
        
        escolha = input(">> Escolha uma opção: ")
        
        if escolha == '1':
            converter_real_para_inteiro()
        elif escolha == '2':
            exemplo_media_ponderada()
        elif escolha == '3':
            exemplo_probabilidade_simples()
        elif escolha == '4':
            exemplo_probabilidade_combinatoria()
        elif escolha == '5':
            exemplo_probabilidade_simulacao()
        elif escolha == '0':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
