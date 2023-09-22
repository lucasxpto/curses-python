"""
Claudinei de Oliveira - UTF8 - pt-br - 15-09-2023
Aluno: Lucas Pedreira Vital
"""


# Importa o módulo de testes unitários do Python,
# o unittest, que fornece uma estrutura para criar  e
# executar testes unitários em código Python
import unittest
from validar_cpf import ValidaCPF

# Importa a função valida_cpf do módulo testa_cpf,
# que é a função que verifica se um número de CPF é válido.


# Definição da classe de teste para a função valida_cpf
class TestValidaCpf(unittest.TestCase):
    # Teste de unidade que verifica se a função valida_cpf reconhece corretamente um CPF válido
    def test_valida_cpf_valido(self):
        # Verifica se a função valida_cpf retorna True para um CPF válido
        # Para testar: usamos CPF "529.982.247-25", que é um CPF válido
        # A função deve retornar True para indicar que reconheceu o CPF como válido.
        self.assertTrue(valida_cpf('52998224725'), 'A função não validou corretamente um CPF válido.')

    # Teste de unidade que verifica se a função valida_cpf reconhece corretamente um CPF inválido
    def test_valida_cpf_invalido(self):
        # verifica se a função valida_cpf retorna False para um CPF invalido # CPF "111.111.111-11", é um CPF inválido.
        # este método deve retornar False para indicar que reconheceu o CPF como inválido
        self.assertFalse(ValidaCPF.valida_cpf('11111111111'), 'A função não reconheceu corretamente um CPF inválido.')

    # Teste de unidade que verifica se a função mascara_cpf retorna o CPF formatado
    def test_mascara_cpf(self):
        # Verifica se a função mascara_cpf retorna o CPF formatado
        # Para testar: usamos CPF "529.982.247-25", que é um CPF válido
        # A função deve retornar True para indicar que reconheceu o CPF como válido.
        self.assertEqual(ValidaCPF.aplicar_mascara('52998224725'), '529.982.247-25', 'A função não formatou corretamente o CPF.')

# Verifica se este arquivo é o ponto de entrada do programa
if __name__ == '__main__':
    # Se for, inicia a execução dos testes de unidade
    unittest.main()
