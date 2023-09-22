"""
Claudinei de Oliveira - UTF8 - pt-br - 15-09-2023
Aluno: Lucas Pedreira Vital
"""

import re

class ValidaEmail:
    @staticmethod
    def valida_email(email):
        email_temp = email.strip()
        if not email_temp:
            return None, "E-mail não pode estar vazio"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_temp):
            return None, "Formato de e-mail inválido"
        else:
            return email_temp, "E-mail válido!!!"
