"""
Claudinei de Oliveira - UTF8 pt-br - 18-08-2023
Aluno: Lucas Pedreira Vital
test_principal.py
"""

# Importa a biblioteca pytest, que é utilizada para
# escrever testes simples e escaláveis
import pytest
from validar_cpf import ValidaCPF

# import patch: a função patch do módulo mock da biblioteca
# de testes unittest é usada para substituir objetos dentro
# do escopo de um teste, como simular funções e métodos
from unittest.mock import patch

# Importa a classe App do módulo principal.py que contém a lógica
# principal do programa e será a classe que será testada neste
# módulo de testes de integração.
from principal import App


# Testa a integração da função pede_cpf com um CPF válido
def test_valida_cpf_integration_valido(mocker):
    # Instanciar a classe App do módulo principal.py
    app = App()

    # Um exemplo de CPF válido para o teste
    cpf_valido = '12345678909'

    # Adicionar mais caracteres à entrada do usuário (vários "Enter") para evitar a exceção StopIteration
    user_input = list(cpf_valido + '\n' + '\n' + '\n')

    # Simular a entrada do usuário
    with patch('readchar.readchar', side_effect=user_input):
        # Substituir a função 'print' embutida por um objeto de simulação
        mock_print = mocker.patch('builtins.print')

        # Executar o método 'pede_cpf' da classe 'App'
        app.pede_cpf()

        # Verificar se a função 'print' foi chamada com a saída esperada
        mock_print.assert_called_with('Encerrando o programa...')

#Testa a integração de função pede cot com un CPF Invalido
def test_valida_cpf_integration_invalido(mocker):
    app = App() # Instancia a classe App do modula principal.py
    cpf_invalido = '11111111111' # exemplo de CPF inválido para o teste
    # Adicionar mais caracteres à entrada do usuário (varios "Enter")
    # para evitar a exceção StopIteration
    user_input = list(cpf_invalido + '\n' + '\n' + '\n')
    # Simular a entrada do usuário
    with patch('readchar.readchar', side_effect=user_input):
        # Substituir a função 'print' embutida por um objeto de simulação
        mock_print = mocker.patch('builtins.print')

        # Executar o método "pede cor da classe "App"
        app.pede_cpf()
        # Verificar se a função 'print' fol chamada cosa saída esperada 
        mock_print.assert_called_with('Encerrando o programa...')
# simular um usuário que pressionou a tecla de backspace enquanto digitava seu CPF.
def test_valida_cpf_integration_with_backspace(mocker):
    # Instanciar a classe App do módulo principal.py
    app = App()
    # CPF com backspace
    cpf_with_backspace = '12345\x7f6789\x7f0909'
    # Adicionar mais caracteres à entrada do usuário (vários "Enter") para evitar a exceção StopIteration
    user_input = list(cpf_with_backspace + '\n' + '\n' + '\n')
    # Simular a entrada do usuário
    with patch('readchar.readchar', side_effect=user_input):
        # Substituir a função 'print' embutida por um objeto de simulação
        mock_print = mocker.patch('builtins.print')
        # Executar o método 'pede_cpf' da classe 'App'
        app.pede_cpf()
        # Verificar se a função 'print' foi chamada com a saída esperada
        mock_print.assert_called_with('Encerrando o programa...')