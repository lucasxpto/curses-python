class Utils:
    def __init__(self):
        pass

    def centraliza(self, stdscr, texto, y=0):
        height, width = stdscr.getmaxyx()
        # Calcula a posição para centralizar o texto na tela
        start_x = int((width // 2) - (len(texto) // 2))
        start_y = height // 2 + y
        return start_x, start_y