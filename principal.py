"""
Claudinei de Oliveira - UTF8 - pt-br - 15-09-2023
Aluno: Lucas Pedreira Vital
"""

import curses
from curses.textpad import rectangle, Textbox
from validar_cpf import ValidaCPF
from valida_nome import ValidaNome
from valida_email import ValidaEmail
import time
from utils import Utils
from telas import Tela
# https://docs.python.org/3/library/curses.html
class App:
    def __init__(self):
        self.utils = Utils()
        self.tela = Tela()
        curses.wrapper(self.main)

    def exibir_dados(self, stdscr, cpf, nome, email):
        stdscr.clear()
        stdscr.addstr(0, 0, "Dados do Usuário")
        stdscr.addstr(2, 0, f"CPF: {cpf}")
        stdscr.addstr(4, 0, f"Nome: {nome}")
        stdscr.addstr(6, 0, f"Email: {email}")
        stdscr.refresh()
        stdscr.getch()  # Aguarda o usuário pressionar qualquer tecla

    def formatar_cpf(self, cpf_lista):
        cpf_str = ''.join(cpf_lista)
        return cpf_str[:3] + '.' + cpf_str[4:7] + '.' + cpf_str[8:11] + '-' + cpf_str[12:]

    def main(self, stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        
        mostrar_intro = True
        cpf = ''
        while True:
            if mostrar_intro:
                self.tela.introducao(stdscr)
            
            tecla = stdscr.getch()
            
            if tecla == ord('\n'):
                stdscr.clear()
                stdscr.refresh()
                stdscr.addstr(0, 0, "Informe o CPF: ")

                rectangle(stdscr, 1, 0, 1 + 1 + 1, 1 + 15 + 1)

                cpf = [' '] * 14
                pos = 0
                while True:
                    tecla = stdscr.getch(2, pos + 1)
                    if tecla == ord('\n'):  # Se for 'Enter', sair do loop
                        cpf_unmasked = ''.join(cpf).strip()
        
                        if ValidaCPF.valida_cpf(cpf_unmasked):
                            stdscr.addstr(4, 0, "O CPF informado é válido!")
                            stdscr.refresh()
                            # time.sleep(2)  # Mantém a mensagem na tela por 2 segundos, ou o tempo que preferir
                            # stdscr.clear()
                            stdscr.addstr(6, 0, "Informe o nome da pessoa associada ao CPF: ")
                            rectangle(stdscr, 7, 0, 9, 30)
                            nome = ''
                            while True:
                                tecla = stdscr.getch(8, len(nome) + 1)
                                
                                # Limpar a mensagem de validação anterior
                                stdscr.addstr(10, 0, ' ' * 80)
                                
                                if tecla == ord('\n'):  # Se for 'Enter'
                                    if not nome.strip():  # Se o nome estiver vazio
                                        break  # Saia do loop de nome
                                    else:
                                        # Prossiga com a validação do nome
                                        nome_validado, mensagem = ValidaNome.valida_nome(nome)
                                        if nome_validado is not None:
                                            # Exiba mensagem de nome válido e encerre o loop
                                            stdscr.addstr(10, 0, mensagem)
                                            stdscr.refresh()
                                            time.sleep(1)
                                            break
                                        else:
                                            # Exiba mensagem de erro e permita ao usuário corrigir o nome
                                            stdscr.addstr(10, 0, mensagem)
                                            stdscr.refresh()
                                            time.sleep(1)
                                            stdscr.addstr(10, 0, ' ' * len(mensagem))  # Limpa a mensagem de erro
                                elif tecla == curses.KEY_BACKSPACE or tecla == 127:  # Se for backspace
                                    if len(nome) > 0:  # Se houver caracteres para apagar
                                        nome = nome[:-1]
                                        stdscr.addch(8, len(nome) + 1, ' ')
                                elif tecla >= 32 and tecla <= 126:  # Se for qualquer caractere ASCII imprimível
                                    if len(nome) == 0 or (len(nome) > 0 and nome[-1] == ' '):  # Se é o início de uma palavra
                                        tecla = tecla - 32 if tecla >= ord('a') and tecla <= ord('z') else tecla  # Converte para maiúscula se for letra minúscula
                                    nome += chr(tecla)
                                    nome = ValidaNome.capitalizar_nome(nome)
                                    stdscr.addch(8, len(nome), chr(tecla))
                        
                                # Chama a função de validação aqui, mas sem exibir a mensagem de sucesso ainda
                                nome_validado, mensagem = ValidaNome.valida_nome(nome)
                                if not nome_validado:
                                    stdscr.addstr(10, 0, mensagem)  # Exibe apenas mensagens de erro
                                    
                            stdscr.addstr(12, 0, "Informe o e-mail da pessoa associada ao CPF e ao nome: ")
                            rectangle(stdscr, 13, 0, 15, 80)
                            email = ''
                            while True:
                                tecla = stdscr.getch(14, len(email) + 1)
                                # Limpar a mensagem de validação anterior
                                stdscr.addstr(16, 0, ' ' * 80)
                                if tecla == ord('\n'):  # Se for 'Enter'
                                    email_validado, mensagem = ValidaEmail.valida_email(email)
                                    if email_validado is not None:
                                        stdscr.addstr(16, 0, mensagem)  # Ajuste a posição conforme necessário
                                        stdscr.refresh()
                                        time.sleep(1)
                                        cpf_formatado = self.formatar_cpf(cpf)
                                        self.exibir_dados(stdscr, cpf_formatado, nome, email)  # Exibe os dados após o email ser validado
                                        break  # Se o e-mail é válido, sair do loop
                                    else:
                                        stdscr.addstr(16, 0, mensagem)
                                        stdscr.refresh()
                                        time.sleep(1)
                                        stdscr.addstr(16, 0, ' ' * len(mensagem))  # Limpa a mensagem de erro
                                elif tecla == curses.KEY_BACKSPACE or tecla == 127:  # Se for backspace
                                    if len(email) > 0:
                                        email = email[:-1]
                                        stdscr.addch(14, len(email) + 1, ' ')
                                elif tecla >= 32 and tecla <= 126:  # Se for um caractere imprimível
                                    email += chr(tecla)
                                    stdscr.addch(14, len(email), chr(tecla))

                        else:
                            stdscr.addstr(4, 0, "O CPF informado é inválido!")
                            stdscr.refresh()
                            time.sleep(2)  # Mantém a mensagem na tela por 2 segundos, ou o tempo que preferir
                            stdscr.addstr(4, 0, ' ' * 30)  # Limpa a mensagem de erro
                            stdscr.addstr(2, 1, ' ' * 14)  # Limpa o conteúdo dentro do retângulo
                            stdscr.addch(2, 4, ' ')  # Limpa o primeiro ponto da máscara
                            stdscr.addch(2, 8, ' ')  # Limpa o segundo ponto da máscara
                            stdscr.addch(2, 12, ' ')  # Limpa o hífen da máscara
                            cpf = [' '] * 14  # Limpa a lista cpf
                            pos = 0  # Reinicia a posição do cursor

                    elif tecla == curses.KEY_RIGHT and pos < 13:  # Mover para a direita
                        pos += 1
                        if pos in [3, 7, 11]:  # Pular os caracteres da máscara
                            pos += 1
                    elif tecla == curses.KEY_LEFT and pos > 0:  # Mover para a esquerda
                        pos -= 1
                        if pos in [3, 7, 11]:  # Pular os caracteres da máscara
                            pos -= 1
                    elif tecla >= ord('0') and tecla <= ord('9'):  # Se for dígito
                        if pos <= 13:
                            cpf[pos] = chr(tecla)
                            stdscr.addch(2, pos + 1, chr(tecla))
                            if pos <= 13:
                                pos += 1
                                if pos in [3, 7, 11]:  # Pular os caracteres da máscara
                                    pos += 1
                            stdscr.move(2, pos + 1)  # Mover o cursor para a posição correta após a entrada
                    elif tecla == curses.KEY_BACKSPACE or tecla == 127:  # Se for backspace
                        if pos > 0 and pos <= 13:
                            if pos in [3, 7, 11]:  # Se o cursor está em uma posição de máscara
                                pos -= 1  # Mover uma posição à esquerda antes de remover
                            cpf[pos] = ' '
                            stdscr.addch(2, pos + 1, ' ')
                            pos -= 1  # Mover uma posição à esquerda após remover
                        if pos > 13:  # Se o cursor está na última posição
                            pos -= 1
                            cpf[pos] = ' '
                            stdscr.addch(2, pos + 1, ' ')
                        elif pos == 0:  # Se o cursor está na primeira posição
                            cpf[pos] = ' '
                            stdscr.addch(2, pos + 1, ' ')

                    # Adicionando e removendo a máscara de forma gradual
                    cpf = ValidaCPF.aplicar_mascara(stdscr, cpf, pos)

                cpf = ''.join(cpf).strip()
                stdscr.refresh()
                mostrar_intro = False
        

        

if __name__ == "__main__":
    App()

