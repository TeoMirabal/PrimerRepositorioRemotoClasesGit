import turtle
import time

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong - Teo Edition")
ventana.bgcolor("purple")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Puntajes
puntaje_izq = 0
puntaje_der = 0

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("black")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador1: 0  Jugador2: 0", align="center", font=("Courier", 24, "normal"))

# Estado de pausa
pausado = False

# Texto de pausa
texto_pausa = turtle.Turtle()
texto_pausa.hideturtle()
texto_pausa.color("white")
texto_pausa.penup()
texto_pausa.goto(0, 0)

# Paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.speed(0)
paleta_izq.shape("square")
paleta_izq.color("black")
paleta_izq.shapesize(stretch_wid=6, stretch_len=1)
paleta_izq.penup()
paleta_izq.goto(-350, 0)

# Paleta derecha
paleta_der = turtle.Turtle()
paleta_der.speed(0)
paleta_der.shape("square")
paleta_der.color("black")
paleta_der.shapesize(stretch_wid=6, stretch_len=1)
paleta_der.penup()
paleta_der.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("yellow")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2
pelota.dy = 0.2

# Teclas presionadas
teclas_presionadas = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}

# Funciones para detectar teclas presionadas y soltadas
def presionar_tecla(tecla):
    teclas_presionadas[tecla] = True

def soltar_tecla(tecla):
    teclas_presionadas[tecla] = False

# Función para pausar y reanudar el juego
def toggle_pausa():
    global pausado
    pausado = not pausado
    if pausado:
        texto_pausa.write("PAUSE", align="center", font=("Courier", 36, "bold"))
    else:
        texto_pausa.clear()

# Asignación de eventos
ventana.listen()
ventana.onkeypress(lambda: presionar_tecla("w"), "w")
ventana.onkeyrelease(lambda: soltar_tecla("w"), "w")
ventana.onkeypress(lambda: presionar_tecla("s"), "s")
ventana.onkeyrelease(lambda: soltar_tecla("s"), "s")
ventana.onkeypress(lambda: presionar_tecla("Up"), "Up")
ventana.onkeyrelease(lambda: soltar_tecla("Up"), "Up")
ventana.onkeypress(lambda: presionar_tecla("Down"), "Down")
ventana.onkeyrelease(lambda: soltar_tecla("Down"), "Down")
ventana.onkeypress(toggle_pausa, "p")

# Función para reiniciar la pelota y actualizar el marcador
def reiniciar_pelota(direccion):
    global puntaje_izq, puntaje_der
    pelota.goto(0, 0)
    pelota.dx = 0
    pelota.dy = 0
    ventana.update()

    if direccion == -1:
        puntaje_der += 1
    else:
        puntaje_izq += 1

    marcador.clear()
    marcador.write(f"Jugador1: {puntaje_der}  Jugador2: {puntaje_izq}", align="center", font=("Courier", 24, "normal"))

    time.sleep(1)
    pelota.dx = 0.2 * direccion
    pelota.dy = 0.2

# Bucle principal del juego
while True:
    ventana.update()

    if not pausado:
        # Movimiento continuo de paletas
        if teclas_presionadas["w"] and paleta_izq.ycor() < 250:
            paleta_izq.sety(paleta_izq.ycor() + 0.5)
        if teclas_presionadas["s"] and paleta_izq.ycor() > -240:
            paleta_izq.sety(paleta_izq.ycor() - 0.5)
        if teclas_presionadas["Up"] and paleta_der.ycor() < 250:
            paleta_der.sety(paleta_der.ycor() + 0.5)
        if teclas_presionadas["Down"] and paleta_der.ycor() > -240:
            paleta_der.sety(paleta_der.ycor() - 0.5)

        # Movimiento de la pelota
        pelota.setx(pelota.xcor() + pelota.dx)
        pelota.sety(pelota.ycor() + pelota.dy)

        # Rebote en bordes superior e inferior
        if pelota.ycor() > 290 or pelota.ycor() < -290:
            pelota.dy *= -1

        # Rebote en los laterales (reinicio)
        if pelota.xcor() > 390:
            reiniciar_pelota(-1)

        if pelota.xcor() < -390:
            reiniciar_pelota(1)

        # Colisiones con paletas
        if (340 < pelota.xcor() < 350) and (paleta_der.ycor() - 50 < pelota.ycor() < paleta_der.ycor() + 50):
            pelota.setx(340)
            pelota.dx *= -1

        if (-350 < pelota.xcor() < -340) and (paleta_izq.ycor() - 50 < pelota.ycor() < paleta_izq.ycor() + 50):
            pelota.setx(-340)
            pelota.dx *= -1

    time.sleep(0.0000001) # Ajusta la velocidad de la pelota (a mas cerca de 0, mas rápido)