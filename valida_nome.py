import re
import time

class ValidaNome:
    @staticmethod
    def valida_nome(nome):
        nome_temp = nome.strip()  # Remove espaços no início e final do nome
        if len(nome_temp) < 2:
            # time.sleep(1) # Espera 1 segundo antes de retornar
            return None, "Nome deve ter duas letras ou mais"
        elif re.search(r'[^a-zA-Z\s]', nome_temp):
            # time.sleep(1) # Espera 1 segundo antes de retornar
            return None, "Nome com caracteres especiais não é elegível para este sistema"
        else:
            nome_temp = re.sub(r'\s+', ' ', nome_temp)  # Reduz espaços múltiplos entre palavras a um único espaço
            nome_temp = ' '.join(word.capitalize() for word in nome_temp.split())  # Mantenha apenas a inicial de cada palavra em maiúscula
            return nome_temp, "Nome válido!!!"

    @staticmethod
    def capitalizar_nome(nome):
        if len(nome) == 0 or nome[-1] == ' ':  # Se for a primeira letra da palavra
            return nome.capitalize()
        return nome
