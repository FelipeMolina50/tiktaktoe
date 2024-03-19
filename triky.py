import pygame

class ElementoGrafico:
    def __init__(self, imagen, escala):
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, escala)
        self.rect = self.imagen.get_rect()

    def dibujar(self, superficie, posicion):
        superficie.blit(self.imagen, posicion)

class Tablero(ElementoGrafico):
    def __init__(self, imagen, escala):
        super().__init__(imagen, escala)

class Ficha(ElementoGrafico):
    def __init__(self, imagen, escala):
        super().__init__(imagen, escala)

class Equis(Ficha):
    def __init__(self, imagen, escala):
        super().__init__(imagen, escala)

class Circulo(Ficha):
    def __init__(self, imagen, escala):
        super().__init__(imagen, escala)

class Juego:
    def __init__(self):
        pygame.init()
        self.interfaz = pygame.display.set_mode((450,450))
        pygame.display.set_caption("TriKy")

        self.tablero = Tablero("tiktaktoe/Fondo.png", (450, 450))
        self.equis = Equis("tiktaktoe/equis.png", (200, 200))
        self.circulo = Circulo("tiktaktoe/Circulo.png", (200, 200))

        self.matriz = [[(10,10),(125,10),(245,10)],
                       [(10,120),(125,120),(245,120)],
                       [(10,240),(125,240),(245,240)]]

        self.tablero_estado = [["","",""],
                               ["","",""],
                               ["","",""]]

        self.turno = "x"
        self.fin_Juego = False
        self.clock = pygame.time.Clock()

    def graficar_board(self):
        self.tablero.dibujar(self.interfaz, (0, 0))
        for fila in range(3):
            for col in range(3):
                if self.tablero_estado[fila][col] == "x":
                    self.equis.dibujar(self.interfaz, self.matriz[fila][col])
                elif self.tablero_estado[fila][col] == "o":
                    self.circulo.dibujar(self.interfaz, self.matriz[fila][col])

    def verificar_ganador(self):
        for i in range(3):
            if self.tablero_estado[i][0] == self.tablero_estado[i][1] == self.tablero_estado[i][2] != "":
                return True
            if self.tablero_estado[0][i] == self.tablero_estado[1][i] == self.tablero_estado[2][i] != "":
                return True
        if self.tablero_estado[0][0] == self.tablero_estado[1][1] == self.tablero_estado[2][2] != "":
            return True
        if self.tablero_estado[0][2] == self.tablero_estado[1][1] == self.tablero_estado[2][0] != "":
            return True
        return False

    def ejecutar(self):
        while not self.fin_Juego:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.fin_Juego = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    if (41 <= mouseX < 406) and (47 <= mouseY < 403):
                        fila = (mouseY - 47) // 125
                        col = (mouseX - 41) // 125
                        if self.tablero_estado[fila][col] == "":
                            self.tablero_estado[fila][col] = self.turno
                            fin = self.verificar_ganador()
                            if fin:
                                print(f"El jugador {self.turno} ha ganado!!")
                                self.fin_Juego = True
                            self.turno = "o" if self.turno == "x" else "x"
            self.graficar_board()
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()