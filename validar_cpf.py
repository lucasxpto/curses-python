"""
Claudinei de Oliveira - UTF8 - pt-br - 18-08-2023
Aluno: Lucas Pedreira Vital
testa_cpf.py
"""

# código importa o módulo re (que representa "expressões regulares")
# da biblioteca padrão do Python - que são chamadas de regex
# Expressões regulares, podem ser usadas para pesquisar, combinar e
#manipular texto de maneira complexa e flexível

import re


class ValidaCPF:

    @staticmethod
    def valida_cpf(cpf):
        # Verifica se um CPF é válido.
        # tem como parâmero: uma string representando um CPF
        # e retorna True se o CPF for válido, False se inválido

        # Remove caracteres não numéricos do CPF
        cpf=''.join(re.findall(r'\d', cpf))

        # Verifica se o CPF tem 11 digitos
        if len(cpf) != 11:
            return False

        # Verifica se o CPF tem todos os digitos iguals (inválido)
        if cpf == cpf[0] * 11:
            return False

        # Calcula os digitos verificadores do CPF
        def calcula_digito(d):

            # Calcula o digito verificador de um CPF
            # soma dos produtos dos digitos do CPF por um peso especifico
            # retorna o digito verificador.

            return (11 - d % 11) % 10

        # Calcula o primeiro digito verificador
        digito1 = sum(i * int(cpf[idx]) for idx, i in enumerate(range(10, 1, -1)))

        # Calcula o segundo digito verificador (incluindo o primeiro digito verificador)
        digito2 = sum(i * int(cpf[idx]) for idx, i in enumerate(range(11, 1, -1)))

        # Retorna True se os digitos calculados correspondem aos digitos do CPF
        return  cpf[-2:] == f'{calcula_digito(digito1)}{calcula_digito(digito2)}'

    @staticmethod
    def aplicar_mascara(stdscr, cpf, pos):
        # Adicionando e removendo a máscara de forma gradual
        if len(''.join(cpf[:3]).strip()) == 3:
            stdscr.addch(2, 4, '.')
        else:
            stdscr.addch(2, 4, ' ')

        if len(''.join(cpf[4:7]).strip()) == 3:
            stdscr.addch(2, 8, '.')
        else:
            stdscr.addch(2, 8, ' ')

        if len(''.join(cpf[8:11]).strip()) == 3:
            stdscr.addch(2, 12, '-')
        else:
            stdscr.addch(2, 12, ' ')

        return cpf

