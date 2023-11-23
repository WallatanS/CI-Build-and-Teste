class testcalculadora(unittest.TestCase):
    def testar_calculadora(self):
        # Teste 1: Soma
        resultado_soma = Operacao.calcular('soma', 5, 3)
        self.assertEqual(resultado_soma, 8, f"Erro no teste de soma. Resultado esperado: 8, Resultado obtido: {resultado_soma}")

        # Teste 2: Subtração
        resultado_subtracao = Operacao.calcular('subtracao', 8, 2)
        self.assertEqual(resultado_subtracao, 6, f"Erro no teste de subtração. Resultado esperado: 6, Resultado obtido: {resultado_subtracao}")

        # Teste 3: Operação inválida
        resultado_invalido = Operacao.calcular('multiplicacao', 4, 2)
        self.assertIsNone(resultado_invalido, f"Erro no teste de operação inválida. Resultado esperado: None, Resultado obtido: {resultado_invalido}")

        print("Todos os testes passaram com sucesso!")

# Executa o teste automatizado
testcalculadora().testar_calculadora()