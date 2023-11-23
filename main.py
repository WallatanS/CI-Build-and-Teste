class Operacao:
    @staticmethod
    def calcular(operacao, num1, num2):
        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        else:
            resultado = None
            print("Operação inválida. Escolha entre 'soma' e 'subtracao'.")
        return resultado

if __name__ == "__main__":
    # Exemplos de uso:
    print("Soma de 5 e 3:", Operacao.calcular('soma', 4, 3))
    print("Subtração de 8 e 2:", Operacao.calcular('subtracao', 8, 2))
