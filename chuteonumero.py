import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarAleatorio()
        self.PedirValor()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_chute) > self.valor_aleatorio:
                    print("Chute um valor mais baixo!")
                    self.PedirValor()
                elif int(self.valor_chute) < self.valor_aleatorio:
                    print("Chute um valor mais alto!")
                    self.PedirValor()
                if int(self.valor_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print("Você acertou!")
        except:
            print("Favor, digitar apensar números!")
            self.Iniciar()
    
    def PedirValor(self):
        self.valor_chute = input("Chute um número: ")
    
    def GerarAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()

