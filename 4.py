class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        suma = self.num1 + self.num2
        print("suma:", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("resta:", resta)

    def multiplicar(self):
        multiplicar = self.num1 * self.num2
        print("multiplicar:", multiplicar)

    def dividir(self):
        division = self.num1 / self.num2
        print("division:", division)
