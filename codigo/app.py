# app.py
# Correção do código, retirado erros de sintáxe e lógica - P
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

if __name__ == "__main__":
    main()
    print("Meu nome foi Kauan, agora é Pedro")
