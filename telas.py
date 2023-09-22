"""
Claudinei de Oliveira - UTF8 - pt-br - 15-09-2023
Aluno: Lucas Pedreira Vital
"""

from utils import Utils
import curses
class Tela:
    def __init__(self):
        self.utils = Utils()

    def introducao(self, stdscr):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        white_on_green = curses.color_pair(1)
        green = curses.color_pair(2)

        # Texto a ser centrado
        ifro = " IFRO "
        campus = "Campus Ariquemes - RO"
        enter = "Pressione ENTER para iniciar... "
        posicao_ifro = self.utils.centraliza(stdscr, ifro, -4)
        posicao_campus = self.utils.centraliza(stdscr, campus, -2)
        posicao_enter = self.utils.centraliza(stdscr, enter, 0)
        # Desenha o texto
        stdscr.addstr(posicao_ifro[1], posicao_ifro[0], ifro, white_on_green | curses.A_BOLD | curses.A_BLINK)
        stdscr.addstr(posicao_campus[1], posicao_campus[0], campus, green | curses.A_BOLD)
        stdscr.addstr(posicao_enter[1], posicao_enter[0], enter, green | curses.A_LOW)
        stdscr.refresh()