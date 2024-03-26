import pygame 

pygame.init()
interfaz=pygame.display.set_mode((450,450))
pygame.display.set_caption("TriKy")

fondo = pygame.image.load("Fondo.png")
circulo = pygame.image.load("Circulo.png")
equis = pygame.image.load("equis.png")

fondo = pygame.transform.scale(fondo,(450,450))
circulo = pygame.transform.scale(circulo,(200,200))
equis = pygame.transform.scale(equis,(200,200))

matriz = [[(10,10),(125,10),(245,10)],
          [(10,120),(125,120),(245,120)],
          [(10,240),(125,240),(245,240)]]

tablero = [["","",""],
           ["","",""],
           ["","",""]]

turno = "x"
fin_Juego = False
clock = pygame.time.Clock()

def graficar_board():
    interfaz.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == "x":
                dibujar_x(fila,col)
            elif tablero[fila][col] == "o":
                dibujar_o(fila,col)

def dibujar_x(fila,col):
    interfaz.blit(equis,(matriz[fila][col]))

def dibujar_o(fila,col):
    interfaz.blit(circulo,(matriz[fila][col]))

def verificar_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return True
    return False
while not fin_Juego:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin_Juego = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 41 and mouseX < 406) and (mouseY >= 47 and mouseY < 403):
                fila = (mouseY - 47)//125
                col = (mouseX - 41)//125
                if tablero[fila][col] == "":
                    tablero[fila][col] = turno
                    fin=verificar_ganador()
                    if fin == True:
                        print(f"El jugador {turno} ha ganado!!")
                        fin_Juego = True
                    turno = "o" if turno == "x" else "x"
    graficar_board()

    pygame.display.update()
pygame.quit()
