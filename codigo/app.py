# app.py
from math import trunc

def hello_world():
    """Hello world"""
    print("Hello, world!")


if __name__ == "__main__":
    hello_world()

# Kauan

def main():

    num = float(imput('Digite um valor: '))
    print('O valor digitado foi {} e a sua porção inteira é {}', format(num, trunc(num)))
    
    print("Meu nome é Kauan")
    
    
# Como fazer sem biblioteca? 
# Nesse caso não precisaria importar da biblioteca math (matemática) a funcão trunc, usariamos o 'int' no lugar.
    
    num = float(imput('Digite um valor: '))
    print('O valor digitado foi {} e a sua porção inteira é {}', fromat(num, int(num)))
