import turtle
import time

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong - Teo Edition")
ventana.bgcolor("red")
ventana.setup(width=800, height=600)
ventana.tracer(0)

# Puntajes
puntaje_izq = 0
puntaje_der = 0

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("green")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("Jugador A: 0  Jugador B: 0", align="center", font=("Courier", 24, "normal"))


# Paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.speed(0.5)
paleta_izq.shape("square")
paleta_izq.color("black")
paleta_izq.shapesize(stretch_wid=6, stretch_len=1)
paleta_izq.penup()
paleta_izq.goto(-350, 0)

# Paleta derecha
paleta_der = turtle.Turtle()
paleta_der.speed(0.5)
paleta_der.shape("square")
paleta_der.color("white")
paleta_der.shapesize(stretch_wid=6, stretch_len=1)
paleta_der.penup()
paleta_der.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(-100000)  # Velocidad máxima
pelota.shape("circle")
pelota.color("yellow")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.2
pelota.dy = 0.2

# Movimiento de paletas
def paleta_izq_arriba():
    y = paleta_izq.ycor()
    if y < 250:
        paleta_izq.sety(y + 20)

def paleta_izq_abajo():
    y = paleta_izq.ycor()
    if y > -240:
        paleta_izq.sety(y - 20)

def paleta_der_arriba():
    y = paleta_der.ycor()
    if y < 250:
        paleta_der.sety(y + 20)

def paleta_der_abajo():
    y = paleta_der.ycor()
    if y > -240:
        paleta_der.sety(y - 20)

# Controles
ventana.listen()
ventana.onkeypress(paleta_izq_arriba, "w")
ventana.onkeypress(paleta_izq_abajo, "s")
ventana.onkeypress(paleta_der_arriba, "Up")
ventana.onkeypress(paleta_der_abajo, "Down")

# Función para reiniciar la pelota y actualizar el marcador
def reiniciar_pelota(direccion):
    global puntaje_izq, puntaje_der
    pelota.goto(0, 0)
    pelota.dx = 0
    pelota.dy = 0
    ventana.update()

    # Sumar punto
    if direccion == -1:
        puntaje_der += 1
    else:
        puntaje_izq += 1

    # Actualizar marcador
    marcador.clear()
    marcador.write(f"Jugador A: {puntaje_izq}  Jugador B: {puntaje_der}", align="center", font=("Courier", 24, "normal"))

    time.sleep(3)
    pelota.dx = 0.2 * direccion
    pelota.dy = 0.2

# Bucle principal del juego
while True:
    ventana.update()

    # Movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote en bordes superior e inferior
    if pelota.ycor() > 290 or pelota.ycor() < -290:
        pelota.dy *= -1

    # Rebote en los laterales (reinicio)
    if pelota.xcor() > 390:
        reiniciar_pelota(-1)  # Vuelve hacia la izquierda

    if pelota.xcor() < -390:
        reiniciar_pelota(1)   # Vuelve hacia la derecha

    # Colisiones con paletas
    if (340 < pelota.xcor() < 350) and (paleta_der.ycor() - 50 < pelota.ycor() < paleta_der.ycor() + 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (-350 < pelota.xcor() < -340) and (paleta_izq.ycor() - 50 < pelota.ycor() < paleta_izq.ycor() + 50):
        pelota.setx(-340)
        pelota.dx *= -1
    
    time.sleep(0.0000001)