class Calculadora:
    # o metodo __init__ é sempre executado na instanciação da classe.
    # caso a classe não tem inicialização não precisa criar o __init__
    def __init__(self):
        pass
    # Metodos
    def soma(self, a, b):
        return a+b
    def subtracao (self,a,b):
        return a-b
    def multiplicasao (self,a,b):
        return a*b
    def divisao (self,a,b):
        return a/b
if __name__ == '__main__':
    calculadora = Calculadora()

    print(calculadora.soma(4,5))
    print(calculadora.subtracao(3,5))
    print(calculadora.multiplicasao(1,2))
    print(calculadora.divisao(6,2))